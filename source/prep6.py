from PIL import Image
import os
S='shots/'
def op(n): return Image.open(S+n+'.png').convert('RGB')
def chunks(src,prefix,n):
    im=op(src); h=im.height; step=-(-h//n)
    for i in range(n):
        im.crop((0,i*step,im.width,min(h,(i+1)*step))).save(f'{S}{prefix}-{i+1}.png')
    print(prefix,n,im.size)
chunks('fm-landing','fm-land',2)
chunks('sky-night','sky-n',4); chunks('sky-day','sky-d',4)
chunks('abc-home','abc-home',2); chunks('abc-constructor','abc-cons',2)
chunks('rg-landing-full','rg-land',3)
def rr(im,r=28):
    from PIL import ImageDraw
    im=im.convert('RGBA'); m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,im.width-1,im.height-1),r,fill=255); im.putalpha(m); return im
def strip(ims,bg,gap=50,pad=60,name=''):
    W=sum(i.width for i in ims)+gap*(len(ims)-1)+2*pad; H=max(i.height for i in ims)+2*pad
    c=Image.new('RGB',(W,H),bg).convert('RGBA'); x=pad
    for i in ims: c.alpha_composite(i,(x,pad+(H-2*pad-i.height)//2)); x+=i.width+gap
    c.convert('RGB').save(S+name+'.png'); print(name,c.size)
# fermalytics phones
ph=[rr(op(n).resize((450,800),Image.LANCZOS),40) for n in ['fm-app-main','fm-app-chart','fm-app-inv','fm-app-ph']]
strip(ph,'#e8f0ff',name='fm-phones')
# abc mobile 3 columns
m=op('abc-mobile'); h=m.height; st=-(-h//3)
cols=[rr(m.crop((0,i*st,375,min(h,(i+1)*st))),24) for i in range(3)]
strip(cols,'#eef2ff',name='abc-mobile-strip')
t=op('abc-tablet'); h=t.height; st=-(-h//2)
strip([rr(t.crop((0,i*st,834,min(h,(i+1)*st))),24) for i in range(2)],'#eef2ff',name='abc-tablet-strip')
# regardify mobile
strip([rr(op(n),24) for n in ['rg-m-blog','rg-m-events','rg-m-team']],'#fff1e6',name='rg-mobile-strip')
# instagram grid
ig=[op(f'rg-ig-{i}') for i in range(1,6)]
print([i.size for i in ig])
ig=[rr(i.resize((520,520),Image.LANCZOS),24) for i in ig]
c=Image.new('RGB',(3*520+4*50,2*520+3*50),'#fff1e6').convert('RGBA')
pos=[(50,50),(620,50),(1190,50),(335,620),(905,620)]
for i,p in zip(ig,pos): c.alpha_composite(i,p)
c.convert('RGB').save(S+'rg-ig-grid.png')
# sky posts grid
sp=[rr(op(f'sky-post-{i}').resize((560,560),Image.LANCZOS),24) for i in range(1,5)]
c=Image.new('RGB',(2*560+3*50,2*560+3*50),'#0f0f10').convert('RGBA')
for i,p in zip(sp,[(50,50),(660,50),(50,660),(660,660)]): c.alpha_composite(i,p)
c.convert('RGB').save(S+'sky-posts-grid.png')
