exec(open('/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2/add2_head.py').read())
from PIL import Image
SH='/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/shots/'
def F(img,alt,t,d,cls="shot"):
    w,h=Image.open(SH+img+'.png').size
    return fig(img,w,h,alt,t,d,cls)
SKYL=("SkyLab, a software and design studio","SkyLab, студия разработки и дизайна")
NOTE=("Studio project made at SkyLab and shown as part of a portfolio.","Студийный проект, сделанный в SkyLab и показанный в рамках портфолио.")
FM=("Fermalytics app, logo and landing","Fermalytics: приложение, логотип и лендинг")
SK=("SkyLab brand: day and night landing, social media","Бренд SkyLab: дневной и ночной лендинг, соцсети")
AB=("ABC Domain: landing, mobile, tablet and 404","ABC Domain: лендинг, мобильная и планшетная версии, 404")
RG=("Regardify brand, landing and social media","Regardify: бренд, лендинг и соцсети")
GM=("Games: Warriors Path, Countries and Virus","Игры: Warriors Path, Countries и Virus")
chain=[("case-bardzunq",("Bardzunq logo","Логотип Bardzunq")),("case-fermalytics",FM),("case-sky",SK),("case-abc-domain",AB),("case-regardify-brand",RG),("case-games",GM)]
WORK=("work",("Back to the work index","Назад к списку работ"),("All work","Все работы"))
def pg(i,**kw):
    r,t=chain[i]; nxt=chain[i+1] if i+1<len(chain) else WORK
    return case(r,t,prev=chain[i-1],nxt=nxt,**kw)
pages=[]
# ---------- Fermalytics
pages.append(pg(1,label=LBL(PR),
 lead=("A mobile app, a logo and a landing page for people who make cheese and beer at home and want to learn from every batch.","Мобильное приложение, логотип и лендинг для тех, кто делает сыр и пиво дома и хочет учиться на каждой варке."),
 meta=[(CL,SKYL),(DI,("Product design, branding, web design","Продуктовый дизайн, брендинг, веб-дизайн")),(SC,("Brand and logo, mobile and tablet app screens, landing page","Бренд и логотип, экраны мобильного приложения и планшета, лендинг")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("Home fermenters keep notes on paper and in spreadsheets, so they can’t compare batches or learn from other makers.","Домашние ферментаторы ведут записи на бумаге и в таблицах, поэтому не могут сравнивать варки и учиться у других.")),
         (("Solution","Решение"),("An app that guides the make day with timers and steps, records temperature and pH, and shows how your batch compares with the crowd.","Приложение, которое ведёт по дню варки таймерами и шагами, записывает температуру и pH и показывает, как ваша варка соотносится с другими.")),
         (("Result","Результат"),("A full set: a recognisable bubble-and-cheese mark, app screens for phone and tablet, and a landing page that explains the idea.","Полный комплект: узнаваемый знак из пузырьков и сыра, экраны для телефона и планшета и лендинг, который объясняет идею."))],
 sections=[sec(("The idea","Идея"),[("Fermalytics (fermentation analytics) collects the data of successful and not so successful makes. The app is used on the make day, the site is for review afterwards. The goal is to replace pen and paper with a shared database of processes.","Fermalytics (аналитика ферментации) собирает данные удачных и не очень варок. Приложением пользуются в день варки, сайтом позже, чтобы разобрать результаты. Цель: заменить ручку и бумагу общей базой процессов."),],
   steps=[]),
  sec(("Brand","Бренд"),[("The mark is a block of cheese seen as a stepped bar chart, with bubbles as the holes. It works in white on blue, in blue on white and as a circle app icon. Blue was chosen to stay apart from the usual yellow and brown of food apps and to feel like data.","Знак — кусок сыра, прочитанный как ступенчатая диаграмма, а пузырьки — это дырки. Он работает белым на синем, синим на белом и в круглой иконке приложения. Синий выбран, чтобы отличаться от привычных жёлтых и коричневых цветов food-приложений и ассоциироваться с данными."),]),
  sec(("The app","Приложение"),[],steps=[
   (("One home, two crafts.","Один экран, два ремесла."),("Cheese and Beer are switched at the top; New make, In progress and History are the only actions on the main screen.","Сыр и пиво переключаются сверху; «Новая варка», «В процессе» и «История» — единственные действия на главном экране.")),
   (("Charts first.","Сначала графики."),("The live chart shows your temperature and pH with the user average and the crowd average, so you see at once if the batch drifts.","Живой график показывает вашу температуру и pH, среднее по вам и среднее по сообществу, поэтому сразу видно, если варка уходит в сторону.")),
   (("Steps and timers.","Шаги и таймеры."),("The current step sits between the past and the next one, with a timer and a big Next step button.","Текущий шаг стоит между прошлым и следующим, с таймером и большой кнопкой «Следующий шаг».")),
   (("Inventory.","Склад."),("Milk, malt and hops with amounts, so ingredients and expiry dates are tracked in the same place.","Молоко, солод и хмель с количеством: ингредиенты и сроки хранятся в одном месте."))]),
  sec(("The landing page","Лендинг"),[("A wavy blue hero introduces the app, a chart shows what Premium unlocks, and long copy explains why crowdsourced fermentation data matters. Desktop, tablet and mobile versions were designed.","Волнистый синий первый экран знакомит с приложением, график показывает, что даёт Premium, а длинный текст объясняет, зачем нужны краудсорсинговые данные о ферментации. Сделаны версии для десктопа, планшета и мобильного."),])],
 figs=[F("cov-case-fermalytics","Fermalytics landing page in a browser beside two phone screens of the app.",("Overview","Обзор"),("The landing and the app together.","Лендинг и приложение вместе.")),
  F("fm-logo-name","The Fermalytics mark of white and blue steps with bubbles and the wordmark below.",("The logo","Логотип"),("The final mark with the wordmark.","Итоговый знак с надписью.")),
  F("fm-logo-circle","The Fermalytics mark inside a white circle on grey.",("App icon","Иконка приложения"),("The circular version used as the app icon.","Круглая версия для иконки приложения.")),
  F("fm-phones","Four Fermalytics phone screens: main, chart with temperature and pH, inventory and a Temp/pH entry form.",("App screens","Экраны приложения"),("Main screen, live chart, inventory and manual temperature and pH entry.","Главный экран, живой график, склад и ручной ввод температуры и pH.")),
  F("fm-land-1","Top half of the Fermalytics landing page: a blue wavy hero, a chart and the How it works block.",("Landing, part 1","Лендинг, часть 1"),("Hero, Premium statistics and How it works.","Первый экран, статистика Premium и «Как это работает».")),
  F("fm-land-2","Bottom half of the landing page: advantages, why Fermalytics, about, a blue call to action and a contact form.",("Landing, part 2","Лендинг, часть 2"),("Advantages, story, call to action and the contact form.","Преимущества, история, призыв к действию и форма связи."))],
 note=NOTE))
# ---------- SKY
def skyfigs(mode,pre,alts):
    o=''
    for i in range(4):
        o+=F(f"{pre}-{i+1}",alts[i],(f"{mode[0]}, part {i+1}",f"{mode[1]}, часть {i+1}"),(alts[4+i][0],alts[4+i][1]))+'\n'
    return o
night_alts=["Night landing, first screen: black page with the SKY logo and a white line-art hand rising from a block stair.","Night landing, services and values with line-art illustrations on black.","Night landing, team and technologies section.","Night landing, portfolio and contact.",
 ("The logo, the stair and the hand set the tone.","Логотип, лестница и рука задают тон."),("Services and the values the studio stands for.","Услуги и ценности студии."),("People and the stack they work in.","Люди и технологии, с которыми они работают."),("Selected work and a way to get in touch.","Избранные работы и контакты.")]
day_alts=["Day landing, first screen: white page with the blue SKYLAB logo, a stair and a hand.","Day landing, services and values with blue line-art illustrations.","Day landing, team and technologies section.","Day landing, portfolio and contact.",
 ("The same story in white and blue.","Та же история в белом и голубом."),("Services and values in the day palette.","Услуги и ценности в дневной палитре."),("Team and technologies, day mode.","Команда и технологии, дневной режим."),("Portfolio and contact, day mode.","Портфолио и контакты, дневной режим.")]
sw=('<div class="sky-switch" role="group" aria-label="'+A("Landing theme","Тема лендинга")+'">'
    '<button type="button" class="chip" data-sky-mode="night" aria-pressed="true">'+T("Night mode","Ночной режим")+'</button>'
    '<button type="button" class="chip" data-sky-mode="day" aria-pressed="false">'+T("Day mode","Дневной режим")+'</button></div>')
night='<div class="sky-group" data-sky="night"><div class="shots">'+skyfigs(("Night mode","Ночной режим"),"sky-n",night_alts)+'</div></div>'
day='<div class="sky-group" data-sky="day" hidden><div class="shots">'+skyfigs(("Day mode","Дневной режим"),"sky-d",day_alts)+'</div></div>'
pages.append(pg(2,label=LBL(GR),
 lead=("A brand and a landing for a software studio, designed twice: as a black night page and as a white day page, with line-art illustrations that carry the story.","Бренд и лендинг для студии разработки, сделанные дважды: чёрная ночная и белая дневная страницы, с иллюстрациями в линейной графике, которые рассказывают историю."),
 meta=[(CL,SKYL),(DI,("Branding, web design, illustration, social media","Брендинг, веб-дизайн, иллюстрация, соцсети")),(SC,("Logo, day and night landing, social posts, banners","Логотип, дневной и ночной лендинг, посты для соцсетей, баннеры")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("A studio that builds software for others needed its own face that feels human and not like another agency template.","Студии, которая делает софт для других, нужно было собственное лицо, живое, а не ещё один шаблон агентства.")),
         (("Solution","Решение"),("A square emblem built from the letters S, K and Y, a strict black, white and blue palette and hand-drawn line illustrations of hands, stairs and statues.","Квадратный знак из букв S, K и Y, строгая палитра из чёрного, белого и голубого и рисованные линейные иллюстрации рук, лестниц и статуй.")),
         (("Result","Результат"),("A site in two moods that you can switch below, plus a social media set with the same visual language.","Сайт в двух настроениях, которые можно переключить ниже, и набор для соцсетей в том же визуальном языке."))],
 sections=[sec(("The brand","Бренд"),[("The emblem is a square frame with S, K and Y cut out of its diagonals. Round and organic illustrations soften the strict geometry: a pointing hand on a stair of blocks, a torso rising from a desert, windows with sketches inside.","Знак — квадратная рамка, в диагоналях которой вырезаны буквы S, K и Y. Мягкие, органичные иллюстрации смягчают строгую геометрию: указывающая рука на лестнице из блоков, торс, поднимающийся из пустыни, окна с набросками внутри."),]),
  sec(("Two moods","Два настроения"),[("The night page is the main version, with white line art on black. The day page keeps the same layout and illustrations, recoloured in blue on white. Use the switch to compare them below.","Ночная страница — основная версия: белая линейная графика на чёрном. Дневная сохраняет ту же сетку и иллюстрации, перекрашенные в голубой на белом. Переключатель ниже позволяет их сравнить."),]),
  sec(("Social media","Соцсети"),[("The same stair-and-hand illustration became a system of posts with quotes, a profile picture and banners, so the studio looks the same on the website, LinkedIn and Facebook.","Та же иллюстрация с лестницей и рукой стала системой постов с цитатами, аватаром и баннерами, чтобы студия выглядела одинаково на сайте, в LinkedIn и Facebook."),])],
 figs=[F("cov-case-sky","Night and day versions of the SKYLAB landing page side by side with a social media post.",("Overview","Обзор"),("Night, day and social media.","Ночь, день и соцсети.")),
  F("sky-logo","The SKYLAB logo, a square frame with S, K and Y letterforms.",("The logo","Логотип"),("The emblem and the wordmark.","Знак и надпись.")),
  sw, night, day,
  F("sky-posts-grid","Four social posts: a quote with a pointing hand on a stair, the same without the quote, a logo on blue, and a statue in a window next to the Fermalytics and SKYLAB logos.",("Social media","Соцсети"),("Quote posts, a logo post and a window collage in the same language.","Посты с цитатами, пост с логотипом и коллаж с окном в одном языке.")),
  F("sky-banner","A blue banner with white paper planes and a large light blue circle.",("Banner","Баннер"),("A banner with paper planes for social profiles.","Баннер с бумажными самолётиками для профилей в соцсетях."))],
 note=NOTE))
# ---------- ABC Domain
pages.append(pg(3,label=LBL(WB),
 lead=("A domain and hosting registrar for Armenia: a landing, a site constructor page, tablet and mobile versions, a mobile app and a set of hand-drawn 404 pages.","Регистратор доменов и хостинга для Армении: лендинг, страница конструктора сайтов, планшетная и мобильная версии, мобильное приложение и набор нарисованных от руки страниц 404."),
 meta=[(CL,("ABC Domain, Armenia","ABC Domain, Армения")),(DI,("Web design, product design, illustration","Веб-дизайн, продуктовый дизайн, иллюстрация")),(SC,("Landing, site constructor page, hosting and SSL pages, tablet and mobile, app screens, 404 illustrations in English and Armenian","Лендинг, страница конструктора сайтов, страницы хостинга и SSL, планшет и мобильная версия, экраны приложения, иллюстрации 404 на английском и армянском")),(LG,("Armenian, English, Russian","Армянский, английский, русский")),(TL,("Figma, Procreate","Figma, Procreate"))],
 glance=[(("Problem","Задача"),("Buying a domain should take a minute, but registrar sites are cluttered, and the local zones .am, .հայ and .arm need to be easy to find.","Купить домен должно быть делом минуты, но сайты регистраторов перегружены, а местные зоны .am, .հայ и .arm должны быть легко найти.")),
         (("Solution","Решение"),("A domain search at the very top, zones as colourful price cards, clear hosting packages and the same system on desktop, tablet and phone.","Поиск домена на самом верху, зоны в виде цветных карточек с ценой, понятные тарифы хостинга и одна система на десктопе, планшете и телефоне.")),
         (("Character","Характер"),("Even the error page has a personality: a hand-drawn ostrich in a hat and glasses, drawn in Procreate.","Даже у страницы ошибки есть характер: нарисованный от руки страус в шляпе и очках, сделанный в Procreate."))],
 sections=[sec(("The landing","Лендинг"),[("The home page starts with the search field, then shows the zones .arm, .am, .hay and .io as colour-coded cards with prices, followed by hosting packages and the reasons to choose the company. The Armenian version sets the tone; English and Russian follow it.","Главная начинается с поля поиска, затем показывает зоны .arm, .am, .hay и .io цветными карточками с ценами, а дальше тарифы хостинга и причины выбрать компанию. Армянская версия задаёт тон, английская и русская следуют за ней."),]),
  sec(("Responsive and app","Адаптив и приложение"),[("The tablet and mobile layouts keep the same order of blocks and turn the menu into a drawer. The mobile app shows domains, services, support tickets and invoices on one dashboard.","Планшетная и мобильная версии сохраняют порядок блоков, а меню превращается в выдвижную панель. Мобильное приложение показывает домены, услуги, обращения в поддержку и счета на одном экране."),]),
  sec(("404 illustrations","Иллюстрации 404"),[("The 404 pages were drawn by hand in Procreate: an ostrich with its head in the sand, a hat, glasses and a jacket that wait on the page as if after a failed disguise. There are versions in English and Armenian, plus tablet and mobile.","Страницы 404 нарисованы от руки в Procreate: страус, который прячет голову в песок, шляпа, очки и пиджак, лежащие на странице как остатки неудачного маскарада. Есть версии на английском и армянском, а также для планшета и мобильного."),])],
 figs=[F("cov-case-abc-domain","The ABC Domain English 404 page, the Armenian landing and an app screen.",("Overview","Обзор"),("404 illustration, landing and app.","Иллюстрация 404, лендинг и приложение.")),
  F("abc-home-1","Armenian home page of ABC Domain: a domain search headline and domain zone cards.",("Landing, part 1","Лендинг, часть 1"),("Domain search and the zone cards.","Поиск доменов и карточки зон.")),
  F("abc-home-2","Lower part of the home page with hosting packages and reasons to choose the company.",("Landing, part 2","Лендинг, часть 2"),("Hosting packages and trust blocks.","Тарифы хостинга и блоки доверия.")),
  F("abc-cons-1","Site constructor page with a colourful illustration at the top.",("Site constructor, part 1","Конструктор сайтов, часть 1"),("A page that sells the site builder.","Страница, которая продаёт конструктор сайтов.")),
  F("abc-cons-2","Lower part of the site constructor page.",("Site constructor, part 2","Конструктор сайтов, часть 2"),("Templates, features and pricing.","Шаблоны, возможности и цены.")),
  F("abc-tablet-strip","Two halves of the tablet layout side by side.",("Tablet","Планшет"),("The tablet layout in two halves.","Планшетная версия в двух частях.")),
  F("abc-mobile-strip","Three parts of the mobile layout side by side.",("Mobile","Мобильная версия"),("The mobile layout in three parts.","Мобильная версия в трёх частях.")),
  F("abc-app-promo","Store promotional image for the ABC Domain mobile app.",("Mobile app","Мобильное приложение"),("The promotional image for the app stores.","Промо-изображение для магазинов приложений.")),
  F("abc-app-1","Mobile app dashboard with domains, services, tickets and invoices.",("App dashboard","Дашборд приложения"),("One screen for domains, services, tickets and invoices.","Один экран для доменов, услуг, обращений и счетов.")),
  F("abc-404-eng","Hand-drawn English 404 page: a rocket, 404 ERROR, a hat, glasses, a jacket and an ostrich.",("404, English","404, английский"),("Hand-drawn in Procreate.","Нарисовано от руки в Procreate.")),
  F("abc-404-arm","Hand-drawn Armenian 404 page with the same ostrich and props.",("404, Armenian","404, армянский"),("The same drawing with Armenian text.","Тот же рисунок с армянским текстом.")),
  F("abc-404-ipad","Tablet 404 page with a drawer menu in Russian.",("404, tablet","404, планшет"),("The tablet version with the drawer menu.","Планшетная версия с выдвижным меню."))],
 note=NOTE))
# ---------- Regardify brand
pages.append(pg(4,label=LBL(GR),
 lead=("A brand, a landing page, mobile screens and social posts for a platform that organises team-building events and keeps remote teams connected.","Бренд, лендинг, мобильные экраны и посты для платформы, которая организует корпоративные события и помогает удалённым командам оставаться на связи."),
 meta=[(CL,SKYL),(DI,("Branding, web design, social media","Брендинг, веб-дизайн, соцсети")),(SC,("Logo, landing and inner pages, mobile screens, Instagram posts","Логотип, лендинг и внутренние страницы, мобильные экраны, посты для Instagram")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("HR teams plan events by hand and remote colleagues lose touch with each other.","HR-команды планируют события вручную, а удалённые коллеги теряют связь друг с другом.")),
         (("Solution","Решение"),("A friendly brand with an F mark of black and white blocks, orange and yellow accents, and a landing that says it directly: “We help organize your connections in a special way”.","Дружелюбный бренд со знаком F из чёрных и белых блоков, оранжевыми и жёлтыми акцентами и лендингом, который говорит прямо: «Мы помогаем организовывать ваши связи особым образом».")),
         (("Result","Результат"),("A wordmark and a mark, a long landing with how-it-works, events, pricing, team and blog pages, mobile screens and a set of Instagram posts.","Логотип и знак, длинный лендинг со страницами «Как это работает», «События», «Цены», «Команда» и «Блог», мобильные экраны и набор постов для Instagram."))],
 sections=[sec(("The brand","Бренд"),[("The mark is a letter F built from blocks, with an orange and a yellow square as playful accents. The wordmark is calm and geometric, so the colourful illustration on the landing does the talking.","Знак — буква F из блоков с оранжевым и жёлтым квадратами в роли игривых акцентов. Логотип спокойный и геометричный, поэтому говорить за бренд остаётся цветной иллюстрации на лендинге."),]),
  sec(("Website and mobile","Сайт и мобильная версия"),[("The landing opens with the promise and a hero illustration, then the logos of well-known companies, how it works, event formats, pricing and the team. The blog, event and team pages share one system, and mobile versions keep the same order.","Лендинг открывается обещанием и иллюстрацией, затем идут логотипы известных компаний, «как это работает», форматы событий, цены и команда. Страницы блога, события и команды работают в одной системе, а мобильные версии сохраняют тот же порядок."),]),
  sec(("Social media","Соцсети"),[("The Instagram posts turn blog articles and tips into square cards that use the same black, orange and yellow.","Посты для Instagram превращают статьи блога и советы в квадратные карточки в тех же чёрном, оранжевом и жёлтом."),])],
 figs=[F("cov-case-regardify-brand","The Regardify landing in a browser beside an Instagram post and a mobile blog screen.",("Overview","Обзор"),("Landing, social post and mobile.","Лендинг, пост и мобильная версия.")),
  F("rg-logo-main","The Regardify wordmark in black on white.",("Wordmark","Логотип"),("The wordmark.","Логотип-надпись.")),
  F("rg-logo-mark","The black and white F mark with an orange and a yellow square.",("The mark","Знак"),("The F mark in black and white with orange and yellow accents.","Знак F в чёрном и белом с оранжевым и жёлтым акцентами.")),
  F("rg-land-1","Regardify landing, first part: hero with illustration and partner logos, then how it works.",("Landing, part 1","Лендинг, часть 1"),("Promise, illustration and logos.","Обещание, иллюстрация и логотипы.")),
  F("rg-land-2","Regardify landing, second part.",("Landing, part 2","Лендинг, часть 2"),("Event formats and pricing.","Форматы событий и цены.")),
  F("rg-land-3","Regardify landing, third part with the team and the footer.",("Landing, part 3","Лендинг, часть 3"),("The team and the footer.","Команда и подвал.")),
  F("rg-blog","Regardify blog page.",("Blog","Блог"),("The blog index.","Список статей блога.")),
  F("rg-event","Regardify event page.",("Event page","Страница события"),("A single event with details.","Отдельное событие с подробностями.")),
  F("rg-mobile-strip","Three Regardify mobile screens: blog, events, team.",("Mobile","Мобильная версия"),("Blog, events and team on a phone.","Блог, события и команда на телефоне.")),
  F("rg-ig-grid","Five square Instagram posts in black, orange and yellow.",("Instagram posts","Посты для Instagram"),("Articles and tips as square cards.","Статьи и советы в виде квадратных карточек."))],
 note=NOTE))
# ---------- Games
pages.append(pg(5,label=LBL(PR),
 lead=("Interface design for three games: a strategy about countries, a puzzle about a virus, and a learning path for a team of warriors.","Интерфейсы для трёх игр: стратегии про страны, головоломки про вирус и обучающего пути для команды воинов."),
 meta=[(CL,SKYL),(DI,("Game UI, product design, illustration","Игровые интерфейсы, продуктовый дизайн, иллюстрация")),(SC,("Screens, levels, cards and icons for each game, plus an admin panel for Warriors Path","Экраны, уровни, карточки и иконки для каждой игры, плюс админ-панель для Warriors Path")),(TL,("Figma","Figma"))],
 glance=[(("Countries","Countries"),("A turn-based strategy in the spirit of Civilization: sign in, choose a region, play cards on a world map and win.","Пошаговая стратегия в духе Civilization: вход, выбор региона, карты на карте мира и победа.")),
         (("Virus","Virus"),("A level-based game, “Memoirs of Coronavirus”, followed by “Adventure of Bibus”, with a new virus character.","Игра с уровнями «Memoirs of Coronavirus», а затем «Adventure of Bibus» с новым персонажем-вирусом.")),
         (("Warriors Path","Warriors Path"),("A gamified learning path for a team: paths, exams, users and configurations, with sign-in through Slack.","Геймифицированный обучающий путь для команды: пути, экзамены, пользователи и настройки, вход через Slack."))],
 sections=[sec(("What I designed","Что я делала"),[("Each game needed its own visual world and a clear interface under it. For Countries it is a dark map with bright regions and cards; for Virus a playful biology look with levels and hints; for Warriors Path a pixel-art bird as the mascot and a calm admin interface for managers.","У каждой игры нужен был свой визуальный мир и понятный интерфейс под ним. Для Countries это тёмная карта с яркими регионами и карточками; для Virus игривая биологическая стилистика с уровнями и подсказками; для Warriors Path пиксельная птица как маскот и спокойный интерфейс администратора для менеджеров."),])],
 figs=[F("cov-case-games","Three game boards in browser frames: Countries, Virus and Warriors Path.",("Overview","Обзор"),("Three games, three visual worlds.","Три игры, три визуальных мира.")),
  F("cg-over","Countries game screens: sign in, choose a region, cards, a world map and a YOU WIN screen.",("Countries","Countries"),("From sign-in to a win screen.","От входа до экрана победы.")),
  F("vg-l1","Virus game level 1 screens.",("Virus, level 1","Virus, уровень 1"),("The first level and its screens.","Первый уровень и его экраны.")),
  F("vg-bibus","Adventure of Bibus screens.",("Adventure of Bibus","Adventure of Bibus"),("A new virus character and its adventure.","Новый персонаж-вирус и его приключение.")),
  F("wp-logo","The Warriors Path pixel-art bird logo.",("Warriors Path logo","Логотип Warriors Path"),("The pixel-art bird mascot.","Пиксельная птица-маскот.")),
  F("wp-web","Warriors Path admin screens: sign in with Slack, paths, exams, users and configurations.",("Warriors Path admin","Админка Warriors Path"),("Paths, exams, users and settings for managers.","Пути, экзамены, пользователи и настройки для менеджеров."))],
 note=NOTE))
cards=[
 card("case-fermalytics","product","x",1800,1100,("Fermalytics","Fermalytics"),("A fermentation app for cheese and beer makers, with its logo and landing.","Приложение для ферментации сыра и пива, с логотипом и лендингом."),[PR,("Branding","Брендинг")]),
 card("case-sky","graphic","x",1800,1100,("SkyLab brand","Бренд SkyLab"),("A day and night landing with line-art illustrations, plus social media.","Дневной и ночной лендинг с линейными иллюстрациями и соцсети."),[GR,WB]),
 card("case-abc-domain","web","x",1800,1100,("ABC Domain","ABC Domain"),("A domain registrar site, app and hand-drawn 404 pages.","Сайт регистратора доменов, приложение и нарисованные от руки страницы 404."),[WB,("Illustration","Иллюстрация")]),
 card("case-regardify-brand","graphic","x",1800,1100,("Regardify brand","Бренд Regardify"),("A logo, landing, mobile screens and Instagram posts for a team events platform.","Логотип, лендинг, мобильные экраны и посты для платформы командных событий."),[GR,WB]),
 card("case-games","product","x",1800,1100,("Games","Игры"),("Interfaces for Countries, Virus and Warriors Path.","Интерфейсы для Countries, Virus и Warriors Path."),[PR,("Game UI","Игровой UI")]),
]
cards=[re.sub(r'<img data-use="x"',f'<img src="{{{{img:cov-{c.split("#")[1].split(chr(34))[0]}}}}}"',c) for c in cards]
s=open(f"{B}/src.html",encoding="utf-8").read()
# insert pages
i=s.index('<!-- ABOUT -->'); s=s[:i]+'\n'.join(pages)+'\n'+s[i:]
# lermontov next -> fermalytics
j=s.index('data-route="case-bardzunq"'); k=s.index('<a class="next" href="#work">',j)
e=s.index('</a>',k)+4
s=s[:k]+f'<a class="next" href="#case-fermalytics"><span class="mono">{T("Next","Далее")}</span><span class="t">{T(*FM)}</span></a>'+s[e:]
# cards: after lermontov card
m=re.search(r'<a class="card"[^>]*href="#case-bardzunq">.*?</a>\n',s,re.S)
assert m
s=s[:m.end()]+'\n'.join(cards)+'\n'+s[m.end():]
# switcher css + js
css='''
.sky-switch{display:flex;gap:8px;margin:0 0 -28px}
.sky-group[hidden]{display:none}
'''
s=s.replace('</style>',css+'</style>',1)
js='''<script>
document.addEventListener("click",function(e){var b=e.target.closest("[data-sky-mode]");if(!b)return;var m=b.getAttribute("data-sky-mode");
document.querySelectorAll("[data-sky-mode]").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});
document.querySelectorAll(".sky-group").forEach(function(g){g.hidden=g.getAttribute("data-sky")!==m});});
</script>
'''
p=s.rindex('</script>')+9
s=s[:p]+'\n'+js+s[p:]
open(f"{B}/src.html","w",encoding="utf-8").write(s)
open(f"{B}/ru_extra.py","a",encoding="utf-8").write("\nRU.update("+repr(RUN)+")\n")
print("ok",len(pages),len(RUN))
