from covers import *
from PIL import ImageFont
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/opentype/inter/Inter-{w}.otf',s)
def chips(d,items,x,y,maxw,fill,fg,font):
    cx,cy=x,y
    for t in items:
        w=d.textlength(t,font=font)+56
        if cx+w>x+maxw: cx=x; cy+=84
        d.rounded_rectangle((cx,cy,cx+w,cy+64),32,fill=(255,255,255),outline=None); d.text((cx+28,cy+14),t,font=font,fill=(20,20,50)); cx+=w+16
def lead(name,c1,c2,title,sub,items,card_img=None):
    bg=grad(hexc(c1),hexc(c2)).convert('RGBA'); d=ImageDraw.Draw(bg)
    d.text((110,150),sub,font=F('Medium',40),fill=(255,255,255,200))
    d.text((110,215),title,font=F('Bold',112),fill='white')
    chips(d,items,110,640 if card_img else 520,950 if card_img else 1500,(255,255,255,40),'white',F('Medium',34))
    if card_img:
        im=Image.open(S+card_img+'.png').convert('RGB'); c=card(im,520,False,26)
        place(bg,c,1130,200,4)
    bg.convert('RGB').save(S+'cov-'+name+'.png')
lead('lead-summit','#0e7490','#1e1b4b','Seaside Startup Summit','Team Lead, then Head of Team Leads',['India: Rajasthan','India: Goa','Armenia: Sevan','UAE: Ras Al Khaimah','UAE: Al Marjan Island'])
lead('lead-lermontov','#7c2d12','#1e1b4b','Café Lermontov','Director for four months',['Café','Canteen','Game zone','Grill zone','Beach zone','Events','Menus','Ads'],'ler-cover')
im=Image.open(S+'ler-menu-mock.png').convert('RGB').resize((1800,1125),Image.LANCZOS).crop((0,12,1800,1112)); im.save(S+'cov-case-lermontov.png')
