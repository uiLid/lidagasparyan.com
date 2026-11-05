import re, os, json, shutil, datetime
from bs4 import BeautifulSoup
B="/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2"
OUT=f"{B}/pub"; SITE="https://lidagasparyan.com"
src=open(f"{B}/index_ext.html",encoding="utf-8").read().replace('src="img/','src="/img/')
soup=BeautifulSoup(src,"html.parser")
pages={}
for e in soup.select("[data-route]"):
    h=e.find("h1"); p=e.select_one(".lead") or e.find("p")
    pages[e["data-route"]]=(h.get_text(" ",strip=True) if h else e["data-route"], re.sub(r"\s+"," ",p.get_text(" ",strip=True)) if p else "")
def trim(t,n=155):
    t=t.replace("‑","-")
    if len(t)<=n: return t
    return t[:n].rsplit(" ",1)[0].rstrip(",;:.")+"."
HOME_T="Lida Gasparyan | Senior Product and UI/UX Designer, Remote (Yerevan)"
HOME_D="Senior product designer with 9+ years across hosting, e-commerce and AI tools, and a former Product Director. Open to full-time remote or in-house roles."
def meta_for(r):
    h,l=pages[r]
    if r=="home": return HOME_T,HOME_D
    if r=="work": return "Work: product, UI/UX and brand design case studies | Lida Gasparyan",trim(l)
    if r=="about": return "About Lida Gasparyan, senior product designer in Yerevan",trim(l)
    if r=="contact": return "Contact Lida Gasparyan, remote product designer",trim(l)
    if r=="book": return "Book a call with Lida Gasparyan",trim(l)
    if r=="leadership": return "Leadership: teams at a startup summit and a café | Lida Gasparyan",trim(l)
    if r=="design-system": return "Design system (atomic design, v1) | Lida Gasparyan",trim(l)
    return f"{h} | Case study by Lida Gasparyan, product designer",trim(l)
PERSON={"@type":"Person","@id":SITE+"/#lida","name":"Lida Gasparyan","jobTitle":"Senior Product Designer (UI/UX)","url":SITE+"/","image":SITE+"/og.png",
 "address":{"@type":"PostalAddress","addressLocality":"Yerevan","addressCountry":"AM"},
 "sameAs":["https://www.linkedin.com/in/lidagasparyan","https://www.behance.net/gasparyanlida"],
 "knowsAbout":["Product design","UI/UX design","Design systems","Dashboards","Web design","Branding","AI product design"],
 "knowsLanguage":["en","ru","hy"]}
def head(r):
    t,d=meta_for(r); url=SITE+("/" if r=="home" else f"/{r}/")
    ld=[{"@context":"https://schema.org",**PERSON}]
    if r=="home": ld.append({"@context":"https://schema.org","@type":"WebSite","name":"Lida Gasparyan, product designer","url":SITE+"/","inLanguage":["en","ru"],"author":{"@id":SITE+"/#lida"}})
    else: ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":pages[r][0],"item":url}]})
    esc=lambda x:x.replace("&","&amp;").replace('"',"&quot;")
    return (f'<!doctype html><html lang="en" data-initial="{r}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>{esc(t)}</title><meta name="description" content="{esc(d)}"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large">'
      f'<meta name="author" content="Lida Gasparyan"><meta property="og:type" content="{"website" if r=="home" else "article"}"><meta property="og:site_name" content="Lida Gasparyan"><meta property="og:title" content="{esc(t)}"><meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
      f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(t)}"><meta name="twitter:description" content="{esc(d)}"><meta name="twitter:image" content="{SITE}/og.png">'
      f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>'
      '<script>(function(){var r=document.documentElement.getAttribute("data-initial");if(r&&r!=="home"&&!location.hash)history.replaceState(null,"",location.pathname+"#"+r)})()</script>')
body=re.sub(r"<title>.*?</title>","",src,count=1,flags=re.S)
cases=[r for r in pages if r.startswith(("case-","lead-"))]
nav=('<nav class="all-links" aria-label="All case studies"><h2>All case studies</h2><ul>'+"".join(f'<li><a href="/{r}/">{pages[r][0]}</a></li>' for r in cases)+'</ul></nav>'
     '<style>.all-links{max-width:1120px;margin:48px auto 0;padding:24px 16px 0;border-top:1px solid var(--line,#ddd);font-size:.9rem}.all-links h2{font-size:.9rem;margin:0 0 12px}.all-links ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:6px 24px}.all-links a{color:var(--muted,#555)}</style>')
assert "</footer>" in body
body=body.replace("</footer>","</footer>"+nav,1)
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT)
shutil.copytree(f"{B}/img",f"{OUT}/img"); shutil.copy(f"{B}/og.png",f"{OUT}/og.png")
for r in pages:
    d=OUT if r=="home" else f"{OUT}/{r}"; os.makedirs(d,exist_ok=True)
    open(f"{d}/index.html","w",encoding="utf-8").write(head(r)+body+"</body></html>")
today=datetime.date.today().isoformat()
open(f"{OUT}/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'<url><loc>{SITE}{"/" if r=="home" else "/"+r+"/"}</loc><lastmod>{today}</lastmod><priority>{"1.0" if r=="home" else "0.7"}</priority></url>\n' for r in pages)+"</urlset>\n")
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print(len(pages),"pages")
