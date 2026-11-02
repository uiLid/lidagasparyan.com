exec(open('/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2/add2_head.py').read())
src=open(f"{B}/src.html",encoding="utf-8").read()
a=src.index('<div data-route="leadership"'); b=src.index('<div data-route="case-aiimage"')
LI=("Leadership","Лидерство")
def crumbs(p,name):
    return p.replace('<a href="#about">About</a><span aria-hidden="true">/</span>','').replace('<a href="#work">Work</a><span aria-hidden="true">/</span>',f'<a href="#leadership">{T(*LI)}</a><span aria-hidden="true">/</span>',1)
SUM=("Seaside Startup Summit","Seaside Startup Summit"); LER=("Café Lermontov, Director","Кафе «Лермонтов», директор")
summit=case("lead-summit",SUM,("Leadership · Experience","Лидерство · Опыт"),
 ("A startup summit that moves from place to place, and the teams that make it work.","Стартап-саммит, который переезжает с места на место, и команды, которые обеспечивают его работу."),
 [(("Role","Роль"),("Team Lead, then Head of Team Leads","Тимлид, затем руководитель тимлидов")),(("Since","С"),("2018","2018 года")),(("Places","Места"),("India, Armenia, United Arab Emirates","Индия, Армения, ОАЭ"))],
 [(("What I did","Чем занималась"),("I started by leading one team and later led the people who lead the teams.","Начинала с руководства одной командой, затем стала вести тех, кто руководит командами.")),
  (("The challenge","Сложность"),("The summit takes place in a different place each time, so teams, rules and logistics are rebuilt on the spot.","Саммит каждый раз проходит в новом месте, поэтому команды, правила и логистика выстраиваются заново на месте.")),
  (("The result","Итог"),("A repeatable way of working that new Team Leads can pick up quickly.","Повторяемый способ работы, который новые тимлиды быстро осваивают."))],
 [sec(("Places","Места"),[("Each edition brought a new setting.","Каждый выпуск проходил в новом месте.")],
   bullets=[(("India.","Индия."),("Rajasthan and Goa.","Раджастхан и Гоа.")),(("Armenia.","Армения."),("Lake Sevan.","Озеро Севан.")),(("United Arab Emirates.","ОАЭ."),("Ras Al Khaimah and Al Marjan Island.","Рас-эль-Хайма и остров Аль-Маржан."))])],
 [fig("cov-lead-summit",1800,1100,"Seaside Startup Summit with the places visited: India Rajasthan and Goa, Armenia Sevan, UAE Ras Al Khaimah and Al Marjan Island.",("Where the summit took place","Где проходил саммит"),("Five locations in three countries.","Пять мест в трёх странах."))],
 ("Photos from the summit can be added to this page.","Фотографии с саммита можно добавить на эту страницу."),
 ("leadership",LI),("lead-lermontov",LER))
summit=crumbs(summit,"")
ler=case("lead-lermontov",LER,("Leadership · Experience","Лидерство · Опыт"),
 ("I ran a seaside café-restaurant and everything around it for four months.","Четыре месяца я руководила прибрежным кафе-рестораном и всем, что вокруг него."),
 [(("Role","Роль"),("Director","Директор")),(("Time","Срок"),("Four months, one season","Четыре месяца, один сезон")),(("Team","Команда"),("The whole staff of every zone","Весь персонал всех зон"))],
 [(("Scope","Объём"),("Café, canteen, game zone, grill zone, beach zone and more.","Кафе, столовая, игровая зона, мангальная зона, пляжная зона и другие.")),
  (("Business","Бизнес"),("Product orders, staff, events and day-to-day running.","Заказы продуктов, персонал, мероприятия и ежедневная работа.")),
  (("Brand","Бренд"),("Menus, banners, event screens, social media and ads.","Меню, баннеры, экраны для мероприятий, соцсети и реклама."))],
 [sec(("What I was responsible for","За что я отвечала"),[],bullets=[
   (("People.","Люди."),("I led the whole staff across all zones.","Я руководила всем персоналом во всех зонах.")),
   (("Supply.","Снабжение."),("I made the product orders.","Я делала заказы продуктов.")),
   (("Events.","Мероприятия."),("I organised events and designed the screens shown at them.","Я организовывала мероприятия и рисовала экраны для них.")),
   (("Marketing.","Маркетинг."),("Social media posts, an updated Yandex business account and paid ads.","Посты для соцсетей, обновлённый бизнес-аккаунт в Яндексе и платная реклама.")),
   (("Design.","Дизайн."),("Two menus for the café, a menu for the grill zone, and banners. See them in the design case study.","Два меню для кафе, меню мангальной зоны и баннеры. Смотрите их в дизайн-кейсе."))]),
  f'  <p class="note" style="margin-top:8px"><a href="#case-lermontov">{T("See the menus and banners","Смотреть меню и баннеры")}</a></p>'],
 [fig("cov-lead-lermontov",1800,1100,"Café Lermontov, Director for four months, with a menu cover and the zones I led.",("The café and its zones","Кафе и его зоны"),("The zones I led and the menu cover I designed.","Зоны, которыми я руководила, и обложка меню, которую я нарисовала."))],
 None,("lead-summit",SUM),("leadership",LI,("Back to leadership","К разделу «Лидерство»")))
ler=crumbs(ler,"")
cards=lambda r,k,t,d,tags: f'    <a class="card" href="#{r}"><div class="thumb"><img src="{{{{img:{k}}}}}" alt="" width="1800" height="1100"></div><div><h3>{T(*t)}</h3><p>{T(*d)}</p></div><div class="tags">'+''.join(f'<span class="tag{" accent" if i==0 else ""}">{T(*x)}</span>' for i,x in enumerate(tags))+'</div></a>'
idx=(f'<div data-route="leadership" class="page" tabindex="-1" aria-label="{A(*LI)}">\n'
 f'  <nav class="crumbs" aria-label="Breadcrumb"><a href="#home">Home</a><span aria-hidden="true">/</span><span aria-current="page">{T(*LI)}</span></nav>\n'
 f'  <h1 style="font-size:clamp(2.2rem,5vw,3.6rem);margin-top:16px">{T(*LI)}</h1>\n'
 f'  <p class="lead" style="margin-top:14px;color:var(--muted);max-width:56ch;font-size:1.15rem">{T("Leading teams at a startup summit and at a café. Each experience has its own page.","Руководство командами на стартап-саммите и в кафе. У каждого опыта своя страница.")}</p>\n'
 '  <div class="grid two" style="margin-top:32px">\n'
 +cards("lead-summit","cov-lead-summit",SUM,("Team Lead, then Head of Team Leads, in India, Armenia and the UAE.","Тимлид, затем руководитель тимлидов, в Индии, Армении и ОАЭ."),[("Since 2018","С 2018 года"),("Teams","Команды")])+'\n'
 +cards("lead-lermontov","cov-lead-lermontov",LER,("Four months running a seaside café, from staff and orders to events and ads.","Четыре месяца руководства прибрежным кафе: от персонала и заказов до мероприятий и рекламы."),[("Four months","Четыре месяца"),("Operations","Операции")])+'\n  </div>\n</div>\n')
src=src[:a]+idx+summit+ler+src[b:]
# Lermontov design case
LD=("Café Lermontov: menus and banners","Кафе «Лермонтов»: меню и баннеры")
lcase=case("case-lermontov",LD,LBL(GR),
 ("Menus for a seaside café and its grill zone, plus a wide banner, all made while running the café.","Меню для прибрежного кафе и его мангальной зоны и широкий баннер, сделанные в период руководства кафе."),
 [(CL,("Café Lermontov","Кафе «Лермонтов»")),(DI,("Graphic design, print","Графический дизайн, печать")),(SC,("Two menus for the café, a menu for the grill zone, a pizza banner","Два меню для кафе, меню мангальной зоны, баннер для пиццы")),(LG,("Russian","Русский"))],
 [(("Problem","Задача"),("A seaside café needed menus that feel like the place and still work for staff in a hurry.","Прибрежному кафе нужны были меню, которые передают атмосферу места и при этом удобны в спешке.")),
  (("Solution","Решение"),("A calm watercolour look for the café and a loud orange look for the grill zone, with the same clear sections.","Спокойная акварельная тема для кафе и яркая оранжевая для мангальной зоны с одинаковой понятной структурой.")),
  (("Context","Контекст"),("I designed these while I was the café’s Director.","Я делала их, пока была директором кафе."))],
 [f'  <p class="note" style="margin-top:8px"><a href="#lead-lermontov">{T("About my role as Director","О моей роли директора")}</a></p>'],
 [fig("cov-case-lermontov",1800,1100,"A café menu cover with a seaside window view next to a menu page with cold starters on a blue watercolour background.",("The café menu, version 2","Меню кафе, версия 2"),("A cover and an inside page in a mockup. The file also holds a darker first version.","Обложка и внутренняя страница в макете. В файле есть и более тёмная первая версия.")),
  fig("ler-mangal-mock",2000,1000,"A bright orange grill-zone menu with sections for starters, grill, pizza, rolls, sauces and desserts, and a wide orange pizza banner.",("Menu and banner for the grill zone","Меню и баннер для мангальной зоны"),("A warm orange palette with large black brush headings, shown with a wide pizza banner.","Тёплая оранжевая палитра с крупными чёрными кистевыми заголовками и широким баннером для пиццы.")),
  fig("ler-menu-p3",779,1100,"A menu page with cold and hot starters on a blue and white watercolour background with dishes.",("Inside page","Внутренняя страница"),("Cold and hot starters with photographs of real dishes.","Холодные и горячие закуски с фотографиями настоящих блюд."),"shot narrow")],
 ("Mockups were made for this portfolio from the original files.","Макеты сделаны для портфолио по исходным файлам."),
 ("case-friends-mvp",("A platform for making friends, MVP","Платформа для знакомств и дружбы: MVP")),("work",("Back to the work index","Назад к списку работ"),("All work","Все работы")))
src=src.replace('<div data-route="about"',"<!-- CASE: LERMONTOV -->\n"+lcase+'<div data-route="about"',1)
# friends-mvp pager next -> lermontov
i=src.index('data-route="case-friends-mvp"'); j=src.index('<a class="next" href="#work">',i); k=src.index('</a>',j)+4
src=src[:j]+f'<a class="next" href="#case-lermontov"><span class="mono">Next</span><span class="t">{LD[0]}</span></a>'+src[k:]
# Work grid: remove leadership card, add lermontov card
src=re.sub(r'    <a class="card" data-kind="product" href="#leadership">.*?</a>\n','',src,flags=re.S)
lc=card("case-lermontov","graphic","cov-case-lermontov",1800,1100,LD,("Two menus, a grill-zone menu and a banner for a seaside café.","Два меню, меню мангальной зоны и баннер для прибрежного кафе."),[GR,("Print","Печать")]).replace('<img data-use="cov-case-lermontov" alt=""','<img src="{{img:cov-case-lermontov}}" alt=""')
m=re.search(r'(    <a class="card" data-kind="product" href="#case-friends-mvp">.*?</a>\n)',src); src=src.replace(m.group(1),m.group(1)+lc+"\n",1)
# covers on cards
import os
for r in ['case-10web','case-copilot','case-42smm','case-regardify','case-centrallapp','case-matheapp','case-luufen','case-websites','case-reemdried','case-honey','case-cvds','case-10webds','case-connectai']:
    src,n=re.subn(r'(href="#%s"><div class="thumb">)<img data-use="[\w-]+" alt="" width="\d+" height="\d+">'%r, r'\1<img src="{{img:cov-%s}}" alt="" width="1800" height="1100">'%r, src); print(r,n)
# nav
src=src.replace('      <a href="#about" data-nav="about">About</a>','      <a href="#leadership" data-nav="leadership">Leadership</a>\n      <a href="#about" data-nav="about">About</a>',1)
src=src.replace('<a href="#work">Work</a><a href="#about">About</a><a href="#design-system">','<a href="#work">Work</a><a href="#leadership">Leadership</a><a href="#about">About</a><a href="#design-system">',1)
src=src.replace("if (r.indexOf('case-') === 0) return 'work';","if (r.indexOf('case-') === 0) return 'work';\n    if (r.indexOf('lead-') === 0) return 'leadership';",1)
open(f"{B}/src.html","w",encoding="utf-8").write(src)
RUN.update({"Leadership":"Лидерство","Time":"Срок","Team":"Команда","Since":"С","Business":"Бизнес","Brand":"Бренд","Context":"Контекст","Print":"Печать"})
open(f"{B}/ru_new3.py","w",encoding="utf-8").write("RU.update("+json.dumps(RUN,ensure_ascii=False)+")\n")
print('ok',len(RUN))
