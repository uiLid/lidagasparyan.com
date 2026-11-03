import re,os,numpy as np
from PIL import Image
B='.'; S='shots/'; O='shots_trim/'; os.makedirs(O,exist_ok=True)
src=open('site2/src.html',encoding='utf-8').read()
skip=set(re.findall(r'data-use="([^"]+)"',src))
names=sorted(set(re.findall(r'src="\{\{img:([a-z0-9-]+)\}\}"',src)))
def trim(a,tol=6):
    # a: HxWx3 int; trim rows/cols that are uniform (low std) from all sides, repeatedly
    h,w=a.shape[:2]; t,b,l,r=0,h,0,w
    def uni(x): return x.reshape(-1,3).std(axis=0).max()<tol
    ch=True
    while ch:
        ch=False
        while b-t>60 and uni(a[t:t+1,l:r]): t+=1; ch=True
        while b-t>60 and uni(a[b-1:b,l:r]): b-=1; ch=True
        while r-l>60 and uni(a[t:b,l:l+1]): l+=1; ch=True
        while r-l>60 and uni(a[t:b,r-1:r]): r-=1; ch=True
    return l,t,r,b
rep=[]
for n in names:
    p=S+n+'.png'
    if not os.path.exists(p): continue
    im=Image.open(p).convert('RGB')
    if n.startswith('cov-') or n in skip: im.save(O+n+'.png'); continue
    a=np.asarray(im).astype(np.int16)
    # work on a downsampled copy for speed
    f=max(1,im.width//700); sm=a[::f,::f]
    l,t,r,b=trim(sm); l,t,r,b=l*f,t*f,min(r*f,im.width),min(b*f,im.height)
    pad=int(24*max(1,im.width/1200))
    l,t,r,b=max(0,l-pad),max(0,t-pad),min(im.width,r+pad),min(im.height,b+pad)
    if (r-l)*(b-t)<0.9*im.width*im.height and (r-l)>=120 and (b-t)>=120:
        im=im.crop((l,t,r,b)); rep.append((n,a.shape[1],a.shape[0],r-l,b-t))
    im.save(O+n+'.png')
for x in rep: print(*x)
print(len(names),len(rep))
