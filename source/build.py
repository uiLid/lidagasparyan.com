import base64, re, io
from PIL import Image
B="/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad"
s=open(f"{B}/site2/src.html",encoding="utf-8").read()
def sub(m):
    n=m.group(1); im=Image.open(f"{B}/shots/{n}.png").convert("RGB")
    if im.width>1700: im=im.resize((1700,int(im.height*1700/im.width)),Image.LANCZOS)
    if im.height>3000 and im.width>1000: im=im.resize((1000,int(im.height*1000/im.width)),Image.LANCZOS)
    q=74 if n.startswith("cov-") else 84
    if n.startswith("cov-") and im.width>1600: im=im.resize((1600,int(im.height*1600/im.width)),Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,"WEBP",quality=q,method=6)
    return f'data-src-key="{n}" src="data:image/webp;base64,'+base64.b64encode(buf.getvalue()).decode()+'"'
out=re.sub(r'src="\{\{img:([a-z0-9-]+)\}\}"',sub,s)
assert "{{img:" not in out
open(f"{B}/site2/index.html","w",encoding="utf-8").write(out); print(len(out)//1024,"KB")
