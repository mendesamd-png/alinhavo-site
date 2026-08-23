# Site do Sincou

Página do **Sincou** — sincronização de multicâmera pelo áudio, para
editores de vídeo (macOS).

Este repositório é a **cópia publicada**. O fonte de trabalho vive junto do
aplicativo, em `site/` do repositório do motor, e é gerado por
`python3 site/build.py`: 16 páginas, 8 em português na raiz e 8 em inglês
sob `/en/`.

- Publicado por GitHub Pages a partir da branch `main`.
- `.nojekyll` impede o Jekyll de processar o conteúdo já pronto.
- Antes de publicar, `python3 site/check_links.py` sobe o site sob o
  prefixo real e **segue os links por HTTP** — a verificação contra o disco
  não pega o 404 que o prefixo do GitHub Pages cria.

O nome do repositório é o caminho público (`/sincou-site/`), então
renomeá-lo exige atualizar `shell.BASE` e `shell.SITE` no mesmo movimento.
