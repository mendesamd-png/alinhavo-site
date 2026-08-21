#!/usr/bin/env python3
"""Gera o site estatico do Sincro nos dois idiomas.

    python3 site/build.py

Escreve `index.html` e as pastas das paginas internas, em portugues na raiz
e em ingles sob `/en/`. Cada idioma tem arquivos proprios porque buscador
indexa URL, e uma pagina que so monta o texto por JavaScript chega vazia no
rastreador.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import copy_en, copy_pt, legal_en, legal_pt, pages_en, pages_pt  # noqa: E402
import shell  # noqa: E402
from shell import page  # noqa: E402

LANGS = {
    "pt": (copy_pt.T, pages_pt.P, legal_pt.L, legal_pt.UPDATED),
    "en": (copy_en.T, pages_en.P, legal_en.L, legal_en.UPDATED),
}


# --------------------------------------------------------------- helpers ---
def check_keys() -> None:
    """Uma chave que existe num idioma e falta no outro para o build.

    Sem isso a pagina sai com um buraco silencioso, que e o jeito mais facil
    de publicar meia traducao sem ninguem perceber.
    """
    for nome, a, b in (("copy", copy_pt.T, copy_en.T),
                       ("pages", pages_pt.P, pages_en.P),
                       ("legal", legal_pt.L, legal_en.L)):
        so_pt, so_en = set(a) - set(b), set(b) - set(a)
        if so_pt or so_en:
            raise SystemExit(
                f"{nome}: chaves so em pt {sorted(so_pt)}, "
                f"so em en {sorted(so_en)}")


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;")


def write(rel: str, html: str) -> None:
    out = HERE / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {rel}  ({len(html) // 1024} KB)")


def alt_of(lang: str, key: str, t_pt: dict, t_en: dict) -> str:
    """URL da mesma pagina no outro idioma."""
    if key == "home":
        return "/en/" if lang == "pt" else "/"
    if lang == "pt":
        return "/en" + t_en["url_" + key]
    return t_pt["url_" + key]


# ------------------------------------------------------------ componentes ---
def cta(t: dict, base: str, h: str, p: str, note: str = "") -> str:
    extra = f'<span class="cta-note">{note}</span>' if note else ""
    return f"""<section class="closing"><div class="wrap">
  <h2>{h}</h2>
  <p class="lede" style="margin-inline:auto">{p}</p>
  <div class="cta-row"><a class="btn" href="{base}/#preco">{t['hero_cta']}</a>{extra}</div>
</div></section>"""


def steps(items, kicker: str) -> str:
    """Passos numerados. O numero e informacao aqui: a ordem importa."""
    out = []
    for i, (h, p) in enumerate(items, 1):
        out.append(f"""<li class="step-row">
  <div class="step-num"><span>{i:02d}</span></div>
  <div class="step-txt"><h3>{h}</h3><p>{p}</p></div>
</li>""")
    return f'<ol class="steps-list" aria-label="{kicker}">' + "".join(out) + "</ol>"


def shot(src: str, alt: str, base_img: str) -> str:
    return f"""<figure class="shot glass">
  <img src="{base_img}{src}" alt="{alt}" width="1440" height="860" loading="lazy">
  <figcaption>{alt}</figcaption>
</figure>"""


def doc_page(lang: str, t: dict, L: dict, updated: str, key: str,
             url_key: str, alt_url: str) -> str:
    """Pagina de texto corrido (licenca, termos, privacidade, reembolso)."""
    base = "" if lang == "pt" else "/en"
    blocos = []
    for titulo, paras in L[f"{key}_body"]:
        corpo = "".join(f"<p>{p.format(email=t['email'])}</p>"
                        if not isinstance(p, list) else "" for p in paras)
        # listas curtas viram <ul>; o EULA usa isso na secao de restricoes
        if all(len(p) < 130 and not p.startswith("<") for p in paras) and len(paras) > 2:
            itens = "".join(f"<li>{p}</li>" for p in paras)
            corpo = f"<ul>{itens}</ul>"
        blocos.append(f"<h2>{titulo}</h2>{corpo}")

    label = {"pt": "Atualizado em", "en": "Last updated"}[lang]
    ent = legal_pt.ENTITY
    if ent["name"]:
        quem = (f"<p>{ent['name']} · {ent['id']}<br>{ent['address']}<br>"
                f"<a href=\"mailto:{ent['email']}\">{ent['email']}</a></p>")
    else:
        quem = (f"<p><a href=\"mailto:{t['email']}\">{t['email']}</a></p>")

    body = f"""<section class="doc"><div class="wrap">
  <div class="col">
    <div class="eyebrow">{t['foot_legal']}</div>
    <h1 style="font-size:clamp(2.1rem,4vw,3.2rem)">{L[f'{key}_h1']}</h1>
    <p class="lede">{L[f'{key}_lede']}</p>
    <p class="doc-meta">{label}: {updated}</p>
  </div>
  <div class="doc-body" style="margin-top:44px">
    {''.join(blocos)}
    <h2>{'Contato' if lang == 'pt' else 'Contact'}</h2>
    {quem}
  </div>
</div></section>"""
    return page(t, lang=lang, path=f"{base}{t['url_' + url_key]}",
                alt_path=alt_url, title=f"{L[f'{key}_title']} · Sincro",
                desc=L[f"{key}_desc"], body=body, extra_css=DOC_CSS)


# ------------------------------------------------------------------ CSS ----
HOME_CSS = """
.hero { padding-top: clamp(46px, 7vw, 84px); padding-bottom: 0; }
.hero h1 span {
  background: linear-gradient(100deg, var(--g1), var(--g2) 45%, var(--g3));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.cta-row { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; margin-top: 34px; }
.cta-note { font-size: .88rem; color: var(--ink-faint); }
.stage { margin-top: clamp(40px, 5vw, 66px); padding: 20px; }
.stage-head { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 14px; }
.pill {
  font-family: "IBM Plex Mono", monospace; font-size: .74rem; color: var(--ink-soft);
  border: 1px solid var(--glass-line); padding: 5px 12px; border-radius: 999px;
}
.replay {
  margin-left: auto; cursor: pointer; font: inherit; font-size: .87rem;
  color: var(--ink-soft); background: transparent;
  border: 1px solid var(--glass-line); padding: 7px 16px; border-radius: 999px;
}
.replay:hover { color: var(--ink); }
canvas#tl { display: block; width: 100%; height: 280px; border-radius: 16px; }
@media (max-width: 720px) { canvas#tl { height: 220px; } }

.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 26px; padding: 32px 30px; }
.stat .v { font-size: 2.1rem; font-weight: 600; letter-spacing: -.04em; line-height: 1; }
.stat .v.grad {
  background: linear-gradient(100deg, var(--g1), var(--g3));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.stat .k { color: var(--ink-soft); font-size: .9rem; margin-top: 8px; }

.steps { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); margin-top: 46px; }
.step { padding: 30px 28px; }
.step .dot { width: 34px; height: 34px; border-radius: 12px; margin-bottom: 18px; }
.step:nth-child(1) .dot { background: linear-gradient(140deg, var(--g1), var(--g2)); }
.step:nth-child(2) .dot { background: linear-gradient(140deg, var(--g2), var(--g4)); }
.step:nth-child(3) .dot { background: linear-gradient(140deg, var(--g3), var(--g1)); }
.step p { margin-top: 10px; color: var(--ink-soft); font-size: .97rem; }
.more { display: inline-block; margin-top: 26px; color: var(--ink); font-weight: 500; }

.migra { display: grid; gap: 20px; grid-template-columns: 1.15fr 1fr; margin-top: 46px; }
@media (max-width: 860px) { .migra { grid-template-columns: 1fr; } }
.migra .card { padding: 34px 32px; }
.migra ul { list-style: none; padding: 0; margin: 22px 0 0; display: grid; gap: 14px; }
.migra li { padding-left: 26px; position: relative; color: var(--ink-soft); font-size: .97rem; }
.migra li::before {
  content: ""; position: absolute; left: 0; top: .5em; width: 13px; height: 13px;
  border-radius: 5px; background: linear-gradient(140deg, var(--g1), var(--g3));
}

.feats { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); margin-top: 46px; }
.feat { padding: 30px 28px; }
.feat .tag {
  display: inline-block; font-family: "IBM Plex Mono", monospace; font-size: .68rem;
  letter-spacing: .12em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 14px;
}
.feat p { margin-top: 10px; color: var(--ink-soft); font-size: .96rem; }

.ingest { display: grid; gap: 20px; grid-template-columns: 1fr 1.05fr; margin-top: 46px; }
@media (max-width: 900px) { .ingest { grid-template-columns: 1fr; } }
.ingest .card { padding: 30px 28px; }
.ingest ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 20px; }
.ingest li h3 { margin-bottom: 6px; }
.ingest li p { color: var(--ink-soft); font-size: .96rem; }
.term { padding: 24px 26px; font-family: "IBM Plex Mono", monospace; font-size: .82rem; display: flex; flex-direction: column; }
.term-head { display: flex; align-items: center; gap: 10px; color: var(--ink-faint); font-size: .7rem; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 18px; }
.term-head .dots { display: flex; gap: 5px; }
.term-head .dots i { width: 9px; height: 9px; border-radius: 50%; display: block; }
.term-head .dots i:nth-child(1) { background: var(--g2); }
.term-head .dots i:nth-child(2) { background: var(--g4); }
.term-head .dots i:nth-child(3) { background: var(--g3); }
.term .path { display: block; color: var(--ink); line-height: 1.9; word-break: break-all; margin-bottom: 20px; }
.term .path b { font-weight: 500; background: linear-gradient(100deg, var(--g1), var(--g3)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.term-rows { display: grid; gap: 11px; align-content: start; flex: 1; border-top: 1px solid var(--glass-line); padding-top: 18px; }
.term-rows div { display: grid; grid-template-columns: 18px 1fr auto; gap: 12px; align-items: baseline; }
.term-rows span { color: var(--ink-soft); }
.term-rows em { font-style: normal; color: var(--ink-faint); font-size: .76rem; }
.term-rows .ok i { color: #16A34A; font-style: normal; }
.term-rows .same i { color: var(--g3); font-style: normal; }
.term-rows .warn i { color: #D97706; font-style: normal; }
.term-foot { margin-top: 18px; padding-top: 16px; border-top: 1px solid var(--glass-line); color: var(--ink-faint); font-size: .76rem; }

.exports { margin-top: 46px; display: grid; gap: 14px; }
.exp { display: grid; grid-template-columns: 210px 1fr; gap: 22px; align-items: baseline; padding: 24px 28px; }
.exp b { font-weight: 600; font-size: 1.04rem; }
.exp .fmt { display: block; font-family: "IBM Plex Mono", monospace; font-size: .74rem; color: var(--ink-faint); margin-top: 4px; }
.exp p { color: var(--ink-soft); font-size: .96rem; }
@media (max-width: 660px) { .exp { grid-template-columns: 1fr; gap: 8px; } }

.plans { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(268px, 1fr)); margin-top: 46px; }
.plan { padding: 32px 30px; display: flex; flex-direction: column; }
.plan.hi { position: relative; }
.plan.hi::before {
  content: ""; position: absolute; inset: -1px; border-radius: var(--radius); padding: 1.5px;
  background: linear-gradient(130deg, var(--g1), var(--g2), var(--g3), var(--g4));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude; pointer-events: none;
}
.plan .name { font-weight: 600; font-size: 1.06rem; }
.plan .price { font-size: 2.5rem; font-weight: 600; letter-spacing: -.045em; margin: 14px 0 2px; }
.plan .price small { font-size: .92rem; font-weight: 400; color: var(--ink-soft); letter-spacing: 0; }
.plan ul { list-style: none; padding: 0; margin: 22px 0 28px; display: grid; gap: 11px; }
.plan li { color: var(--ink-soft); font-size: .94rem; padding-left: 22px; position: relative; }
.plan li::before { content: ""; position: absolute; left: 0; top: .58em; width: 12px; height: 2px; border-radius: 2px; background: linear-gradient(90deg, var(--g1), var(--g3)); }
.plan .btn { justify-content: center; margin-top: auto; }
.intl { margin-top: 22px; color: var(--ink-faint); font-size: .92rem; }
.soon { margin-top: 24px; padding: 22px 26px; display: flex; gap: 18px; align-items: flex-start; }
.soon-mark { flex: none; width: 12px; height: 12px; border-radius: 4px; margin-top: 6px; background: linear-gradient(140deg, var(--g4), var(--g2)); }
.soon b { font-weight: 600; }
.soon p { color: var(--ink-soft); font-size: .95rem; margin-top: 4px; }

.faq { margin-top: 42px; }
details { border-bottom: 1px solid var(--glass-line); }
details:first-child { border-top: 1px solid var(--glass-line); }
summary { cursor: pointer; list-style: none; padding: 22px 0; font-weight: 500; font-size: 1.05rem; letter-spacing: -.015em; display: flex; align-items: center; gap: 16px; }
summary::-webkit-details-marker { display: none; }
summary::after { content: "+"; margin-left: auto; color: var(--ink-faint); font-family: "IBM Plex Mono", monospace; font-size: 1.2rem; }
details[open] summary::after { content: "\\2013"; }
details p { padding-bottom: 24px; color: var(--ink-soft); max-width: var(--measure); }

.closing { text-align: center; padding: clamp(70px, 9vw, 120px) 0; }
.closing .cta-row { justify-content: center; }
"""

DOC_CSS = """
.doc { padding-bottom: clamp(60px, 8vw, 110px); }
"""

HOWTO_CSS = HOME_CSS + """
.toc { margin-top: 40px; padding: 24px 28px; }
.toc h4 { margin: 0 0 14px; font-size: .72rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-faint); }
.toc ol { margin: 0; padding-left: 20px; display: grid; gap: 8px; }
.toc a { color: var(--ink-soft); text-decoration: none; }
.toc a:hover { color: var(--ink); }

.part-kicker {
  display: inline-block; font-family: "IBM Plex Mono", monospace; font-size: .72rem;
  letter-spacing: .14em; text-transform: uppercase; color: #fff; margin-bottom: 16px;
  padding: 5px 13px; border-radius: 999px;
  background: linear-gradient(110deg, var(--g1), var(--g2));
}
.steps-list { list-style: none; margin: 44px 0 0; padding: 0; display: grid; gap: 4px; }
.step-row { display: grid; grid-template-columns: 74px 1fr; gap: 22px; padding: 24px 0; border-top: 1px solid var(--glass-line); }
.step-row:last-child { border-bottom: 1px solid var(--glass-line); }
.step-num span {
  font-family: "IBM Plex Mono", monospace; font-size: 1.5rem; font-weight: 500;
  background: linear-gradient(140deg, var(--g1), var(--g3));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.step-txt p { margin-top: 8px; color: var(--ink-soft); font-size: .98rem; max-width: 62ch; }
@media (max-width: 620px) { .step-row { grid-template-columns: 1fr; gap: 6px; } }

.shot { margin: 40px 0 0; padding: 14px; }
.shot img { display: block; width: 100%; height: auto; border-radius: 14px; }
.shot figcaption { margin-top: 14px; padding: 0 8px 4px; color: var(--ink-faint); font-size: .86rem; }

.tip { margin-top: 34px; padding: 24px 28px; border-left: 3px solid var(--g1); border-radius: 0 20px 20px 0; }
.tip h3 { margin-bottom: 8px; }
.tip p { color: var(--ink-soft); font-size: .96rem; }

.legend { display: grid; gap: 16px; margin-top: 34px; }
.legend div { display: grid; grid-template-columns: 130px 1fr; gap: 20px; padding: 18px 24px; align-items: baseline; }
.legend b { font-weight: 600; }
.legend p { color: var(--ink-soft); font-size: .95rem; }
@media (max-width: 640px) { .legend div { grid-template-columns: 1fr; gap: 6px; } }
.legend .sw { display: inline-block; width: 13px; height: 13px; border-radius: 4px; margin-right: 9px; vertical-align: -1px; }

.grid2 { display: grid; gap: 18px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); margin-top: 34px; }
.grid2 > div { padding: 26px 28px; }
.grid2 p { margin-top: 8px; color: var(--ink-soft); font-size: .95rem; }

.rel { margin-top: 44px; padding: 32px 34px; }
.rel-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 14px; }
.rel-v {
  font-family: "IBM Plex Mono", monospace; font-size: 1.05rem; font-weight: 500;
  color: #fff; padding: 4px 14px; border-radius: 999px;
  background: linear-gradient(110deg, var(--g1), var(--g2));
}
.rel-date { color: var(--ink-faint); font-size: .84rem; font-family: "IBM Plex Mono", monospace; }
.rel h3 { margin-top: 18px; }
.rel ul { list-style: none; margin: 20px 0 0; padding: 0; display: grid; gap: 13px; }
.rel li { padding-left: 26px; position: relative; color: var(--ink-soft); font-size: .96rem; }
.rel li::before { content: ""; position: absolute; left: 0; top: .55em; width: 13px; height: 13px; border-radius: 5px; background: linear-gradient(140deg, var(--g1), var(--g3)); }
.next li::before { background: linear-gradient(140deg, var(--g4), var(--g2)); }
"""

TL_JS = r"""
(function () {
  var cv = document.getElementById("tl");
  if (!cv) return;
  var ctx = cv.getContext("2d");
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var seed = 20260819;
  function rnd() { return (seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296; }
  var G = ["#8B5CF6", "#F472B6", "#38BDF8", "#FDE047"];
  var SRC = [
    { label: "V2", g: 0, clips: [[.02,.17],[.23,.16],[.44,.19],[.68,.13],[.85,.12]] },
    { label: "V1", g: 2, clips: [[.00,.19],[.24,.14],[.42,.21],[.70,.15],[.88,.10]] },
    { label: "A1", g: 1, clips: [[.05,.22],[.30,.18],[.55,.17],[.78,.16]] },
    { label: "A2", g: 3, clips: [[.03,.24],[.31,.16],[.54,.20],[.79,.14]] }
  ];
  var DRIFT = [.085, -.055, .13, -.10];
  var waves = SRC.map(function (s) {
    return s.clips.map(function () {
      var a = []; for (var i = 0; i < 90; i++) a.push(.25 + rnd() * .75); return a;
    });
  });
  var t = 0, raf = null, start = null, DUR = 1600, HOLD = 700;
  function css(n) { return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); }
  function size() {
    var dpr = Math.min(devicePixelRatio || 1, 2);
    cv.width = cv.clientWidth * dpr; cv.height = cv.clientHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); draw();
  }
  function draw() {
    var w = cv.clientWidth, h = cv.clientHeight;
    var pad = 36, rowH = (h - 28) / SRC.length, barH = Math.min(38, rowH - 10);
    var faint = css("--ink-faint"), line = css("--glass-line");
    ctx.clearRect(0, 0, w, h);
    ctx.font = '11px "IBM Plex Mono", monospace';
    for (var i = 0; i <= 6; i++) {
      var x = Math.round(pad + (w - pad - 10) * i / 6) + .5;
      ctx.strokeStyle = line; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(x, 18); ctx.lineTo(x, h); ctx.stroke();
      if (i < 6) {
        ctx.fillStyle = faint;
        var min = i * 76;
        var hh = String(Math.floor(min / 60)); while (hh.length < 2) hh = "0" + hh;
        var mm = String(min % 60); while (mm.length < 2) mm = "0" + mm;
        ctx.fillText(hh + ":" + mm + ":00:00", x + 7, 12);
      }
    }
    SRC.forEach(function (src, r) {
      var y = 28 + r * rowH + (rowH - barH) / 2;
      ctx.save(); ctx.beginPath(); ctx.rect(pad - 6, 0, w, h); ctx.clip();
      src.clips.forEach(function (c, i) {
        var drift = DRIFT[r] * (1 - t);
        var x = pad + (c[0] + drift) * (w - pad - 10);
        var bw = Math.max(12, c[1] * (w - pad - 10));
        var orfao = (r === 3 && i === 3);
        var g = ctx.createLinearGradient(x, y, x + bw, y + barH);
        if (orfao && t > .5) { g.addColorStop(0, "#FDE047"); g.addColorStop(1, "#FB923C"); }
        else { g.addColorStop(0, G[src.g]); g.addColorStop(1, G[(src.g + 2) % 4]); }
        ctx.fillStyle = g; ctx.globalAlpha = .92;
        var rr = 9;
        ctx.beginPath(); ctx.moveTo(x + rr, y);
        ctx.arcTo(x + bw, y, x + bw, y + barH, rr);
        ctx.arcTo(x + bw, y + barH, x, y + barH, rr);
        ctx.arcTo(x, y + barH, x, y, rr);
        ctx.arcTo(x, y, x + bw, y, rr);
        ctx.closePath(); ctx.fill();
        ctx.save(); ctx.clip();
        ctx.fillStyle = "rgba(255,255,255,.55)";
        var wv = waves[r][i], step = Math.max(2, bw / 44);
        for (var k = 0, px = x + 4; px < x + bw - 4; k++, px += step) {
          var a = wv[k % wv.length] * (barH / 2 - 5);
          ctx.fillRect(px, y + barH / 2 - a, Math.max(1, step - 1.5), a * 2);
        }
        ctx.restore(); ctx.globalAlpha = 1;
      });
      ctx.restore();
      ctx.fillStyle = faint;
      ctx.font = '500 10px "IBM Plex Mono", monospace';
      ctx.fillText(src.label, 4, y + barH / 2 + 3);
    });
    var px = Math.round(pad + (cv.clientWidth - pad - 10) * .02) + .5;
    ctx.strokeStyle = "#FF4D6D"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(px, 18); ctx.lineTo(px, cv.clientHeight); ctx.stroke();
  }
  function frame(now) {
    if (start === null) start = now;
    var e = now - start;
    if (e < HOLD) t = 0;
    else {
      var p = Math.min(1, (e - HOLD) / DUR);
      t = p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
    }
    draw();
    if (e < HOLD + DUR) raf = requestAnimationFrame(frame);
  }
  function play() {
    if (reduced) { t = 1; draw(); return; }
    cancelAnimationFrame(raf); start = null; t = 0;
    raf = requestAnimationFrame(frame);
  }
  addEventListener("resize", size);
  document.addEventListener("sincro:theme", draw);
  var rb = document.getElementById("replay");
  if (rb) rb.addEventListener("click", play);
  size();
  if (reduced) { t = 1; draw(); }
  else new IntersectionObserver(function (es, o) {
    if (es[0].isIntersecting) { play(); o.disconnect(); }
  }, { threshold: .3 }).observe(cv);
})();
"""


# ------------------------------------------------------------- as paginas ---
def build_home(lang: str) -> str:
    t, P, L, _ = LANGS[lang]
    base = "" if lang == "pt" else "/en"
    alt = alt_of(lang, "home", copy_pt.T, copy_en.T)

    stats = "".join(
        f'<div class="stat"><div class="v{" grad" if i < 2 else ""} mono">'
        f'{t[f"stat{i+1}_v"]}</div><div class="k">{t[f"stat{i+1}_k"]}</div></div>'
        for i in range(4))

    flow = "".join(
        f'<div class="step glass"><div class="dot"></div>'
        f'<h3>{t[f"flow{i}_h"]}</h3><p>{t[f"flow{i}_p"]}</p></div>'
        for i in (1, 2, 3))

    feats = "".join(
        f'<div class="feat glass"><span class="tag">{tag}</span>'
        f'<h3>{h}</h3><p>{p}</p></div>' for tag, h, p in t["feats"])

    ing = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in t["ing_items"])
    log_ok = "".join(
        f'<div class="ok"><i>&#10003;</i><span>{n}</span>'
        f'<em>{t["ing_copied"]}</em></div>'
        for n in ("C0041.MP4", "C0042.MP4"))
    log_ok2 = "".join(
        f'<div class="ok"><i>&#10003;</i><span>{n}</span>'
        f'<em>{t["ing_copied"]}</em></div>'
        for n in ("ZOOM0007.WAV", "ZOOM0008.WAV", "C0044.MP4", "C0045.MP4"))

    exports = "".join(
        f'<div class="exp glass"><div><b>{n}</b><span class="fmt">{f}</span></div>'
        f'<p>{p}</p></div>' for n, f, p in t["exports"])

    def plan(i, hi=False):
        itens = "".join(f"<li>{x}</li>" for x in t[f"plan{i}_items"])
        cls = "plan glass hi" if hi else "plan glass"
        btn = "btn" if hi else "btn quiet"
        return f"""<div class="{cls}">
  <span class="name">{t[f'plan{i}_name']}</span>
  <div class="price">{t[f'plan{i}_price']} <small>{t[f'plan{i}_unit']}</small></div>
  <ul>{itens}</ul>
  <a class="{btn}" href="#">{t[f'plan{i}_cta']}</a>
</div>"""

    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>"
                  for q, a in t["faq"])

    pe_same = "".join(f"<li>{x}</li>" for x in t["pe_same"])
    pe_new = "".join(f"<li>{x}</li>" for x in t["pe_new"])

    body = f"""<section class="hero"><div class="wrap">
  <div class="col">
    <h1>{t['hero_h1_a']}<br><span>{t['hero_h1_b']}</span></h1>
    <p class="lede">{t['hero_lede']}</p>
    <div class="cta-row">
      <a class="btn" href="#preco">{t['hero_cta']}</a>
      <a class="btn quiet" href="{base}{t['url_howto']}">{t['hero_cta2']}</a>
      <span class="cta-note">{t['hero_note']}</span>
    </div>
  </div>
  <div class="stage glass">
    <div class="stage-head">
      <span class="pill">{t['stage_clips']}</span>
      <span class="pill">{t['stage_srcs']}</span>
      <span class="pill mono">{t['stage_dur']}</span>
      <button class="replay" id="replay" type="button">{t['stage_replay']}</button>
    </div>
    <canvas id="tl" aria-label="{t['stage_alt']}"></canvas>
  </div>
</div></section>

<section><div class="wrap"><div class="stats glass">{stats}</div></div></section>

<section id="fluxo"><div class="wrap">
  <div class="eyebrow">{t['flow_eyebrow']}</div>
  <div class="col"><h2>{t['flow_h2']}</h2><p class="lede">{t['flow_lede']}</p></div>
  <div class="steps">{flow}</div>
  <a class="more" href="{base}{t['url_howto']}">{t['flow_more']} &rarr;</a>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">{t['pe_eyebrow']}</div>
  <div class="col"><h2>{t['pe_h2']}</h2><p class="lede">{t['pe_lede']}</p></div>
  <div class="migra">
    <div class="card glass"><h3>{t['pe_same_h']}</h3><ul>{pe_same}</ul></div>
    <div class="card glass"><h3>{t['pe_new_h']}</h3><ul>{pe_new}</ul></div>
  </div>
  <a class="more" href="{base}{t['url_pluraleyes']}">{t['pe_more']} &rarr;</a>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">{t['feat_eyebrow']}</div>
  <div class="col"><h2>{t['feat_h2']}</h2><p class="lede">{t['feat_lede']}</p></div>
  <div class="feats">{feats}</div>
</div></section>

<section id="ingest"><div class="wrap">
  <div class="eyebrow">{t['ing_eyebrow']}</div>
  <div class="col"><h2>{t['ing_h2']}</h2><p class="lede">{t['ing_lede']}</p></div>
  <div class="ingest">
    <div class="card glass"><ul>{ing}</ul></div>
    <div class="term glass">
      <div class="term-head"><span class="dots"><i></i><i></i><i></i></span>{t['ing_log']}</div>
      <code class="path">/Volumes/DG&nbsp;REALTIME/<b>2026_08_21_JADE_PICON</b>/<b>CAM_A</b>/C0043.MP4</code>
      <div class="term-rows">
        {log_ok}
        <div class="same"><i>=</i><span>C0043.MP4</span><em>{t['ing_there']}</em></div>
        {log_ok2}
        <div class="warn"><i>&#9888;</i><span>C0046.MP4</span><em>{t['ing_nospace']}</em></div>
      </div>
      <div class="term-foot">{t['ing_foot']}</div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">{t['exp_eyebrow']}</div>
  <div class="col"><h2>{t['exp_h2']}</h2></div>
  <div class="exports">{exports}</div>
</div></section>

<section id="preco"><div class="wrap">
  <div class="eyebrow">{t['price_eyebrow']}</div>
  <div class="col"><h2>{t['price_h2']}</h2><p class="lede">{t['price_lede']}</p></div>
  <div class="plans">{plan(1)}{plan(2, hi=True)}{plan(3)}</div>
  <p class="intl">{t['price_intl']}</p>
  <div class="soon glass">
    <span class="soon-mark"></span>
    <div><b>{t['soon_h']}</b><p>{t['soon_p']}</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="eyebrow">{t['faq_eyebrow']}</div>
  <div class="col"><h2>{t['faq_h2']}</h2></div>
  <div class="faq col">{faq}</div>
</div></section>

{cta(t, base, t['close_h2'], t['close_lede'], t['close_note'])}"""

    return page(t, lang=lang, path=f"{base}/", alt_path=alt,
                title=f"Sincro · {t['home_title'] if lang == 'pt' else 'sync by sound'}"
                      if False else ("Sincro · sincroniza a diaria pelo som"
                                     if lang == "pt"
                                     else "Sincro · sync your shoot day by sound"),
                desc=t["home_desc"], body=body, here="home",
                extra_css=HOME_CSS, extra_js=TL_JS)


def build_howto(lang: str) -> str:
    t, P, L, _ = LANGS[lang]
    base = "" if lang == "pt" else "/en"
    img = "/img/"   # as imagens moram so na raiz, servem os dois idiomas
    alt = alt_of(lang, "howto", copy_pt.T, copy_en.T)

    colors = "".join(
        f'<div class="glass"><b>{h}</b><p>{p}</p></div>'
        for h, p in P["howto_colors"])
    numbers = "".join(
        f'<div class="glass"><b class="mono">{h}</b><p>{p}</p></div>'
        for h, p in P["howto_numbers"])
    out = "".join(f'<div class="glass"><h3>{h}</h3><p>{p}</p></div>'
                  for h, p in P["howto_out"])
    exp = "".join(f'<div class="glass"><h3>{h}</h3><p>{p}</p></div>'
                  for h, p in P["howto_export"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>"
                  for q, a in P["howto_faq"])

    toc_items = [(P["howto_part1_h2"], "#ingest"),
                 (P["howto_part2_h2"], "#sync"),
                 (P["howto_read_h2"], "#ler"),
                 (P["howto_out_h2"], "#fora"),
                 (P["howto_export_h2"], "#exportar")]
    toc = "".join(f'<li><a href="{u}">{h}</a></li>' for h, u in toc_items)

    body = f"""<section class="doc"><div class="wrap">
  <div class="col">
    <div class="eyebrow">{P['howto_eyebrow']}</div>
    <h1>{P['howto_h1']}</h1>
    <p class="lede">{P['howto_lede']}</p>
  </div>
  <div class="toc glass col"><h4>{P['howto_toc']}</h4><ol>{toc}</ol></div>
</div></section>

<section id="ingest"><div class="wrap">
  <span class="part-kicker">{P['howto_part1_kicker']}</span>
  <div class="col"><h2>{P['howto_part1_h2']}</h2>
    <p class="lede">{P['howto_part1_lede']}</p></div>
  {steps(P['howto_ing_steps'], P['howto_part1_h2'])}
  {shot(f'app-ingest-{lang}.png', P['howto_ing_shot'], img)}
  <div class="tip glass">
    <h3>{P['howto_ing_tip_h']}</h3><p>{P['howto_ing_tip_p']}</p>
  </div>
</div></section>

<section id="sync"><div class="wrap">
  <span class="part-kicker">{P['howto_part2_kicker']}</span>
  <div class="col"><h2>{P['howto_part2_h2']}</h2>
    <p class="lede">{P['howto_part2_lede']}</p></div>
  {shot(f'app-prescan-{lang}.png', P['howto_sync_shot1'], img)}
  {steps(P['howto_sync_steps'], P['howto_part2_h2'])}
  {shot(f'app-synced-{lang}.png', P['howto_sync_shot2'], img)}
</div></section>

<section id="ler"><div class="wrap">
  <div class="col"><h2>{P['howto_read_h2']}</h2>
    <p class="lede">{P['howto_read_lede']}</p></div>
  <h3 style="margin-top:40px">{P['howto_colors_h']}</h3>
  <div class="legend">{colors}</div>
  <h3 style="margin-top:44px">{P['howto_numbers_h']}</h3>
  <div class="legend">{numbers}</div>
  <div class="tip glass">
    <h3>{P['howto_thresholds_h']}</h3><p>{P['howto_thresholds_p']}</p>
  </div>
</div></section>

<section id="fora"><div class="wrap">
  <div class="col"><h2>{P['howto_out_h2']}</h2>
    <p class="lede">{P['howto_out_lede']}</p></div>
  <div class="grid2">{out}</div>
</div></section>

<section id="exportar"><div class="wrap">
  <div class="col"><h2>{P['howto_export_h2']}</h2></div>
  <div class="grid2">{exp}</div>
</div></section>

<section><div class="wrap">
  <div class="col"><h2>{P['howto_faq_h2']}</h2></div>
  <div class="faq col">{faq}</div>
</div></section>

{cta(t, base, P['howto_cta_h'], P['howto_cta_p'])}"""

    return page(t, lang=lang, path=f"{base}{t['url_howto']}", alt_path=alt,
                title=f"{P['howto_title']} · Sincro", desc=P["howto_desc"],
                body=body, here="howto", extra_css=HOWTO_CSS)


def build_pluraleyes(lang: str) -> str:
    t, P, L, _ = LANGS[lang]
    base = "" if lang == "pt" else "/en"
    alt = alt_of(lang, "pluraleyes", copy_pt.T, copy_en.T)

    why = "".join(f'<div class="glass"><h3>{h}</h3><p>{p}</p></div>'
                  for h, p in P["pe_why"])
    diff = "".join(f'<div class="glass"><h3>{h}</h3><p>{p}</p></div>'
                   for h, p in P["pe_diff"])
    move = steps([(h, p) for h, p in P["pe_move"]], P["pe_move_h2"])

    body = f"""<section class="doc"><div class="wrap">
  <div class="col">
    <div class="eyebrow">{P['pe_page_eyebrow']}</div>
    <h1>{P['pe_page_h1']}</h1>
    <p class="lede">{P['pe_page_lede']}</p>
    <div class="cta-row">
      <a class="btn" href="{base}/#preco">{t['hero_cta']}</a>
      <a class="btn quiet" href="{base}{t['url_howto']}">{t['hero_cta2']}</a>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="col"><h2>{P['pe_why_h2']}</h2></div>
  <div class="grid2">{why}</div>
</div></section>

<section><div class="wrap">
  <div class="col"><h2>{P['pe_diff_h2']}</h2></div>
  <div class="grid2">{diff}</div>
</div></section>

<section><div class="wrap">
  <div class="col"><h2>{P['pe_move_h2']}</h2></div>
  {move}
</div></section>

{cta(t, base, P['pe_page_cta_h'], P['pe_page_cta_p'])}"""

    return page(t, lang=lang, path=f"{base}{t['url_pluraleyes']}", alt_path=alt,
                title=f"{P['pe_title']} · Sincro", desc=P["pe_desc"],
                body=body, here="pluraleyes", extra_css=HOWTO_CSS)


def build_whatsnew(lang: str) -> str:
    t, P, L, _ = LANGS[lang]
    base = "" if lang == "pt" else "/en"
    alt = alt_of(lang, "whatsnew", copy_pt.T, copy_en.T)

    rel = ""
    for v, date, title, items in P["wn_releases"]:
        li = "".join(f"<li>{x}</li>" for x in items)
        rel += f"""<div class="rel glass">
  <div class="rel-head"><span class="rel-v">{v}</span>
    <span class="rel-date">{date}</span></div>
  <h3>{title}</h3><ul>{li}</ul>
</div>"""
    nxt = "".join(f"<li>{x}</li>" for x in P["wn_next"])

    body = f"""<section class="doc"><div class="wrap">
  <div class="col">
    <div class="eyebrow">{P['wn_eyebrow']}</div>
    <h1>{P['wn_h1']}</h1>
    <p class="lede">{P['wn_lede']}</p>
  </div>
  {rel}
  <div class="rel glass next" style="margin-top:20px">
    <h3>{P['wn_next_h']}</h3><ul>{nxt}</ul>
    <p class="doc-meta">{P['wn_note']}</p>
  </div>
</div></section>

{cta(t, base, t['close_h2'], t['close_lede'], t['close_note'])}"""

    return page(t, lang=lang, path=f"{base}{t['url_whatsnew']}", alt_path=alt,
                title=f"{P['wn_title']} · Sincro", desc=P["wn_desc"],
                body=body, here="whatsnew", extra_css=HOWTO_CSS)


def sitemap() -> str:
    urls = []
    for lang in ("pt", "en"):
        t = LANGS[lang][0]
        base = "" if lang == "pt" else "/en"
        urls.append(f"{base}/")
        for k in ("howto", "pluraleyes", "whatsnew", "eula", "terms",
                  "privacy", "refunds"):
            urls.append(f"{base}{t['url_' + k]}")
    itens = "".join(f"  <url><loc>{shell.SITE}{u}</loc></url>\n" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{itens}</urlset>\n")


def main() -> None:
    check_keys()
    print("gerando o site:")
    for lang in ("pt", "en"):
        t, P, L, updated = LANGS[lang]
        d = "" if lang == "pt" else "en/"
        write(f"{d}index.html", build_home(lang))
        write(f"{d}{t['url_howto'].strip('/')}/index.html", build_howto(lang))
        write(f"{d}{t['url_pluraleyes'].strip('/')}/index.html", build_pluraleyes(lang))
        write(f"{d}{t['url_whatsnew'].strip('/')}/index.html", build_whatsnew(lang))
        for key, url_key in (("eula", "eula"), ("terms", "terms"),
                             ("privacy", "privacy"), ("refunds", "refunds")):
            alt = alt_of(lang, url_key, copy_pt.T, copy_en.T)
            write(f"{d}{t['url_' + url_key].strip('/')}/index.html",
                  doc_page(lang, t, L, updated, key, url_key, alt))
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {shell.SITE}/sitemap.xml\n")
    # as imagens do ingles apontam para /img/, que so existe na raiz
    print("pronto.")


if __name__ == "__main__":
    main()
