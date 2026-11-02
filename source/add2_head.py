import re, html, json
B = "/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2"
src = open(f"{B}/src.html", encoding="utf-8").read()
RUN = {}
def T(en, ru):
    RUN[re.sub(r"\s+", " ", en).strip()] = ru
    return html.escape(en, quote=False)
def A(en, ru):  # attribute
    RUN[re.sub(r"\s+", " ", en).strip()] = ru
    return html.escape(en, quote=True)

def fig(img, w, h, alt, t, d, cls="shot", alt_ru=None):
    return (f'    <figure class="fig"><div class="{cls}"><img src="{{{{img:{img}}}}}" width="{w}" height="{h}" alt="{A(alt, alt_ru or alt)}"></div>'
            f'<figcaption><h3>{T(*t)}</h3><p>{T(*d)}</p></figcaption></figure>')

def sec(h, paras=(), steps=(), bullets=()):
    o = f'  <section class="sec"><h2>{T(*h)}</h2>'
    for p in paras: o += f'<p>{T(*p)}</p>'
    if steps:
        o += '<ol class="steps">' + ''.join(f'<li><b style="color:var(--fg)">{T(*a)}</b> {T(*b)}</li>' for a, b in steps) + '</ol>'
    if bullets:
        o += '<ul class="also">' + ''.join(f'<li><b style="color:var(--fg)">{T(*a)}</b> {T(*b)}</li>' for a, b in bullets) + '</ul>'
    return o + '</section>'

def case(route, title, label, lead, meta, glance, sections, figs, note, prev, nxt, aria=None):
    o = f'<div data-route="{route}" class="page" tabindex="-1" aria-label="{A(*(aria or title))}">\n'
    o += f'  <nav class="crumbs" aria-label="Breadcrumb"><a href="#home">Home</a><span aria-hidden="true">/</span><a href="#work">Work</a><span aria-hidden="true">/</span><span aria-current="page">{T(*title)}</span></nav>\n'
    o += f'  <header class="case-hero">\n    <p class="label">{T(*label)}</p>\n    <h1>{T(*title)}</h1>\n    <p class="lead">{T(*lead)}</p>\n    <dl class="meta-row">\n'
    for k, v in meta: o += f'      <div class="meta"><dt>{T(*k)}</dt><dd>{T(*v)}</dd></div>\n'
    o += '    </dl>\n  </header>\n'
    if glance:
        o += '  <div class="glance">\n' + ''.join(f'    <div class="gl"><span class="k">{T(*k)}</span><p>{T(*v)}</p></div>\n' for k, v in glance) + '  </div>\n'
    for s in sections: o += s + '\n'
    o += '  <div class="shots">\n' + '\n'.join(figs) + '\n  </div>\n'
    if note: o += f'  <p class="note" style="margin-top:32px">{T(*note)}</p>\n'
    o += (f'  <nav class="pager" aria-label="More case studies" style="margin-top:64px"><a class="prev" href="#{prev[0]}"><span class="mono">{T("Previous","Назад")}</span><span class="t">{T(*prev[1])}</span></a>'
          f'<a class="next" href="#{nxt[0]}"><span class="mono">{T(*nxt[2]) if len(nxt)>2 else T("Next","Далее")}</span><span class="t">{T(*nxt[1])}</span></a></nav>\n</div>\n')
    return o

def card(route, kind, key, w, h, title, desc, tags):
    t = ''.join(f'<span class="tag{" accent" if i == 0 else ""}">{T(*x)}</span>' for i, x in enumerate(tags))
    return (f'    <a class="card" data-kind="{kind}" href="#{route}"><div class="thumb"><img data-use="{key}" alt="" width="{w}" height="{h}"></div>'
            f'<div><h3>{T(*title)}</h3><p>{T(*desc)}</p></div><div class="tags">{t}</div></a>')

GR = ("Graphic design", "Графический дизайн"); PR = ("Product design", "Продуктовый дизайн"); WB = ("Web design", "Веб-дизайн")
LBL = lambda k: (k[0] + " · Case study", k[1] + " · Кейс")
CL = ("Client", "Клиент"); DI = ("Discipline", "Направление"); SC = ("Scope", "Объём работ"); TL = ("Tools", "Инструменты")
LG = ("Languages", "Языки")
NOTE_CLIENT = ("Client work shown as part of a portfolio.", "Работа для клиента показана в рамках портфолио.")

