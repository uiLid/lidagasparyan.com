import base64, re, io, os
EXT=os.environ.get("EXT")=="1"
from PIL import Image
B="/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad"
s=open(f"{B}/site2/src.html",encoding="utf-8").read()
def sub(m):
    n=m.group(1); im=Image.open(f"{B}/shots_trim/{n}.png").convert("RGB")
    if im.width>1700: im=im.resize((1700,int(im.height*1700/im.width)),Image.LANCZOS)
    if im.height>3000 and im.width>1000: im=im.resize((1000,int(im.height*1000/im.width)),Image.LANCZOS)
    big=re.match(r"(sky-[nd]-|abc-home|abc-cons|rg-land|fm-land|abc-mobile|abc-tablet|rg-mobile|cg-over|vg-|wp-web|fm-phones|rg-ig|sky-posts)",n)
    if big and im.width>1400: im=im.resize((1400,int(im.height*1400/im.width)),Image.LANCZOS)
    q=70 if big else 74 if n.startswith("cov-") else 84
    if n.startswith("cov-") and im.width>1600: im=im.resize((1600,int(im.height*1600/im.width)),Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,"WEBP",quality=q,method=6)
    if EXT:
        os.makedirs(f"{B}/site2/img",exist_ok=True); open(f"{B}/site2/img/{n}.webp","wb").write(buf.getvalue())
        return n,im.width,im.height,None
    return n,im.width,im.height,base64.b64encode(buf.getvalue()).decode()
def tag(m):
    g1,n,g3=m.group(1),m.group(2),m.group(3)
    n,w,h,data=sub(re.match(r"(.*)",n))
    if n.startswith("cov-"): a=g1+g3
    else: a=re.sub(r'\s(width|height)="\d+"',"",g1+g3)+f' width="{w}" height="{h}"'
    if EXT: return f'<img{a} data-src-key="{n}" src="img/{n}.webp" loading="lazy" decoding="async">'
    return f'<img{a} data-src-key="{n}" src="data:image/webp;base64,{data}">'
out=re.sub(r'<img([^>]*?)src="\{\{img:([a-z0-9-]+)\}\}"([^>]*)>',tag,s)
assert "{{img:" not in out
open(f"{B}/site2/"+("index_ext.html" if EXT else "index.html"),"w",encoding="utf-8").write(out); print(len(out)//1024,"KB")
