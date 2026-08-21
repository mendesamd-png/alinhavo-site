#!/usr/bin/env python3
"""Confere os links do site contra a URL REAL, servindo o prefixo.

    python3 site/check_links.py

Existe por causa de um erro concreto: a primeira verificacao comparava os
hrefs com o sistema de arquivos, onde `/como-funciona/` existe. No ar, o
GitHub Pages serve o repositorio sob `/alinhavo-site/`, e o mesmo href caia
fora do site inteiro e devolvia 404. Comparar com o disco nao pega isso;
comparar com a URL, sim.

O truque e montar uma pasta temporaria com o site dentro de `<BASE>/`, do
mesmo jeito que o Pages monta, e so entao seguir os links.
"""
from __future__ import annotations

import http.server
import re
import shutil
import socketserver
import sys
import tempfile
import threading
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import shell  # noqa: E402

LINK = re.compile(r'(?:href|src)="([^"#][^"]*)"')
PORT = 8911


def _serve(root: Path):
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(root), **kw)

        def log_message(self, *a):
            pass

    socketserver.TCPServer.allow_reuse_address = True
    for porta in range(PORT, PORT + 20):
        try:
            srv = socketserver.TCPServer(("127.0.0.1", porta), H)
            break
        except OSError:
            continue
    else:
        raise SystemExit("nenhuma porta livre para o servidor de teste")
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def main() -> int:
    base = shell.BASE.strip("/")
    tmp = Path(tempfile.mkdtemp())
    raiz = tmp / base if base else tmp
    raiz.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(HERE, raiz,
                    ignore=shutil.ignore_patterns("*.py", "__pycache__"))

    srv, porta = _serve(tmp)
    origem = f"http://127.0.0.1:{porta}"
    inicio = f"{origem}{shell.BASE}/"

    vistos, fila, quebrados, paginas = set(), [inicio], [], 0
    try:
        while fila:
            url = fila.pop()
            if url in vistos:
                continue
            vistos.add(url)
            try:
                with urllib.request.urlopen(url, timeout=5) as r:
                    corpo = r.read()
                    tipo = r.headers.get_content_type()
            except urllib.error.HTTPError as e:
                quebrados.append((url, e.code))
                continue
            except (urllib.error.URLError, OSError) as e:
                quebrados.append((url, str(e)))
                continue

            if tipo != "text/html":
                continue
            paginas += 1
            for href in LINK.findall(corpo.decode("utf-8", "replace")):
                if href.startswith(("http://", "https://", "mailto:", "data:")):
                    continue
                alvo = urllib.parse.urljoin(url, href)
                if alvo.startswith(origem):
                    fila.append(alvo)
    finally:
        srv.shutdown()
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"paginas visitadas : {paginas}")
    print(f"destinos checados : {len(vistos)}")
    if quebrados:
        print(f"\nQUEBRADOS ({len(quebrados)}):")
        for u, e in sorted(set(quebrados)):
            print(f"  {e}  {u.replace(origem, '')}")
        return 1
    print("\nnenhum link quebrado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
