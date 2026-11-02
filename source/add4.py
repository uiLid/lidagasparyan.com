exec(open('/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2/add2_head.py').read())
src=open(f"{B}/src.html",encoding="utf-8").read()
MF=("MF5 agency website, start a project","Сайт агентства MF5: старт проекта")
ZP=("Zeppelin Cat Armenia website","Сайт Zeppelin Cat Armenia")
UP=("UP2 e-commerce startup","UP2: стартап в сфере e-commerce")
GS=("Green Suitcase travel service","Green Suitcase: сервис для путешествий")
BZ=("Bardzunq logo","Логотип Bardzunq")
LD=("Café Lermontov: menus and banners","Кафе «Лермонтов»: меню и баннеры")
chain=[("case-lermontov",LD),("case-mf5",MF),("case-zeppelin",ZP),("case-up2",UP),("case-greensuitcase",GS),("case-bardzunq",BZ)]
WORK=("work",("Back to the work index","Назад к списку работ"),("All work","Все работы"))
def pg(i,**kw):
    r,t=chain[i]; nxt=chain[i+1] if i+1<len(chain) else WORK
    return case(r,t,prev=chain[i-1],nxt=nxt,**kw)
NOTE_MF5=("Shown as part of a portfolio. Projects with MF5, a marketing company working between Spain and Germany.","Показано в рамках портфолио. Проекты с MF5, маркетинговой компанией, работающей между Испанией и Германией.")
pages=[]
pages.append(pg(1,label=LBL(WB),
 lead=("The questionnaire that starts every project on the MF5 agency website.","Анкета, с которой на сайте агентства MF5 начинается каждый проект."),
 meta=[(CL,("MF5, a marketing company in Spain and Germany","MF5, маркетинговая компания в Испании и Германии")),(DI,("Web design, UX","Веб-дизайн, UX")),(SC,("A full-screen step-by-step form with progress, 14 question screens and a start screen","Полноэкранная пошаговая форма с прогрессом, 14 экранов вопросов и стартовый экран")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("A long brief scares people off, but the agency needs the details to prepare a strategy.","Длинный бриф отпугивает, но агентству нужны детали, чтобы подготовить стратегию.")),
         (("Solution","Решение"),("One question per screen, a progress line, and an honest time estimate of one to five minutes.","Один вопрос на экран, полоса прогресса и честная оценка времени: от одной до пяти минут.")),
         (("Detail","Деталь"),("A clear way out for people in a hurry: “I don’t have the time”.","Понятный выход для тех, кто спешит: «У меня нет времени».")) ],
 sections=[sec(("Decisions","Решения"),[],steps=[
   (("A friendly opening.","Дружелюбное начало."),("The start screen says “Enough about us, let’s talk about you!” and offers one green button.","Стартовый экран говорит: «Хватит о нас, поговорим о вас!» и предлагает одну зелёную кнопку.")),
   (("Dark and calm.","Тёмный и спокойный."),("A dark panel with one lime accent keeps attention on the question.","Тёмная панель с одним лаймовым акцентом удерживает внимание на вопросе.")),
   (("Always oriented.","Всегда понятно, где ты."),("A progress line in the corner and up and down buttons show where you are and let you go back.","Полоса прогресса в углу и кнопки вверх и вниз показывают, где вы, и позволяют вернуться."))])],
 figs=[fig("cov-case-mf5",1800,1100,"Two dark questionnaire screens with lime green buttons in browser frames.",("The questionnaire","Анкета"),("The start screen and the first question.","Стартовый экран и первый вопрос.")),
       fig("mf5-start",1440,1080,"Start screen: Enough about us, let’s talk about you, with a green Start a project button and a progress line.",("Start screen","Стартовый экран"),("One sentence, one button.","Одна фраза, одна кнопка.")),
       fig("mf5-q1",1440,1080,"Question 1 with two answers: I’m ready to get started and I don’t have the time.",("First question","Первый вопрос"),("Two answers, including a polite exit.","Два ответа, включая вежливый отказ."))],
 note=NOTE_MF5))
pages.append(pg(2,label=LBL(WB),
 lead=("A website concept for the Armenian dealer of Caterpillar machines and parts.","Концепт сайта для армянского дилера техники и запчастей Caterpillar."),
 meta=[(CL,("Zeppelin Cat Armenia, via MF5","Zeppelin Cat Armenia, через MF5")),(DI,("Web design","Веб-дизайн")),(SC,("Home page, product categories, offers, service, parts, testimonials, footer. Russian-language navigation","Главная страница, категории техники, предложения, сервис, запчасти, отзывы, подвал. Навигация на русском")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("A large range of machines, services and parts had to be easy to enter from one page.","Большой ассортимент техники, сервисов и запчастей должен быть доступен с одной страницы.")),
         (("Solution","Решение"),("Big photo tiles for the main markets and small tiles for the other lines, in the brand yellow and black.","Крупные фото-плитки для основных рынков и малые для остальных направлений в фирменных жёлтом и чёрном.")),
         (("Detail","Деталь"),("A bright strip, “Faster, easier parts”, sends people straight to the parts shop.","Яркая полоса «Быстрее, проще запчасти» ведёт прямо в магазин запчастей."))],
 sections=[sec(("The page, from top to bottom","Страница сверху вниз"),[],bullets=[
   (("Hero.","Главный экран."),("A full-width photo of a loader with one call to action.","Фото погрузчика во всю ширину и один призыв к действию.")),
   (("Markets.","Направления."),("Construction and mining, agriculture, then power systems, rental, used machines and material handling.","Строительство и добыча, сельское хозяйство, затем энергосистемы, аренда, б/у техника и погрузочная техника.")),
   (("Offers and service.","Предложения и сервис."),("An offers block, then a dark service block with a branded van.","Блок предложений и тёмный блок сервиса с фирменным фургоном.")),
   (("Parts and trust.","Запчасти и доверие."),("The parts banner, client testimonials, social links and a newsletter form.","Баннер запчастей, отзывы клиентов, ссылки на соцсети и форма подписки."))])],
 figs=[fig("cov-case-zeppelin",1800,1100,"The Zeppelin Cat Armenia home page with a loader hero and category tiles in browser frames.",("The home page","Главная страница"),("The hero and the category tiles.","Главный экран и плитки направлений.")),
       fig("zep-home",1440,4000,"The full Zeppelin Cat Armenia home page: hero, category tiles, offers, service, parts banner, testimonials and footer.",("The full page","Страница целиком"),("Photos are placeholders from the concept, and some text is sample copy.","Фото и часть текста в концепте условные."),"shot narrow")],
 note=NOTE_MF5))
pages.append(pg(3,label=LBL(WB),
 lead=("A landing page for a German startup that opens an online store for small businesses in a few steps.","Лендинг для немецкого стартапа, который помогает малому бизнесу открыть интернет-магазин за несколько шагов."),
 meta=[(CL,("UP2, a startup in Germany","UP2, стартап в Германии")),(DI,("Web design, UX","Веб-дизайн, UX")),(SC,("A long landing page in Armenian with pricing, FAQ and a contact form, plus mobile screens","Длинный лендинг на армянском с тарифами, FAQ и формой обратной связи, а также мобильные экраны")),(LG,("Armenian, English","Армянский, английский"))],
 glance=[(("Problem","Задача"),("Small shops needed a clear promise: your own online store, free during the first period, without technical work.","Малым магазинам нужно было понятное обещание: собственный интернет-магазин, бесплатно в первый период, без технической работы.")),
         (("Solution","Решение"),("A dark hero with one button, four simple steps, benefits as icons, and four plan cards.","Тёмный первый экран с одной кнопкой, четыре простых шага, преимущества в иконках и четыре карточки тарифов.")),
         (("Detail","Деталь"),("A green block with two actions: get a demo or open the admin panel.","Зелёный блок с двумя действиями: получить демо или открыть админ-панель."))],
 sections=[sec(("Structure","Структура"),[],steps=[
   (("Four steps.","Четыре шага."),("A guided path from choosing products to launching the shop.","Путь от выбора товаров до запуска магазина.")),
   (("Why go online.","Зачем выходить в онлайн."),("Six benefits, from being open to the world to analytics.","Шесть преимуществ: от открытости миру до аналитики.")),
   (("Plans.","Тарифы."),("Basic, fixed price, monthly and a special offer, with the recommended plan lifted above the others.","Базовый, фиксированная цена, помесячный и специальное предложение; рекомендуемый тариф приподнят над остальными.")),
   (("Trust.","Доверие."),("Questions and answers, a contact form and phone, email and social links.","Вопросы и ответы, форма связи, телефон, почта и ссылки на соцсети."))])],
 figs=[fig("cov-case-up2",1800,1100,"The UP2 landing page: a dark hero with the title and a plans section in browser frames.",("The landing page","Лендинг"),("The hero and the pricing area.","Первый экран и блок тарифов.")),
       fig("up2-web",1439,7389,"The full UP2 landing page in Armenian: hero, four steps, benefits, plans, FAQ and contact form.",("The full page","Страница целиком"),("From the hero to the contact form.","От первого экрана до формы обратной связи."),"shot narrow")],
 note=NOTE_CLIENT))
pages.append(pg(4,label=LBL(WB),
 lead=("A landing page for a travel logistics service that gathers trip information in one place.","Лендинг сервиса туристической логистики, который собирает информацию о поездке в одном месте."),
 meta=[(CL,("Green Suitcase","Green Suitcase")),(DI,("Web design, product","Веб-дизайн, продукт")),(SC,("Landing page with a search by place, dates and price, a how-it-works block, a gallery, a blog and subscription","Лендинг с поиском по месту, датам и цене, блоком «как это работает», галереей, блогом и подпиской")),(TL,("Figma, FigJam","Figma, FigJam"))],
 glance=[(("Problem","Задача"),("People plan trips across many tabs. The service had to promise one place for it.","Люди планируют поездки в десятках вкладок. Сервис должен был пообещать одно место для этого.")),
         (("Solution","Решение"),("A search bar sits right in the hero, then three steps: tell us, share your preferences, get recommendations.","Строка поиска прямо на главном экране, затем три шага: расскажите, поделитесь предпочтениями, получите рекомендации.")),
         (("Detail","Деталь"),("A photo mosaic of destinations makes the next step feel like an adventure.","Мозаика фото направлений превращает следующий шаг в приключение."))],
 sections=[sec(("Structure","Структура"),[],bullets=[
   (("Search first.","Сначала поиск."),("Place, dates and average price in one bar with one button.","Место, даты и средняя цена в одной строке с одной кнопкой.")),
   (("Trust.","Доверие."),("Partner logos, a “Why choose us” block and customer quotes.","Логотипы партнёров, блок «Почему мы» и отзывы клиентов.")),
   (("Inspiration.","Вдохновение."),("A mosaic of destinations and a blog with four articles.","Мозаика направлений и блог с четырьмя статьями.")),
   (("Retention.","Удержание."),("A subscription block with deals and offers.","Блок подписки на акции и предложения."))])],
 figs=[fig("cov-case-greensuitcase",1800,1100,"The Green Suitcase landing page with a search bar and a destination gallery in browser frames.",("The landing page","Лендинг"),("The hero with search and the destinations mosaic.","Главный экран с поиском и мозаика направлений.")),
       fig("gs-landing",1280,5500,"The full Green Suitcase landing page: hero with search, how it works, why choose us, destinations, blog, testimonials, subscription and footer.",("The full page","Страница целиком"),("Sample texts and photos from the concept.","Тексты и фото из концепта условные."),"shot narrow")],
 note=("The affinity mapping board and the MVP are not shown on this page yet.","Доска аффинити-мэппинга и MVP пока не показаны на этой странице.")))
pages.append(pg(5,label=LBL(GR),
 lead=("A logo for an Armenian brand: a faceted mountain at sunrise with a tall custom wordmark.","Логотип для армянского бренда: гранёная гора на восходе и высокий авторский логотип-шрифт."),
 meta=[(CL,("Bardzunq","Bardzunq")),(DI,("Logo design, identity","Логотип, айдентика")),(SC,("An emblem, a wordmark and a combined logo","Эмблема, логотип-шрифт и комбинированный знак")),(LG,("Armenian","Армянский"))],
 glance=[(("Idea","Идея"),("The name means a height, so the mark is a mountain, drawn in facets like cut glass.","Название означает высоту, поэтому знак это гора, нарисованная гранями, как огранённое стекло.")),
         (("Colour","Цвет"),("A warm sunrise sky above cool blue slopes, and a deep navy wordmark.","Тёплое небо восхода над холодными синими склонами и тёмно-синий логотип.")),
         (("System","Система"),("The emblem works alone, with the wordmark, and as a small mark inside the lettering.","Эмблема работает отдельно, с логотипом-шрифтом и как маленький знак внутри букв."))],
 sections=[],
 figs=[fig("cov-case-bardzunq",1800,1100,"The Bardzunq emblem with the wordmark below, and the wordmark filled with the same facets.",("The logo","Логотип"),("Combined logo and the faceted wordmark.","Комбинированный знак и граненый логотип-шрифт.")),
       fig("bardz-both",409,409,"Bardzunq combined logo: a faceted mountain at sunrise in a circle, with the Armenian wordmark below.",("Combined logo","Комбинированный знак"),("The emblem above, the wordmark below.","Эмблема сверху, логотип снизу."),"shot narrow"),
       fig("bardz-logo",856,295,"The Bardzunq wordmark filled with blue facets, with the small emblem in the lettering.",("Faceted wordmark","Граненый логотип-шрифт"),("The same facets, carried into the letters.","Те же грани в буквах."))],
 note=("Social media visuals for this brand can be added to this page.","Визуалы для соцсетей этого бренда можно добавить на эту страницу.")))
# insert pages before ABOUT
src=src.replace("<!-- ABOUT -->","<!-- CASES: MF5 etc -->\n"+"\n".join(pages)+"\n<!-- ABOUT -->",1)
# lermontov next
i=src.index('data-route="case-lermontov"'); j=src.index('<a class="next" href="#work">',i); k=src.index('</a>',j)+4
src=src[:j]+f'<a class="next" href="#case-mf5"><span class="mono">Next</span><span class="t">{MF[0]}</span></a>'+src[k:]
# cards
cs=[card("case-mf5","web","cov-case-mf5",1800,1100,MF,("A full-screen step-by-step brief form for a marketing agency.","Полноэкранная пошаговая форма брифа для маркетингового агентства."),[WB,("MF5","MF5")]),
 card("case-zeppelin","web","cov-case-zeppelin",1800,1100,ZP,("A website concept for a Caterpillar dealer: machines, service and parts.","Концепт сайта дилера Caterpillar: техника, сервис и запчасти."),[WB,("Zeppelin","Zeppelin")]),
 card("case-up2","web","cov-case-up2",1800,1100,UP,("A landing page for a German startup that helps shops go online.","Лендинг для немецкого стартапа, который помогает магазинам выйти в онлайн."),[WB,("Startup","Стартап")]),
 card("case-greensuitcase","web","cov-case-greensuitcase",1800,1100,GS,("A landing page for a travel logistics service.","Лендинг сервиса туристической логистики."),[WB,("Travel","Путешествия")]),
 card("case-bardzunq","graphic","cov-case-bardzunq",1800,1100,BZ,("A faceted mountain emblem with a custom Armenian wordmark.","Эмблема-гора из граней и авторский армянский логотип-шрифт."),[GR,("Logo","Логотип")])]
cs=[c.replace('<img data-use="cov-','<img src="{{img:cov-').replace('" alt=""','}}" alt=""',1) if 'data-use' in c else c for c in cs]
cs=[re.sub(r'<img data-use="(cov-[\w-]+)" alt=""',r'<img src="{{img:\1}}" alt=""',c) for c in cs]
m=re.search(r'(    <a class="card" data-kind="graphic" href="#case-lermontov">.*?</a>\n)',src); src=src.replace(m.group(1),m.group(1)+"\n".join(cs)+"\n",1)
# luufen: new cover on card, new figs on page
src,n=re.subn(r'(href="#case-luufen"><div class="thumb">)<img data-use="[\w-]+" alt="" width="\d+" height="\d+">',r'\1<img src="{{img:cov-case-luufen}}" alt="" width="1800" height="1100">',src); print('luufen card',n)
newf="\n".join([fig("luufen-hero",1440,1024,"Luufen home page with a vertical logo, a circular menu, a Viking ship and a watercolour wave.",("Home page, Original flavour","Главная, вкус Original"),("A circular menu moves between flavours. The logo stands vertically on the left, and a watercolour wave closes the screen.","Круговое меню переключает вкусы. Логотип стоит вертикально слева, а акварельная волна завершает экран.")),
 fig("luufen-cbd",1440,1024,"Luufen CBD page with a green watercolour leaf and the story of the name.",("The CBD story","История про CBD"),("A watercolour leaf and a short story of how the name Lüufen came to be.","Акварельный лист и короткая история о том, как появилось название Lüufen.")),
 fig("luufen-page",1440,4562,"Luufen product page for the Original can with callouts, nutrition facts and a footer.",("Product page","Страница продукта"),("A can on an ice field, circled in red, with callouts for what is inside.","Банка на льдине, обведённая красным, с подписями о составе."),"shot narrow")])
a=src.index('data-route="case-luufen"'); b=src.index('<div class="shots">',a)+len('<div class="shots">')
src=src[:b]+"\n"+newf+src[b:]
src=src.replace("Twenty-five case studies,","Thirty case studies,").replace("Case studies (25)","Case studies (30)")
src=re.sub(r'(<span class="n">)25(</span><span class="t">case studies)',r'\g<1>30\2',src)
open(f"{B}/src.html","w",encoding="utf-8").write(src)
RUN.update({"Thirty case studies, each told through the real work. Filter by discipline.":"Тридцать кейсов, каждый показан через реальную работу. Фильтруйте по направлению.","Case studies (30)":"Кейсы (30)","Detail":"Деталь","Idea":"Идея","Colour":"Цвет","System":"Система","Startup":"Стартап","Travel":"Путешествия","Logo":"Логотип","Zeppelin":"Zeppelin","MF5":"MF5"})
open(f"{B}/ru_new4.py","w",encoding="utf-8").write("RU.update("+json.dumps(RUN,ensure_ascii=False)+")\n")
print("ok",len(RUN))
