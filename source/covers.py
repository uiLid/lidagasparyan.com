from PIL import Image, ImageDraw, ImageFilter, ImageFont
S='shots/'
W,H=1800,1100
def grad(c1,c2):
    import numpy as np
    y,x=np.mgrid[0:H,0:W]; t=((x/W)*0.6+(y/H)*0.4)[...,None]
    arr=np.array(c1)*(1-t)+np.array(c2)*t
    return Image.fromarray(arr.astype('uint8'))
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def card(img,w,chrome,radius=22):
    im=Image.open(S+img+'.png').convert('RGB') if isinstance(img,str) else img.convert('RGB')
    h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    bar=44 if chrome else 0
    out=Image.new('RGBA',(w,h+bar),(255,255,255,255))
    if chrome:
        d=ImageDraw.Draw(out); d.rectangle((0,0,w,bar),fill=(243,244,246))
        for i,c in enumerate(['#ff5f57','#febc2e','#28c840']): d.ellipse((18+i*22,15,32+i*22,29),fill=c)
        d.rounded_rectangle((w//2-170,10,w//2+170,34),8,fill=(255,255,255))
    out.paste(im,(0,bar))
    m=Image.new('L',out.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,out.width-1,out.height-1),radius,fill=255)
    out.putalpha(m); return out
def place(bg,c,x,y,rot=0):
    if rot: c=c.rotate(rot,expand=True,resample=Image.BICUBIC)
    sh=Image.new('RGBA',(c.width+160,c.height+160),(0,0,0,0))
    a=c.split()[3].point(lambda v:int(v*0.35)); sh.paste((10,10,30,255),(80,100),a)
    sh=sh.filter(ImageFilter.GaussianBlur(36))
    bg.alpha_composite(sh,(x-80,y-80)); bg.alpha_composite(c,(x,y))
def make(name,c1,c2,items):
    bg=grad(hexc(c1),hexc(c2)).convert('RGBA')
    for kind,img,crop,x,y,w,rot in items:
        im=Image.open(S+img+'.png').convert('RGB')
        if crop: im=im.crop(crop)
        place(bg,card(im,w,kind=='b'),x,y,rot)
    bg.convert('RGB').save(S+'cov-'+name+'.png'); print(name)
B,P='b','p'
if __name__=='__main__':
  make('case-10web','#1b1464','#4f46e5',[(B,'workspaces',None,880,110,860,0),(B,'menu-expanded',None,120,400,1040,0)])
  make('case-copilot','#0f172a','#7c3aed',[(P,'copilot-askai',(0,0,627,880),1180,130,500,0),(B,'copilot-intro',None,120,330,1100,0)])
  make('case-42smm','#fde68a','#fb7185',[(B,'smm-ai',None,860,110,860,0),(B,'smm-calendar',None,110,330,1080,0)])
  make('case-regardify','#1f2937','#6366f1',[(B,'regardify-task',None,860,90,860,0),(B,'regardify-weekly',None,110,330,1080,0)])
  make('case-centrallapp','#e0e7ff','#a5b4fc',[(B,'central-pair',None,300,200,1200,0)])
  make('case-matheapp','#fde68a','#f97316',[(B,'mathe-practice',None,880,110,820,0),(B,'mathe-onboarding',None,110,360,1060,0)])
  make('case-luufen','#fce7f3','#f472b6',[(P,'luufen-page',(0,0,1421,1000),950,110,700,0),(B,'luufen-flavours',None,110,430,1100,0)])
  make('case-websites','#111827','#475569',[(B,'web-zeppelin',(0,0,1440,900),960,90,780,0),(B,'web-internet',(0,0,1117,700),780,500,900,0),(B,'web-skylab',(0,0,715,900),130,150,560,0)])
  make('case-reemdried','#fed7aa','#fb923c',[(P,'fd-strawberry',None,150,160,470,-4),(P,'fd-apricot-art',None,1180,160,470,4),(P,'fd-pouch',None,560,70,620,0)])
  make('case-honey','#fef3c7','#f59e0b',[(P,'honey-shop',(0,0,602,900),1180,200,520,3),(P,'honey-products',(0,0,725,900),150,200,560,-3),(P,'honey-home',(0,0,488,820),700,110,500,0)])
  make('case-cvds','#ede9fe','#a78bfa',[(B,'cv-ds-overview',None,230,200,1340,0)])
  make('case-10webds','#1e1b4b','#4338ca',[(B,'ds10-buttons',None,900,560,820,0),(B,'ds10-thumb',(0,0,1600,1100),110,130,1000,0)])
  make('case-connectai','#dbeafe','#60a5fa',[(P,'cai-onboarding',None,1000,90,640,0),(B,'cai-dash',None,110,300,1100,0)])
