exec(open('/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2/add2_head.py').read())
cases=[]
names = {
 "case-connectai": ("ConnectAI, friend matching", "ConnectAI: подбор друзей с помощью ИИ"),
 "case-aiimage": ("AI Image Generator for Elementor", "AI Image Generator для Elementor"),
 "case-10web-more": ("More 10Web projects", "Другие проекты 10Web"),
 "case-treeme": ("Treeme, plant a tree platform", "Treeme: платформа посадки деревьев"),
 "case-tcf-emails": ("Email templates for TCF", "Email-шаблоны для TCF"),
 "case-friends-mvp": ("A platform for making friends, MVP", "Платформа для знакомств и дружбы: MVP"),
}
chain=["case-connectai","case-aiimage","case-10web-more","case-treeme","case-tcf-emails","case-friends-mvp"]
def add(route, **kw):
    i=chain.index(route)
    prev=(chain[i-1],names[chain[i-1]])
    nxt=(chain[i+1],names[chain[i+1]]) if i+1<len(chain) else ("work",("Back to the work index","Назад к списку работ"),("All work","Все работы"))
    cases.append(case(route,names[route],prev=prev,nxt=nxt,**kw))
NOTE2=("Selected screens from the Figma files, shown as part of a portfolio.","Избранные экраны из файлов Figma, показаны в рамках портфолио.")

add("case-aiimage", label=LBL(PR),
 lead=("An image generator inside the Elementor editor, designed before AI image tools were everywhere.","Генератор изображений внутри редактора Elementor, нарисованный до того, как ИИ-генерация стала повсеместной."),
 meta=[(CL,("10Web","10Web")),(DI,("Product design, AI","Продуктовый дизайн, ИИ")),(SC,("A modal with three tools: new image, edit, variations. Credits, ratios, loading and error states","Модальное окно с тремя инструментами: новое изображение, редактирование, вариации. Кредиты, пропорции, состояния загрузки и ошибок")),(TL,("Figma","Figma"))],
 glance=[(("Problem","Задача"),("People building a site in Elementor needed pictures and had to leave the editor to find them.","Тем, кто делает сайт в Elementor, нужны картинки, а за ними приходилось выходить из редактора.")),
         (("Solution","Решение"),("Describe the image, choose a style, a ratio and a number of images, and insert the result in one place.","Опишите картинку, выберите стиль, пропорции и число изображений и вставьте результат в одном месте.")),
         (("Detail","Деталь"),("Previous generations stay in a column on the right, and a credits counter shows what is left.","Прошлые генерации остаются в колонке справа, а счётчик кредитов показывает остаток."))],
 sections=[sec(("Decisions","Решения"),[],steps=[
   (("A dark workspace.","Тёмное рабочее пространство."),("A black canvas keeps the focus on the pictures and makes colour stand out.","Чёрный холст держит внимание на изображениях и делает цвета выразительнее.")),
   (("The prompt on the left, the result on the right.","Запрос слева, результат справа."),("A field with an example, then style, ratio and number of images. The ratio changes the shape of the empty tiles right away, so people see what they will get.","Поле с примером, затем стиль, пропорции и число изображений. Пропорции сразу меняют форму пустых плиток, поэтому видно, что получится.")),
   (("Credits in view.","Кредиты на виду."),("The available credits sit at the top, next to the Use Image button, so cost is never a surprise.","Доступные кредиты стоят сверху рядом с кнопкой Use Image, поэтому стоимость никогда не становится сюрпризом.")),
   (("Guard rails.","Защита от ошибок."),("Dialogs ask before discarding an image, and the flow covers loading, several results, and a single large result.","Диалоги спрашивают подтверждение перед удалением изображения, а сценарий охватывает загрузку, несколько результатов и один крупный результат."))])],
 figs=[fig("aig-cover",1800,1100,"Two views of the dark AI image generator modal in browser frames.",("The generator in a mockup","Генератор в макете"),("Square and landscape ratios of the same modal, shown together.","Квадратные и горизонтальные пропорции одного и того же окна, показанные вместе.")),
       fig("aig-landscape",1280,620,"New image modal with a prompt field, style, ratio set to Landscape, number of images, and four empty landscape tiles.",("Landscape ratio","Горизонтальные пропорции"),("Choosing 16:9 reshapes the preview tiles. The thumbnails on the right keep earlier results.","Выбор 16:9 меняет форму плиток предпросмотра. Миниатюры справа хранят прошлые результаты.")),
       fig("aig-three",1280,620,"New image modal with the square ratio and four empty tiles, and three thumbnails of birds on the right.",("Square ratio","Квадратные пропорции"),("The same panel with the default ratio, before anything is generated.","Та же панель с пропорциями по умолчанию, до генерации."))],
 note=NOTE_CLIENT)

add("case-10web-more", label=LBL(PR),
 lead=("Further work at 10Web beyond the dashboard: backups, pricing, the Elementor AI Builder, AI Ecommerce and landing pages.","Другие работы в 10Web помимо дашборда: бэкапы, тарифы, Elementor AI Builder, AI Ecommerce и лендинги."),
 meta=[(CL,("10Web","10Web")),(("Role","Роль"),("Product Designer, 2021 to 2024. Owner of the AI Ecommerce project","Продуктовый дизайнер, 2021–2024. Владелец проекта AI Ecommerce")),(DI,("Product design, web design","Продуктовый дизайн, веб-дизайн")),(("Worked with","Работала с"),("Elementor, WordPress, WooCommerce","Elementor, WordPress, WooCommerce"))],
 glance=None,
 sections=[sec(("What is in here","Что здесь"),[
   ("AI Ecommerce was the largest of these projects. I owned it end to end, working with Elementor, WordPress and WooCommerce. The overview below shows the file as a map, so you can see how many screens and states it holds.","AI Ecommerce был самым крупным из этих проектов. Я вела его от начала до конца, работая с Elementor, WordPress и WooCommerce. Обзор ниже показывает файл как карту, чтобы было видно, сколько в нём экранов и состояний.")],
   bullets=[(("Backups.","Бэкапы."),("Backup list, schedule dialog, prepare and restore flows, date picker and states.","Список бэкапов, окно расписания, сценарии подготовки и восстановления, выбор даты и состояния.")),
            (("Pricing.","Тарифы."),("Pricing pages with feature comparison, FAQ and variants for desktop, tablet and phone.","Страницы тарифов со сравнением функций, FAQ и вариантами для десктопа, планшета и телефона.")),
            (("Elementor AI Builder.","Elementor AI Builder."),("Onboarding, builder screens and dialogs for creating a site with AI inside Elementor.","Онбординг, экраны конструктора и диалоги для создания сайта с ИИ внутри Elementor.")),
            (("AI Ecommerce.","AI Ecommerce."),("Store setup and management with AI for WooCommerce stores.","Создание и управление магазином с ИИ для магазинов на WooCommerce.")),
            (("Landing pages.","Лендинги."),("Marketing pages for the AI Builder in several sizes.","Маркетинговые страницы AI Builder в нескольких размерах."))])],
 figs=[fig("more10web-cover",1800,1100,"Three file overviews in browser frames: backups, pricing and Elementor AI Builder.",("Three files, one product family","Три файла, одно семейство продуктов"),("A mockup made from the file overviews.","Макет из обзоров файлов.")),
       fig("bk-overview",1600,880,"Overview of the Backups file with backup lists, a calendar, scheduling dialogs and restore dialogs.",("Backups","Бэкапы"),("A map of the flow. Lists, a calendar, scheduling, restore and prepare-to-download dialogs sit side by side.","Карта сценария. Списки, календарь, расписание, восстановление и подготовка к скачиванию стоят рядом.")),
       fig("pricing-overview",1600,754,"Overview of the Pricing file with light and dark pricing pages, feature tables and FAQ at desktop, tablet and phone widths.",("Pricing","Тарифы"),("Pricing pages in light and dark themes with long feature tables.","Страницы тарифов в светлой и тёмной темах с длинными таблицами функций.")),
       fig("eai-overview",948,1400,"Overview of the Elementor AI Builder file with onboarding screens and builder states.",("Elementor AI Builder","Elementor AI Builder"),("Onboarding and builder screens in sections by task.","Онбординг и экраны конструктора по разделам задач."),"shot narrow")],
 note=("File overviews are shown small on purpose. I can add detailed screens for any of these.","Обзоры файлов показаны мелко намеренно. Для любого из проектов можно добавить подробные экраны."))

add("case-treeme", label=LBL(WB),
 lead=("A platform that lets people and companies plant trees in Armenia and follow each tree afterwards. I joined as Product Designer and became Product Director.","Платформа, на которой люди и компании сажают деревья в Армении и потом следят за ростом каждого. Я пришла как продуктовый дизайнер и стала директором по продукту."),
 meta=[(CL,("Treeme, Armenia","Treeme, Армения")),(("Role","Роль"),("Product Designer, then Product Director","Продуктовый дизайнер, затем директор по продукту")),(DI,("Product and web design","Продуктовый и веб-дизайн")),(SC,("Landing page, user dashboard, admin panel, presentations, a Hay Antar admin panel","Лендинг, кабинет пользователя, админ-панель, презентации, админ-панель Hay Antar")),(LG,("Armenian","Армянский"))],
 glance=[(("Problem","Задача"),("Planting a tree is easy to promise and hard to prove. People want to see that their tree exists.","Посадку дерева легко пообещать и трудно подтвердить. Люди хотят видеть, что их дерево существует.")),
         (("Solution","Решение"),("A personal certificate with a QR code, five years of care for each planted tree and a map of the regions.","Личный сертификат с QR-кодом, пять лет ухода за каждым посаженным деревом и карта регионов.")),
         (("Next","Дальше"),("Packages for individuals and for companies, with a project catalogue and a blog.","Пакеты для частных лиц и компаний, каталог проектов и блог."))],
 sections=[sec(("What I designed","Что я проектировала"),[
   ("The home page tells the story in this order: a forest hero, why every planted tree matters, a map of Armenia, how Treeme works, active projects, species of trees, pricing for individuals and companies, and questions.","Главная страница рассказывает историю в таком порядке: лесной первый экран, почему важно каждое дерево, карта Армении, как работает Treeme, активные проекты, породы деревьев, цены для частных лиц и компаний и вопросы."),
   ("Behind the site there is an admin panel with lists, forms and tables, built in the same visual language. The file also holds the flows between pages as a map.","За сайтом стоит админ-панель со списками, формами и таблицами в том же визуальном языке. В файле также есть карта переходов между страницами.")])],
 figs=[fig("treeme-cover",1800,1100,"The Treeme home page hero in a browser frame next to a phone-width view.",("The home page, in a mockup","Главная страница в макете"),("The forest hero, the main promise and two calls to action: corporate packages and packages for individuals.","Лесной первый экран, главное обещание и два призыва к действию: корпоративные пакеты и пакеты для частных лиц.")),
       fig("treeme-hero",1440,1242,"Treeme home page hero with the headline Make Armenia green, two buttons and a card explaining why every planted tree matters.",("Hero and promise","Первый экран и обещание"),("A glass navigation bar and a glass panel over a forest photograph. A short card lists a personal certificate with a QR code, five years of care and the Paris agreement goals for 2050.","Стеклянная навигация и стеклянная панель поверх фото леса. Краткая карточка перечисляет личный сертификат с QR-кодом, пять лет ухода и цели Парижского соглашения до 2050 года.")),
       fig("treeme-landing",266,1400,"The full Treeme landing page in a narrow column.",("The full landing page","Вся страница лендинга"),("The page from top to bottom: map of regions, how it works, projects, tree species, two pricing cards and questions.","Страница сверху вниз: карта регионов, как это работает, проекты, породы деревьев, две карточки тарифов и вопросы."),"shot narrow")],
 note=("Admin panel screens are not shown here yet.","Экраны админ-панели здесь пока не показаны."))

add("case-tcf-emails", label=LBL(GR),
 lead=("Email templates for product launches and seasonal campaigns, built for a team I worked with project by project.","Email-шаблоны для запусков продуктов и сезонных кампаний, сделанные для команды, с которой я работала по проектам."),
 meta=[(CL,("TCF","TCF")),(("Engagement","Формат работы"),("Project-based collaboration","Проектное сотрудничество")),(DI,("Email design","Email-дизайн")),(SC,("Three long-form emails: a holiday follow-up, a welcome email with a discount code, a January campaign","Три длинных письма: рождественское продолжение, приветственное письмо с промокодом, январская кампания"))],
 glance=[(("Problem","Задача"),("Emails for several products had to feel like one brand and still sell each product.","Письма для нескольких продуктов должны выглядеть как один бренд и при этом продавать каждый продукт.")),
         (("Solution","Решение"),("A repeating pattern: a big hero with one button, a short story, a product list with one button each, a footer with social links.","Повторяющаяся схема: крупный первый экран с одной кнопкой, короткая история, список продуктов с кнопкой у каждого, подвал со ссылками на соцсети.")),
         (("Detail","Деталь"),("Each product gets its own colour block, so a long email is easy to scan.","У каждого продукта свой цветной блок, поэтому длинное письмо легко просматривать."))],
 sections=[sec(("Decisions","Решения"),[],steps=[
   (("One hero, one action.","Один первый экран, одно действие."),("Every email opens with a single message and a single button, whether it is Shop now, Claim your offer or Shop smart now.","Каждое письмо открывается одним сообщением и одной кнопкой: Shop now, Claim your offer или Shop smart now.")),
   (("A story before the products.","История перед продуктами."),("Short lines about real moments, such as family game nights, set the mood before the product blocks.","Короткие строки о реальных моментах, например семейных игровых вечерах, задают настроение перед блоками продуктов.")),
   (("Colour per product.","Цвет для каждого продукта."),("Green, blue and orange blocks separate the products and keep the list readable on a phone.","Зелёный, синий и оранжевый блоки разделяют продукты и сохраняют читаемость списка на телефоне."))])],
 figs=[fig("tcf-cover",1800,1100,"Three marketing emails side by side: an orange holiday email, a dark welcome email with a discount code, and a green January email.",("Three emails, one system","Три письма, одна система"),("The top of each email in a mockup.","Верх каждого письма в макете.")),
       fig("email-all",673,1600,"Three full-length marketing emails side by side.",("The full emails","Письма целиком"),("From left to right: the holiday follow-up, the welcome email and the January campaign.","Слева направо: рождественское продолжение, приветственное письмо и январская кампания."),"shot narrow")],
 note=NOTE_CLIENT)

add("case-friends-mvp", label=LBL(PR),
 lead=("My own idea for a platform where adults make friends. I wrote the requirements, mapped the product and drew the MVP onboarding.","Моя собственная идея платформы, где взрослые находят друзей. Я описала требования, нарисовала карту продукта и онбординг MVP."),
 meta=[(CL,("Self-initiated","Личный проект")),(DI,("Product strategy, product design","Продуктовая стратегия, продуктовый дизайн")),(SC,("Requirements, product board, mobile onboarding, sign in, keyboards, welcome dialog","Требования, доска продукта, мобильный онбординг, вход, клавиатуры, приветственное окно")),(TL,("FigJam, Figma","FigJam, Figma"))],
 glance=[(("Problem","Задача"),("Making friends in a city as an adult takes time, and dating apps are not built for it.","Завести друзей во взрослом возрасте в городе долго, а приложения для знакомств для этого не созданы.")),
         (("Solution","Решение"),("A short onboarding that collects hard requirements first and soft matching inputs second, with safety preferences included.","Короткий онбординг: сначала жёсткие требования, затем мягкие параметры подбора, включая предпочтения безопасности.")),
         (("Stage","Этап"),("MVP screens: sign in, basics, interests and a welcome.","Экраны MVP: вход, основные данные, интересы и приветствие."))],
 sections=[sec(("The requirements","Требования"),[
   ("The list that drove the design is in three groups.","Список, который определил дизайн, состоит из трёх групп.")],
   bullets=[(("Basics.","Основное."),("City or neighbourhood, languages, age range and what the person is here for: friends, activity buddies or networking.","Город или район, языки, возрастной диапазон и цель: друзья, партнёры по активностям или нетворкинг.")),
            (("Matching inputs.","Параметры подбора."),("Three to seven interests, energy level, meetup style, availability and boundaries such as alcohol, smoking and women-only meetups.","От трёх до семи интересов, уровень энергии, формат встреч, доступность и границы: алкоголь, курение, встречи только для женщин.")),
            (("Trust and safety.","Доверие и безопасность."),("A photo with optional verification later, and safety preferences such as public places only by default.","Фото с необязательной верификацией позже и предпочтения безопасности, например встречи только в публичных местах по умолчанию."))]),
  sec(("Design decisions","Решения по дизайну"),[],steps=[
   (("One question per screen.","Один вопрос на экран."),("A progress bar and a step label, 1/3 Basics, 2/3 Interests, keep the form short in the mind.","Полоса прогресса и подпись шага, 1/3 Основное, 2/3 Интересы, делают форму короткой в восприятии.")),
   (("The right keyboard for each field.","Нужная клавиатура для каждого поля."),("The name field opens a text keyboard and the date of birth a number pad, with a green action key.","Поле имени открывает текстовую клавиатуру, дата рождения цифровую, с зелёной клавишей действия.")),
   (("Green as the only accent.","Зелёный как единственный акцент."),("One green asterisk mark, green selected states and a green main button on a white page.","Зелёный знак-звёздочка, зелёные выбранные состояния и зелёная главная кнопка на белой странице."))])],
 figs=[fig("mvp-cover",1800,1100,"Four mobile screens in a row: sign in, full name, name with birthday and gender, and interests.",("MVP onboarding","Онбординг MVP"),("Four screens from the flow in phone frames.","Четыре экрана сценария в рамках телефонов.")),
       fig("mvp-screens",1600,1150,"Requirements list on the left and mobile screens: sign in, name, birthday and gender, interests, keyboards and a welcome dialog.",("The file at a glance","Файл целиком"),("Requirements on the left, then the screens and the keyboards used by each field.","Требования слева, затем экраны и клавиатуры для каждого поля."))],
 note=("Unreleased project, shown as an MVP design.","Неопубликованный проект, показан как дизайн MVP."))

np="\n".join(cases)

# ---- Leadership page
L=case("leadership",("Leadership","Лидерство"),("Experience","Опыт"),
 ("Leading teams at a startup summit and a café: people, events, menus and a business to run.","Руководство командами на стартап-саммите и в кафе: люди, мероприятия, меню и бизнес, которым нужно управлять."),
 [(("Seaside Startup Summit","Seaside Startup Summit"),("Team Lead, then Head of Team Leads, since 2018","Тимлид, затем руководитель тимлидов, с 2018 года")),
  (("Café Lermontov","Кафе «Лермонтов»"),("Director for four months, leading the whole staff","Директор в течение четырёх месяцев, руководила всем персоналом")),
  (("Places","Места"),("India, Armenia, United Arab Emirates","Индия, Армения, ОАЭ"))],
 None,
 [sec(("Seaside Startup Summit","Seaside Startup Summit"),[
   ("I started as a Team Lead and grew into Head of Team Leads, so I led the people who lead the teams. The summit takes place in a different place each time, and the work moves with it.","Я начинала тимлидом и выросла до руководителя тимлидов, то есть вела тех, кто ведёт команды. Саммит каждый раз проходит в новом месте, и работа переезжает вместе с ним.")],
   bullets=[(("India.","Индия."),("Rajasthan and Goa.","Раджастхан и Гоа.")),
            (("Armenia.","Армения."),("Lake Sevan.","Озеро Севан.")),
            (("United Arab Emirates.","ОАЭ."),("Ras Al Khaimah and Al Marjan Island.","Рас-эль-Хайма и остров Аль-Маржан."))]),
  sec(("Café Lermontov, Director","Кафе «Лермонтов», директор"),[
   ("For four months I ran a seaside café-restaurant and everything around it: the café, the canteen, the game zone, the grill zone, the beach zone and more. I led the whole staff and carried both the business and the brand.","Четыре месяца я руководила прибрежным кафе-рестораном и всем, что вокруг него: кафе, столовой, игровой зоной, мангальной зоной, пляжной зоной и другими. Я управляла всем персоналом и отвечала и за бизнес, и за бренд.")],
   bullets=[(("Operations.","Операции."),("Staff leadership, product orders and day-to-day running of every zone.","Руководство персоналом, заказы продуктов и ежедневная работа каждой зоны.")),
            (("Events.","Мероприятия."),("Organised events and designed the event screens and visuals.","Организация мероприятий и дизайн экранов и визуалов для них.")),
            (("Design.","Дизайн."),("Two versions of the café menu, a menu for the grill zone, flyers and banners.","Две версии меню кафе, меню мангальной зоны, флаеры и баннеры.")),
            (("Marketing.","Маркетинг."),("Social media posts, an updated Yandex business profile and paid ads.","Посты для соцсетей, обновление бизнес-профиля в Яндексе и платная реклама."))])],
 [fig("ler-menu-mock",2000,1250,"A café menu cover with a seaside window view and the Lermontov logo, next to a menu page with cold starters on a blue watercolour background.",("The café menu, version 2","Меню кафе, версия 2"),("A cover and an inside page in a mockup. Blue-and-white watercolour, ceramic plates and photographs of real dishes. The file also holds a darker first version.","Обложка и внутренняя страница в макете. Сине-белая акварель, керамические тарелки и фото настоящих блюд. В файле есть и более тёмная первая версия.")),
  fig("ler-mangal-mock",2000,1000,"A bright orange grill-zone menu with sections for starters, grill, pizza, rolls, sauces and desserts, and a wide orange pizza banner.",("Menu and banner for the grill zone","Меню и баннер для мангальной зоны"),("A warm orange palette with large black brush headings, shown with a wide pizza banner.","Тёплая оранжевая палитра с крупными чёрными кистевыми заголовками и широким баннером для пиццы.")),
  fig("ler-cover",842,1190,"Menu cover with a window view of a bay, flowers, a boat and the Lermontov café logo with a quill and inkwell.",("Cover","Обложка"),("The cover sets the tone: a sunlit bay seen through a Mediterranean window.","Обложка задаёт тон: залив в солнечном свете, увиденный из окна на средиземноморский лад."),"shot narrow")],
 ("Mockups were made for this portfolio from the original files.","Макеты сделаны для портфолио по исходным файлам."),
 ("about",("About","Обо мне")),("work",("Back to the work index","Назад к списку работ"),("All work","Все работы")))

# ---- apply
src=open(f"{B}/src.html",encoding="utf-8").read()
# connectai next
i=src.index('data-route="case-connectai"'); j=src.index('<a class="next" href="#work">',i)
k=src.index('</a>',j)+4
src=src[:j]+f'<a class="next" href="#case-aiimage"><span class="mono">Next</span><span class="t">{names["case-aiimage"][0]}</span></a>'+src[k:]
RUN[names["case-aiimage"][0]]=names["case-aiimage"][1]
L=L.replace('<a href="#work">Work</a><span aria-hidden="true">/</span>','<a href="#about">About</a><span aria-hidden="true">/</span>',1)
src=src.replace("<!-- ABOUT -->","<!-- LEADERSHIP -->\n"+L+"\n"+np+"\n<!-- ABOUT -->",1)
# jigsaw: cover figure first and thumb
jf=fig("jig-mock",1280,895,"Two jigsaw puzzle boxes standing up on a white surface, the front with a satellite image of Singapore and the back with text and a QR code.",("The box, front and back","Коробка, лицевая и оборотная сторона"),("A mockup of the finished box. The flat artwork follows below.","Макет готовой коробки. Ниже показана плоская развёртка."))
src=src.replace('<figure class="fig"><div class="shot"><img src="{{img:jig-front}}"',jf.strip()+'\n    <figure class="fig"><div class="shot"><img src="{{img:jig-front}}"',1)
src=src.replace('<img data-use="jig-front"','<img data-use="jig-mock"').replace('data-use="jig-mock" alt="" width="1600" height="1306"','data-use="jig-mock" alt="" width="1280" height="895"')
# UX cover + described figures
sq_old=re.search(r'    <div class="sq-grid">.*?</div>\n',src,re.S).group(0)
posts=[("ux-fight1","FIGHT, part 1","FIGHT, часть 1","Figma against Adobe, drawn as pixel-art fighters. The opener of the series.","Figma против Adobe, нарисованные как пиксельные бойцы. Открытие серии."),
 ("ux-fight2","FIGHT, part 2","FIGHT, часть 2","The second round of the pixel-art battle.","Второй раунд пиксельного боя."),
 ("ux-fitts","Fitts’s law","Закон Фиттса","The time to reach a target depends on its distance and its size. Make important targets big and close.","Время, нужное чтобы попасть в цель, зависит от расстояния до неё и её размера. Делайте важные цели крупными и близкими."),
 ("ux-hick","Hick’s law","Закон Хика","The more choices you give, the longer a decision takes. Reduce options and group them.","Чем больше вариантов, тем дольше решение. Сокращайте варианты и группируйте их."),
 ("ux-doherty","Doherty threshold","Порог Доэрти","Answer within about 400 milliseconds and people stay engaged. If a wait is longer, show progress.","Отвечайте примерно за 400 миллисекунд, и человек остаётся вовлечённым. Если ожидание дольше, показывайте прогресс."),
 ("ux-jakob","Jakob’s law","Закон Якоба","People spend most of their time on other products, so they expect yours to work the same way.","Люди проводят большую часть времени в других продуктах, поэтому ждут, что ваш работает так же."),
 ("ux-aesthetic","Aesthetic-usability effect","Эффект эстетической привлекательности","Attractive interfaces are seen as easier to use, and people forgive small problems in them.","Привлекательные интерфейсы кажутся удобнее, и людям легче прощать в них мелкие недочёты.")]
cards_html='    <div class="sq-grid cap">'+''.join(f'<figure><img src="{{{{img:{k}}}}}" width="1080" height="1080" alt="{A(a,b)}"><figcaption><h3>{T(a,b)}</h3><p>{T(d,dr)}</p></figcaption></figure>' for k,a,b,d,dr in posts)+'</div>\n'
cover=fig("ux-cover",1800,1100,"Seven colourful square posts about UX laws arranged on a dark background.",("The series","Серия"),("All seven square posts together.","Все семь квадратных постов вместе."))
src=src.replace(sq_old,cover+'\n'+cards_html,1)
src=src.replace('<img data-use="ux-fight1" alt="" width="1080" height="1080">','<img data-use="ux-cover" alt="" width="1800" height="1100">')
# cards on Work
newcards="\n".join([
 card("case-aiimage","product","aig-cover",1800,1100,names["case-aiimage"],("An AI image generator inside the Elementor editor.","ИИ-генератор изображений внутри редактора Elementor."),[PR,("AI","ИИ")]),
 card("case-10web-more","product","more10web-cover",1800,1100,names["case-10web-more"],("Backups, pricing, Elementor AI Builder, AI Ecommerce and landing pages.","Бэкапы, тарифы, Elementor AI Builder, AI Ecommerce и лендинги."),[PR,("10Web","10Web")]),
 card("case-treeme","web","treeme-cover",1800,1100,names["case-treeme"],("A platform for planting and tracking trees in Armenia: site, dashboard and admin panel.","Платформа посадки и отслеживания деревьев в Армении: сайт, кабинет и админ-панель."),[WB,("Product Director","Директор по продукту")]),
 card("case-tcf-emails","graphic","tcf-cover",1800,1100,names["case-tcf-emails"],("Long-form email templates for product launches and seasonal campaigns.","Длинные email-шаблоны для запусков продуктов и сезонных кампаний."),[GR,("Email","Email")]),
 card("case-friends-mvp","product","mvp-cover",1800,1100,names["case-friends-mvp"],("My idea for a platform to make friends: requirements, flows and MVP screens.","Моя идея платформы для поиска друзей: требования, сценарии и экраны MVP."),[PR,("Own idea","Своя идея")]),
 card("leadership","product","ler-menu-mock",2000,1250,("Leadership: Summit and Café Lermontov","Лидерство: саммит и кафе «Лермонтов»"),("Team Lead and Head of Team Leads at Seaside Startup Summit, and Director of a seaside café.","Тимлид и руководитель тимлидов на Seaside Startup Summit и директор прибрежного кафе."),[("Leadership","Лидерство"),("Experience","Опыт")]),
])
m=re.search(r'(    <a class="card" data-kind="product" href="#case-connectai">.*?</a>\n)',src)
assert m
src=src.replace(m.group(1),m.group(1)+newcards+"\n",1)
src=src.replace("Case studies (19)","Case studies (25)").replace("Nineteen case studies,","Twenty-five case studies,")
src=src.replace(".sq-grid img {",".sq-grid.cap { grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); }\n.sq-grid figcaption { padding: 14px 16px 18px; display: grid; gap: 6px; }\n.sq-grid figcaption h3 { font-size: 1.05rem; }\n.sq-grid figcaption p { color: var(--muted); font-size: .95rem; }\n.sq-grid img {",1)
open(f"{B}/src.html","w",encoding="utf-8").write(src)
RUN.update({"Twenty-five case studies, each told through the real work. Filter by discipline.":"Двадцать пять кейсов, каждый показан через реальную работу. Фильтруйте по направлению.","Case studies (25)":"Кейсы (25)","Role":"Роль","Worked with":"Работала с","Engagement":"Формат работы","Detail":"Деталь","Stage":"Этап","Places":"Места","The series":"Серия","Leadership":"Лидерство","Experience":"Опыт","Product Director":"Директор по продукту","Own idea":"Своя идея","10Web":"10Web","AI":"ИИ","Email":"Email","Previous":"Назад"})
open(f"{B}/ru_new2.py","w",encoding="utf-8").write("RU.update("+json.dumps(RUN,ensure_ascii=False)+")\n")
print(len(cases),len(RUN))
