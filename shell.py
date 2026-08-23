"""Esqueleto compartilhado das paginas do site: CSS, cabecalho e rodape.

O site e estatico e bilingue. Cada pagina existe em dois arquivos reais
(`/algo/index.html` e `/en/something/index.html`) em vez de um so com troca
por JavaScript: buscador indexa cada idioma na sua URL, e uma pagina que so
monta o texto depois do script chega vazia no rastreador.
"""
from __future__ import annotations

SITE = "https://mendesamd-png.github.io/sincou-site"

# Prefixo de TODO caminho interno. O GitHub Pages serve um repositorio de
# projeto sob /nome-do-repo/, entao um href="/como-funciona/" cai fora do
# site e devolve 404. Num dominio proprio (sincou.com.br) isto vira "" e nada
# mais precisa mudar: `build.rebase()` reescreve os caminhos na hora de
# gravar, em vez de espalhar o prefixo por cada link.
BASE = "/sincou-site"

# ---------------------------------------------------------------- paleta ---
CSS = """
:root {
  --ground: #F7F6F3;
  --ground-2: #FFFFFF;
  --glass: rgba(255, 255, 255, .78);
  --glass-line: rgba(23, 23, 28, .09);
  --ink: #17171C;
  --ink-soft: #55555F;
  --ink-faint: #8A8A95;
  --g1: #8B5CF6;
  --g2: #F472B6;
  --g3: #38BDF8;
  --g4: #FDE047;
  --halo: .34;
  --shadow-sm: 0 10px 30px rgba(23, 23, 28, .07), 0 2px 6px rgba(23, 23, 28, .04);
  --radius: 26px;
  --measure: 62ch;
}
/* claro e o padrao por decisao de produto: o escuro entra pela escolha do
   visitante, nunca pelo tema do sistema */
:root[data-theme="dark"] {
  --ground: #0C0C11;
  --ground-2: #14141B;
  --glass: rgba(255, 255, 255, .06);
  --glass-line: rgba(255, 255, 255, .12);
  --ink: #F4F4F7;
  --ink-soft: #A9A9B6;
  --ink-faint: #75757F;
  --halo: .42;
  --shadow-sm: 0 10px 26px rgba(0, 0, 0, .4);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
  }
}
body {
  margin: 0; background: var(--ground); color: var(--ink);
  font-family: Onest, ui-sans-serif, system-ui, -apple-system, sans-serif;
  font-size: 17px; line-height: 1.6; -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
h1, h2, h3 { margin: 0; font-weight: 500; letter-spacing: -.03em; text-wrap: balance; }
h1 { font-size: clamp(2.5rem, 6vw, 4.6rem); line-height: 1.04; font-weight: 600; }
h2 { font-size: clamp(1.9rem, 3.7vw, 2.9rem); line-height: 1.09; }
h3 { font-size: 1.12rem; font-weight: 600; letter-spacing: -.015em; }
p { margin: 0; }
a { color: inherit; }
::selection { background: var(--g1); color: #fff; }
:focus-visible { outline: 2px solid var(--g1); outline-offset: 3px; border-radius: 6px; }

.wrap { width: min(1160px, 90vw); margin-inline: auto; position: relative; z-index: 1; }
.col { max-width: var(--measure); }
.mono { font-family: "IBM Plex Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; }

.halo {
  position: fixed; border-radius: 50%; filter: blur(110px);
  opacity: var(--halo); pointer-events: none; z-index: 0;
  animation: drift 26s ease-in-out infinite alternate;
}
.halo.a { width: 46vw; height: 46vw; left: -12vw; top: -10vw; background: var(--g1); }
.halo.b { width: 38vw; height: 38vw; right: -8vw; top: 6vh; background: var(--g3); animation-delay: -8s; }
.halo.c { width: 34vw; height: 34vw; left: 22vw; bottom: -14vw; background: var(--g2); animation-delay: -16s; }
@keyframes drift {
  from { transform: translate3d(0, 0, 0) scale(1); }
  to   { transform: translate3d(4vw, 5vh, 0) scale(1.12); }
}

section { padding: clamp(52px, 6.5vw, 92px) 0; position: relative; }
.eyebrow {
  font-family: "IBM Plex Mono", monospace; font-size: .74rem;
  letter-spacing: .14em; text-transform: uppercase; color: var(--ink-faint);
  margin-bottom: 18px;
}
.lede { margin-top: 20px; color: var(--ink-soft); font-size: 1.1rem; max-width: 56ch; }

.glass {
  background: var(--glass);
  backdrop-filter: blur(18px) saturate(150%);
  -webkit-backdrop-filter: blur(18px) saturate(150%);
  border: 1px solid var(--glass-line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.btn {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 13px 26px; border-radius: 999px;
  font-size: .97rem; font-weight: 600; text-decoration: none;
  color: #fff; position: relative; overflow: hidden;
  /* o amarelo entra como brilho na borda: sob o texto ele derrubaria o
     contraste do branco */
  background-image:
    radial-gradient(75% 130% at 112% 50%, rgba(253, 224, 71, .62), transparent 62%),
    linear-gradient(110deg, var(--g1), var(--g2) 46%, var(--g3));
  background-size: 100% 100%, 210% 100%;
  box-shadow: 0 10px 30px rgba(139, 92, 246, .32);
  transition: background-position .6s ease, transform .16s ease, box-shadow .16s ease;
}
.btn:hover {
  background-position: 0 0, 100% 0;
  transform: translateY(-2px); box-shadow: 0 16px 38px rgba(139, 92, 246, .38);
}
.btn:active { transform: translateY(0); }
.btn.quiet {
  background: var(--glass); background-image: none; color: var(--ink);
  backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-line); box-shadow: none;
}
.btn.quiet:hover { transform: translateY(-2px); box-shadow: var(--shadow-sm); }

/* ---------------------------------------------------------------- topo --- */
header { position: sticky; top: 16px; z-index: 30; }
.bar { display: flex; align-items: center; gap: 14px; padding: 10px 12px 10px 20px; border-radius: 999px; }
.brand { display: flex; align-items: center; gap: 10px; font-weight: 700; letter-spacing: -.02em; text-decoration: none; }
.bar nav { margin-left: auto; display: flex; align-items: center; gap: 20px; }
.bar nav a { color: var(--ink-soft); text-decoration: none; font-size: .92rem; }
.bar nav a:hover, .bar nav a[aria-current] { color: var(--ink); }
.bar .btn { padding: 10px 20px; font-size: .9rem; }
.pillbtn {
  height: 34px; padding: 0 12px; border-radius: 999px; cursor: pointer;
  background: transparent; border: 1px solid var(--glass-line);
  color: var(--ink); font: inherit; font-size: .82rem; font-weight: 600;
  display: inline-flex; align-items: center; gap: 6px;
}
.pillbtn:hover { background: var(--glass); }
@media (max-width: 900px) { .bar nav a.hide-sm { display: none; } }

/* --------------------------------------------------------------- rodape --- */
footer { padding: 48px 0 64px; color: var(--ink-faint); font-size: .88rem; }
.foot-grid {
  display: grid; gap: 30px; grid-template-columns: 1.4fr repeat(3, 1fr);
  padding-bottom: 34px; border-bottom: 1px solid var(--glass-line);
}
@media (max-width: 780px) { .foot-grid { grid-template-columns: 1fr 1fr; } }
.foot-grid h4 {
  margin: 0 0 14px; font-size: .72rem; font-weight: 600; letter-spacing: .12em;
  text-transform: uppercase; color: var(--ink-faint);
}
.foot-grid ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 9px; }
.foot-grid a { text-decoration: none; color: var(--ink-soft); }
.foot-grid a:hover { color: var(--ink); }
.foot-end {
  margin-top: 26px; display: flex; flex-wrap: wrap; gap: 14px 28px; align-items: center;
}
.foot-end .spacer { flex: 1; }
.made {
  display: inline-flex; align-items: center; gap: 9px; font-weight: 500;
  color: var(--ink-soft); padding: 7px 15px 7px 9px; border-radius: 999px;
  border: 1px solid var(--glass-line); background: var(--glass);
}
.made svg { display: block; border-radius: 3px; }

/* ------------------------------------------------------- paginas de texto --- */
.doc { padding-top: 40px; }
.doc-body { max-width: 72ch; }
.doc-body h2 { font-size: 1.42rem; margin: 46px 0 14px; letter-spacing: -.02em; }
.doc-body h2:first-child { margin-top: 0; }
.doc-body p, .doc-body li { color: var(--ink-soft); }
.doc-body p + p { margin-top: 14px; }
.doc-body ul { margin: 14px 0 0; padding-left: 20px; display: grid; gap: 9px; }
.doc-body strong { color: var(--ink); font-weight: 600; }
.doc-meta {
  margin-top: 18px; font-family: "IBM Plex Mono", monospace;
  font-size: .78rem; color: var(--ink-faint);
}
.notice {
  margin-top: 30px; padding: 18px 22px; border-radius: 18px;
  border: 1px solid var(--glass-line); background: var(--glass);
  color: var(--ink-soft); font-size: .92rem;
}
"""

JS = """
(function () {
  var btn = document.getElementById("theme");
  var saved = localStorage.getItem("sincou-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  if (btn) btn.addEventListener("click", function () {
    var atual = document.documentElement.getAttribute("data-theme") || "light";
    var novo = atual === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", novo);
    localStorage.setItem("sincou-theme", novo);
    document.dispatchEvent(new CustomEvent("sincou:theme", {detail: novo}));
  });
})();
"""

# O simbolo do Sincou: as pontas DIREITAS sao irregulares porque as tomadas
# tem duracoes diferentes; as ESQUERDAS batem todas no mesmo trilho, e e so
# isso que o programa faz. A irregularidade e a informacao - alinhar as
# pontas direitas "para ficar mais bonito" apaga o significado inteiro.
# O trilho ultrapassa em cima e embaixo para o conjunto nao virar um
# grafico de barras.
LOGO = """<svg width="22" height="22" viewBox="0 0 1024 1024" aria-hidden="true">
  <defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#8B5CF6"/><stop offset=".5" stop-color="#F472B6"/>
    <stop offset="1" stop-color="#38BDF8"/></linearGradient></defs>
  <rect x="248" y="196" width="30" height="632" rx="15" fill="currentColor"/>
  <rect x="286" y="300" width="520" height="112" rx="56" fill="url(#lg)"/>
  <rect x="286" y="456" width="600" height="112" rx="56" fill="url(#lg)" opacity=".82"/>
  <rect x="286" y="612" width="420" height="112" rx="56" fill="url(#lg)" opacity=".64"/>
</svg>"""

# bandeira do Brasil desenhada em SVG: um emoji nao renderiza igual em todo
# sistema (no Windows sai como as letras "BR")
FLAG = """<svg width="20" height="14" viewBox="0 0 28 20" aria-hidden="true">
  <rect width="28" height="20" fill="#009B3A"/>
  <path d="M14 2.6 25.4 10 14 17.4 2.6 10Z" fill="#FEDF00"/>
  <circle cx="14" cy="10" r="4.3" fill="#002776"/>
  <path d="M9.9 8.6a4.3 4.3 0 0 0 8.2 1.5 9 9 0 0 0-8.2-1.5Z" fill="#fff"/>
</svg>"""


# Ordem de exibicao e de rodizio dos idiomas. O botao do topo leva ao
# PROXIMO da lista: com tres idiomas, um botao que alterna entre dois
# deixaria o terceiro inalcancavel.
LANG_ORDER = ("pt", "en", "es")

# prefixo de URL de cada idioma. O portugues mora na raiz porque foi o
# primeiro e os links ja publicados apontam para la.
LANG_BASE = {"pt": "", "en": "/en", "es": "/es"}

HTML_LANG = {"pt": "pt-BR", "en": "en", "es": "es"}


def head(title: str, desc: str, lang: str, path: str,
         alts: dict) -> str:
    """<head> completo, com um alternate por idioma para o buscador.

    `alts` mapeia idioma -> caminho equivalente. Uma pagina que exista em
    dois idiomas e nao no terceiro simplesmente nao aparece no mapa, em vez
    de apontar para um 404 - alternate quebrado e pior que alternate
    ausente, porque o buscador leva o leitor para la.
    """
    linhas = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}">'
        for l, u in alts.items())
    # x-default e para quem nao casa com nenhum idioma: o ingles alcanca
    # mais gente do que o portugues.
    padrao = alts.get("en", path)
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
{linhas}
<link rel="alternate" hreflang="x-default" href="{SITE}{padrao}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Onest:wght@300;400;500;600;700&display=swap">
<style>{CSS}</style>"""


def header(t: dict, base: str, alt_url: str, here: str = "",
           prox_lang: str = "en") -> str:
    """Barra do topo. `base` prefixa os links internos ('' no pt, '/en' no en).

    `prox_lang` e o idioma para onde o botao leva, e vai no hreflang do
    link: sem ele o atributo mentiria assim que existisse um terceiro
    idioma.
    """
    def link(key, url, cls="hide-sm"):
        mark = ' aria-current="page"' if here == key else ""
        return f'<a href="{base}{url}" class="{cls}"{mark}>{t["nav_" + key]}</a>'
    return f"""<header><div class="wrap"><div class="bar glass">
  <a class="brand" href="{base}/">{LOGO} Sincou</a>
  <nav>
    {link("howto", t["url_howto"])}
    {link("pluraleyes", t["url_pluraleyes"])}
    {link("whatsnew", t["url_whatsnew"])}
    <a href="{base}/#preco">{t["nav_price"]}</a>
    <a class="pillbtn" href="{alt_url}" hreflang="{prox_lang}"
       aria-label="{t['lang_switch_aria']}">{t["lang_other"]}</a>
    <button class="pillbtn" id="theme" type="button" aria-label="{t['theme_aria']}">&#9680;</button>
    <a class="btn" href="{base}/#preco">{t["nav_download"]}</a>
  </nav>
</div></div></header>"""


def footer(t: dict, base: str) -> str:
    def li(key, url):
        return f'<li><a href="{base}{url}">{t["nav_" + key]}</a></li>'
    return f"""<footer><div class="wrap">
  <div class="foot-grid">
    <div>
      <a class="brand" href="{base}/" style="font-size:.98rem">{LOGO} Sincou</a>
      <p style="margin-top:12px;color:var(--ink-soft);max-width:34ch">{t["foot_tagline"]}</p>
    </div>
    <div><h4>{t["foot_product"]}</h4><ul>
      {li("howto", t["url_howto"])}
      {li("pluraleyes", t["url_pluraleyes"])}
      {li("whatsnew", t["url_whatsnew"])}
      <li><a href="{base}/#preco">{t["nav_price"]}</a></li>
    </ul></div>
    <div><h4>{t["foot_legal"]}</h4><ul>
      {li("eula", t["url_eula"])}
      {li("terms", t["url_terms"])}
      {li("privacy", t["url_privacy"])}
      {li("refunds", t["url_refunds"])}
    </ul></div>
    <div><h4>{t["foot_contact"]}</h4><ul>
      <li><a href="mailto:{t['email']}">{t["email"]}</a></li>
    </ul></div>
  </div>
  <div class="foot-end">
    <span class="made">{FLAG} {t["made_in"]}</span>
    <span class="spacer"></span>
    <span class="mono">{t["foot_req"]}</span>
  </div>
</div></footer>"""


def proximo_idioma(lang: str) -> str:
    """O idioma seguinte no rodizio, voltando ao inicio no fim da lista."""
    i = LANG_ORDER.index(lang) if lang in LANG_ORDER else 0
    return LANG_ORDER[(i + 1) % len(LANG_ORDER)]


def page(t: dict, *, lang: str, path: str, alts: dict, title: str,
         desc: str, body: str, here: str = "", extra_css: str = "",
         extra_js: str = "") -> str:
    base = LANG_BASE.get(lang, "")
    prox = proximo_idioma(lang)
    # se a pagina nao existir no proximo idioma, o botao leva a home dele:
    # melhor mudar de idioma e cair na capa do que nao poder mudar
    alt_url = alts.get(prox, f"{LANG_BASE.get(prox, '')}/")
    css = f"<style>{extra_css}</style>" if extra_css else ""
    js = f"<script>{extra_js}</script>" if extra_js else ""
    return f"""<!doctype html>
<html lang="{HTML_LANG.get(lang, lang)}">
<head>
{head(title, desc, lang, path, alts)}
{css}
</head>
<body>
<div class="halo a"></div><div class="halo b"></div><div class="halo c"></div>
{header(t, base, alt_url, here, prox)}
<main>
{body}
</main>
{footer(t, base)}
<script>{JS}</script>
{js}
</body>
</html>"""
