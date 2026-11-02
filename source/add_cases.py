import re, html, json
B = "/tmp/claude-0/-home-claude/9b13ca33-0b7c-599b-bc24-b0b02ae6060b/scratchpad/site2"
src = open(f"{B}/src.html", encoding="utf-8").read()
RUN = {}
def T(en, ru):
    RUN[re.sub(r"\s+", " ", en).strip()] = ru
    return html.escape(en, quote=False)
def A(en, ru):  # attribute
    RUN[re.sub(r"\s+", " ", en).strip()] = ru
    return html.escape(en, quote=True)

def fig(img, w, h, alt, t, d, cls="shot", alt_ru=None):
    return (f'    <figure class="fig"><div class="{cls}"><img src="{{{{img:{img}}}}}" width="{w}" height="{h}" alt="{A(alt, alt_ru or alt)}"></div>'
            f'<figcaption><h3>{T(*t)}</h3><p>{T(*d)}</p></figcaption></figure>')

def sec(h, paras=(), steps=(), bullets=()):
    o = f'  <section class="sec"><h2>{T(*h)}</h2>'
    for p in paras: o += f'<p>{T(*p)}</p>'
    if steps:
        o += '<ol class="steps">' + ''.join(f'<li><b style="color:var(--fg)">{T(*a)}</b> {T(*b)}</li>' for a, b in steps) + '</ol>'
    if bullets:
        o += '<ul class="also">' + ''.join(f'<li><b style="color:var(--fg)">{T(*a)}</b> {T(*b)}</li>' for a, b in bullets) + '</ul>'
    return o + '</section>'

def case(route, title, label, lead, meta, glance, sections, figs, note, prev, nxt, aria=None):
    o = f'<div data-route="{route}" class="page" tabindex="-1" aria-label="{A(*(aria or title))}">\n'
    o += f'  <nav class="crumbs" aria-label="Breadcrumb"><a href="#home">Home</a><span aria-hidden="true">/</span><a href="#work">Work</a><span aria-hidden="true">/</span><span aria-current="page">{T(*title)}</span></nav>\n'
    o += f'  <header class="case-hero">\n    <p class="label">{T(*label)}</p>\n    <h1>{T(*title)}</h1>\n    <p class="lead">{T(*lead)}</p>\n    <dl class="meta-row">\n'
    for k, v in meta: o += f'      <div class="meta"><dt>{T(*k)}</dt><dd>{T(*v)}</dd></div>\n'
    o += '    </dl>\n  </header>\n'
    if glance:
        o += '  <div class="glance">\n' + ''.join(f'    <div class="gl"><span class="k">{T(*k)}</span><p>{T(*v)}</p></div>\n' for k, v in glance) + '  </div>\n'
    for s in sections: o += s + '\n'
    o += '  <div class="shots">\n' + '\n'.join(figs) + '\n  </div>\n'
    if note: o += f'  <p class="note" style="margin-top:32px">{T(*note)}</p>\n'
    o += (f'  <nav class="pager" aria-label="More case studies" style="margin-top:64px"><a class="prev" href="#{prev[0]}"><span class="mono">{T("Previous","Назад")}</span><span class="t">{T(*prev[1])}</span></a>'
          f'<a class="next" href="#{nxt[0]}"><span class="mono">{T(*nxt[2]) if len(nxt)>2 else T("Next","Далее")}</span><span class="t">{T(*nxt[1])}</span></a></nav>\n</div>\n')
    return o

def card(route, kind, key, w, h, title, desc, tags):
    t = ''.join(f'<span class="tag{" accent" if i == 0 else ""}">{T(*x)}</span>' for i, x in enumerate(tags))
    return (f'    <a class="card" data-kind="{kind}" href="#{route}"><div class="thumb"><img data-use="{key}" alt="" width="{w}" height="{h}"></div>'
            f'<div><h3>{T(*title)}</h3><p>{T(*desc)}</p></div><div class="tags">{t}</div></a>')

GR = ("Graphic design", "Графический дизайн"); PR = ("Product design", "Продуктовый дизайн"); WB = ("Web design", "Веб-дизайн")
LBL = lambda k: (k[0] + " · Case study", k[1] + " · Кейс")
CL = ("Client", "Клиент"); DI = ("Discipline", "Направление"); SC = ("Scope", "Объём работ"); TL = ("Tools", "Инструменты")
LG = ("Languages", "Языки")
NOTE_CLIENT = ("Client work shown as part of a portfolio.", "Работа для клиента показана в рамках портфолио.")

cases = []; cards = []
order = ["case-penza", "case-papaya", "case-reemtea", "case-reemdried", "case-jigsaw", "case-honey", "case-uxstudy", "case-cvds", "case-10webds", "case-connectai"]
names = {
 "case-merrytour": ("Merry Tour print and event materials", "Печатные и event-материалы Merry Tour"),
 "case-penza": ("Kamenka restaurant menu and cards", "Меню и визитки ресторана «Каменка»"),
 "case-papaya": ("Papaya autumn tasting", "Осенняя дегустация Papaya"),
 "case-reemtea": ("Reem herbal tea labels", "Этикетки травяного чая Reem"),
 "case-reemdried": ("Reem freeze-dried fruit packaging", "Упаковка сублимированных фруктов Reem"),
 "case-jigsaw": ("Singapore from Space jigsaw box", "Коробка пазла «Сингапур из космоса»"),
 "case-honey": ("honey.am website", "Сайт honey.am"),
 "case-uxstudy": ("UX laws, a LinkedIn study", "Законы UX: серия для LinkedIn"),
 "case-cvds": ("A design system for my CV", "Дизайн-система для моего резюме"),
 "case-10webds": ("10Web atomic design system", "Атомарная дизайн-система 10Web"),
 "case-connectai": ("ConnectAI, friend matching", "ConnectAI: подбор друзей с помощью ИИ"),
}
chain = ["case-merrytour"] + order
def pn(i):
    prev = (chain[i - 1], names[chain[i - 1]])
    nxt = (chain[i + 1], names[chain[i + 1]]) if i + 1 < len(chain) else ("work", ("Back to the work index", "Назад к списку работ"), ("All work", "Все работы"))
    return prev, nxt
def add(route, **kw):
    i = chain.index(route); p, n = pn(i); cases.append(case(route, names[route], prev=p, nxt=n, **kw))

# 1 PENZA
add("case-penza", label=LBL(GR),
 lead=("A menu and business cards for a restaurant in Penza, Russia, built around a dark-green leaf pattern and a hummingbird mark.",
       "Меню и визитки для ресторана в Пензе: тёмно-зелёный листовой узор и колибри в качестве знака."),
 meta=[(CL, ("Restaurant Kamenka, Penza, Russia", "Ресторан «Каменка», Пенза")), (DI, ("Graphic design, print", "Графический дизайн, печать")),
       (SC, ("Food menu (front and back), business cards", "Меню блюд (две стороны), визитки")), (LG, ("Russian", "Русский"))],
 glance=None,
 sections=[sec(("The brief and the idea", "Задача и идея"),
   [("The restaurant needed a menu that guests could scan quickly and cards that felt like the same place. The hummingbird in a circle, drawn with leaf line art, became the mark. It repeats on both pieces so they read as one identity.",
     "Ресторану нужно было меню, которое гости быстро просматривают, и визитки в том же стиле. Колибри в круге, нарисованный линиями листьев, стал знаком и повторяется на обеих вещах, чтобы они читались как единая айдентика.")],
   steps=[(("Group by how people order.", "Группировка так, как заказывают."), ("Sections run from starters and salads through soups, mains and grill to pastry, sides and desserts, so the page follows the order of a meal.", "Разделы идут от закусок и салатов к супам, горячему и мангалу, затем мучное, гарниры и десерты: страница повторяет порядок обеда.")),
          (("Let the leaves frame the text.", "Листья обрамляют текст."), ("Dark-green leaf panels sit at the edges and a vertical title marks the menu. The centre stays calm for names and prices.", "Тёмно-зелёные панели с листьями стоят по краям, вертикальный заголовок обозначает меню, а центр остаётся спокойным для названий и цен.")),
          (("Keep the card quiet.", "Спокойная визитка."), ("A near-black field, white type and one half-circle of artwork per side. The name and phone sit on one side, the restaurant and street on the other.", "Почти чёрный фон, белый шрифт и по одной половине круга с рисунком на каждой стороне. Имя и телефон на одной стороне, ресторан и улица на другой."))])],
 figs=[fig("penza-menu-mock", 2000, 1250, "Two menu sheets, front and back, in dark green with leaf panels, shown at an angle on a dark surface.", ("Menu, front and back, in a mockup", "Меню, лицевая и оборотная сторона, в макете"), ("The mockup was added for this portfolio. It shows both sides of the food menu at a slight angle, so the leaf panels and the vertical title read as a set.", "Макет сделан для портфолио. На нём обе стороны меню под небольшим углом, чтобы листовые панели и вертикальный заголовок читались как комплект.")),
       fig("penza-menu-front", 1131, 1600, "Menu front with dark-green leaf panels, a vertical title and sections for starters, salads, soups and mains.", ("Front: starters to mains", "Лицевая сторона: от закусок до горячего"), ("Short rows, generous line spacing and a clear heading for each section.", "Короткие строки, свободный интерлиньяж и понятный заголовок у каждого раздела."), "shot narrow"),
       fig("penza-menu-back", 1131, 1600, "Menu back with sections for grill dishes, pastry, sides and desserts.", ("Back: grill, pastry, sides, desserts", "Оборот: мангал, мучное, гарниры, десерты"), ("The second page continues the same grid, so nothing needs to be relearned.", "Вторая страница продолжает ту же сетку, поэтому ничего не нужно перечитывать заново."), "shot narrow"),
       fig("penza-cards-mock", 1800, 1100, "Two black business cards with a hummingbird in a circle of leaf line art, one with a name and a blurred phone number, one with the restaurant name and street.", ("Business cards", "Визитки"), ("Both sides of the card, in a mockup. The phone number is blurred here on purpose. A real printed card exists, and other versions in gold and green were drawn as options.", "Обе стороны визитки в макете. Номер телефона размыт намеренно. Реальная печатная карта существует, а варианты в золоте и зелени нарисованы как альтернативы."))],
 note=("Mockups were made for this portfolio from the original files.", "Макеты сделаны для портфолио по исходным файлам."))

# 2 PAPAYA
add("case-papaya", label=LBL(GR),
 lead=("An invitation, a menu sheet, score cards and name tags for a pastry tasting event, drawn in soft watercolour flowers.", "Приглашение, лист с десертами, карточки оценки и таблички для дегустации выпечки, нарисованные акварельными цветами."),
 meta=[(CL, ("Papaya, a pastry shop in Yerevan", "Papaya, кондитерская в Ереване")), (DI, ("Graphic design, event print", "Графический дизайн, печать для мероприятий")), (SC, ("Invitation, product sheet, score card, seven name tags", "Приглашение, лист продукции, карточка оценки, семь табличек")), (LG, ("English and Armenian", "Английский и армянский"))],
 glance=[(("Problem", "Задача"), ("Guests at a tasting need to know what they are eating and give feedback without breaking the mood.", "Гостям дегустации нужно понимать, что они пробуют, и оставлять отзыв, не нарушая настроения.")),
         (("Solution", "Решение"), ("One floral language across the invitation, the dessert sheet, the score card and the table tags.", "Один цветочный язык для приглашения, листа десертов, карточки оценки и табличек.")),
         (("Format", "Формат"), ("Autumn Tasting, Saturday 08 November at 14:00.", "Осенняя дегустация, суббота, 8 ноября, 14:00."))],
 sections=[sec(("How the pieces work together", "Как работают вместе материалы"), [],
   steps=[(("Invite.", "Приглашение."), ("Date, time and street first, then a short warm text. The Papaya mark sits above, with flowers framing the page.", "Сначала дата, время и адрес, затем короткий тёплый текст. Знак Papaya сверху, цветы обрамляют страницу.")),
          (("Explain.", "Объяснение."), ("The Autumn’s sweet collection sheet shows seven desserts with a photo and a line in English and Armenian each.", "Лист «Осенняя коллекция» показывает семь десертов: у каждого фото и строка на английском и армянском.")),
          (("Ask.", "Вопрос."), ("The score card gives each dessert three rows, Appearance, Aroma and Taste, rated from 1 to 5. Nothing to write, only circles to mark.", "В карточке оценки у каждого десерта три строки: внешний вид, аромат и вкус по шкале от 1 до 5. Писать не нужно, достаточно отметить цифру.")),
          (("Label.", "Подпись."), ("Small name tags, 336 by 192, sit beside each dessert on the table.", "Небольшие таблички 336 на 192 стоят рядом с каждым десертом на столе."))])],
 figs=[fig("papaya-mock", 1800, 1100, "Four pieces on a pink background: an invitation, a dessert sheet, a score card and a name tag reading Pistachio Tart.", ("The set", "Комплект"), ("The invitation, dessert sheet, score card and a table tag, laid out together as a mockup.", "Приглашение, лист десертов, карточка оценки и табличка, показанные вместе в макете.")),
       fig("papaya-invite", 454, 680, "Invitation reading Saturday 08 November 14:00, 5 Vardanants St., inviting guests to the Autumn Tasting at Papaya.", ("Invitation", "Приглашение"), ("Calm type on a pale field with watercolour flowers. The practical details come first.", "Спокойный шрифт на светлом фоне с акварельными цветами. Практические детали идут первыми."), "shot narrow"),
       fig("papaya-products", 454, 680, "Sheet titled Autumn’s sweet collection with seven desserts, each with a photo and an English and Armenian description.", ("Dessert sheet", "Лист десертов"), ("Seven desserts on a repeating two-column rhythm, with the last one centred as a finale.", "Семь десертов в двухколоночном ритме, последний по центру как финал."), "shot narrow")],
 note=("Event materials shown as part of a portfolio.", "Материалы для мероприятия показаны в рамках портфолио."))

# 3 REEM TEA
add("case-reemtea", label=LBL(GR),
 lead=("Front and back labels for a range of herbal teas, with one colour and one mountain scene for each herb.", "Лицевые и оборотные этикетки для линейки травяных чаёв: у каждой травы свой цвет и свой горный пейзаж."),
 meta=[(CL, ("Reem herbal tea, Armenia", "Reem, травяной чай, Армения")), (DI, ("Packaging and label design", "Дизайн упаковки и этикеток")), (SC, ("Front and back labels for five herbs, in Armenian and English", "Лицевые и оборотные этикетки для пяти трав, на армянском и английском")), (TL, ("Figma", "Figma"))],
 glance=[(("Problem", "Задача"), ("A small range that must look like one brand, while each tea is still easy to find on a shelf.", "Небольшая линейка должна выглядеть как один бренд, а каждый чай при этом легко находить на полке.")),
         (("Solution", "Решение"), ("A fixed layout with a green or colour field, a sun over mountains and the herb name in large capitals.", "Единая раскладка: цветное поле, солнце над горами и название травы крупными заглавными.")),
         (("Result", "Результат"), ("Five herbs in two languages: Wild Thyme, Wild Mint, Green Mint, Oregano and Cephalaria.", "Пять трав на двух языках: чабрец, дикая мята, зелёная мята, орегано и скабиоза."))],
 sections=[sec(("Decisions", "Решения"), [],
   steps=[(("One layout, many colours.", "Одна раскладка, много цветов."), ("The logo, the herb name, the weight and the landscape stay in fixed places. Only the palette changes: green for thyme and mint, purple for oregano, yellow for cephalaria.", "Логотип, название травы, вес и пейзаж всегда на своих местах. Меняется только палитра: зелёная для чабреца и мяты, фиолетовая для орегано, жёлтая для скабиозы.")),
          (("The label as a landscape.", "Этикетка как пейзаж."), ("Layers of mountains and a sun sit at the bottom of each front, so a row of boxes forms a skyline.", "Слои гор и солнце внизу каждой лицевой стороны, поэтому ряд коробок складывается в горизонт.")),
          (("A back that answers questions.", "Оборот, который отвечает на вопросы."), ("The back lists the ingredient, calories, shelf life, nutrition values, a QR link, a barcode and the EAC mark in a clear stack.", "На обороте по порядку указаны состав, калорийность, срок годности, пищевая ценность, QR-ссылка, штрихкод и знак EAC.")),
          (("Armenian and English versions.", "Армянская и английская версии."), ("The Armenian name sits under the English one in the final set, and the file also holds an Armenian-only variant.", "В финальном наборе армянское название стоит под английским, а в файле есть и версия только на армянском."))])],
 figs=[fig("reem-lineup", 1800, 900, "Five tea labels in a row: Wild Thyme and Wild Mint in green, Green Mint in teal, Oregano in purple and Cephalaria in yellow.", ("The range", "Линейка"), ("Five fronts in one row. The colour code makes each herb recognisable at a glance.", "Пять лицевых сторон в ряд. Цветовой код позволяет узнать каждую траву с первого взгляда.")),
       fig("reem-thyme-back", 150, 302, "Back label for Wild Thyme with ingredient, calories, shelf life, nutrition values, a QR code and a barcode.", ("The back label", "Оборотная этикетка"), ("Information in clear bands, on the same colour as the front, with the legally needed marks at the bottom.", "Информация чёткими блоками на том же цвете, что и лицевая сторона, обязательные знаки внизу."), "shot narrow")],
 note=NOTE_CLIENT)

# 4 REEM DRIED
add("case-reemdried", label=LBL(GR),
 lead=("Pouch and label design for freeze-dried fruit: a bright blob of colour per fruit and a single badge that says what the product is.", "Дизайн пакетов и этикеток для сублимированных фруктов: яркое цветное пятно для каждого фрукта и один значок, который объясняет продукт."),
 meta=[(CL, ("Reem, Armenia", "Reem, Армения")), (DI, ("Packaging design", "Дизайн упаковки")), (SC, ("Front art and back labels for seven fruits, stand-up pouch mockup", "Лицевая часть и оборотные этикетки для семи фруктов, макет пакета")), (LG, ("English with Arabic, and Armenian with Russian", "Английский с арабским и армянский с русским"))],
 glance=[(("Problem", "Задача"), ("A product with one ingredient has to look appetising and honest at the same time.", "Продукт из одного ингредиента должен выглядеть аппетитно и честно одновременно.")),
         (("Solution", "Решение"), ("The fruit itself shows through a window. A coloured blob, the fruit name and a Freeze dried badge sit above it.", "Сам фрукт виден через окно. Над ним цветное пятно, название фрукта и значок Freeze dried.")),
         (("Range", "Линейка"), ("Apricot, raspberry, melon, strawberry, blackberry, peach and red currant.", "Абрикос, малина, дыня, клубника, ежевика, персик и красная смородина."))],
 sections=[sec(("Decisions", "Решения"), [],
   steps=[(("Colour carries the flavour.", "Цвет передаёт вкус."), ("Each fruit gets its own blob, yellow for apricot, deep red for strawberry, near-black purple for blackberry, so the range works as a colour wall.", "У каждого фрукта своё пятно: жёлтое у абрикоса, насыщенно-красное у клубники, почти чёрно-фиолетовое у ежевики, и линейка работает как стена цвета.")),
          (("Say the claims with icons.", "Свойства показаны значками."), ("No additives, No gluten and No sugar sit in the bottom corner as three small icons.", "«Без добавок», «Без глютена» и «Без сахара» стоят в нижнем углу тремя маленькими значками.")),
          (("A bilingual back.", "Двуязычный оборот."), ("The label is split into two columns. English runs left to right, Arabic right to left, and both share the same nutrition table, lot number, barcode and QR code.", "Этикетка поделена на две колонки: английский слева направо, арабский справа налево, общая таблица пищевой ценности, номер партии, штрихкод и QR-код."))])],
 figs=[fig("fd-pouch", 1024, 1536, "A stand-up kraft pouch with a transparent window showing dried apricots, a yellow blob reading Apricot, a Freeze dried badge and the Reem logo.", ("Apricot pouch, in a mockup", "Пакет с абрикосом в макете"), ("The art placed on a kraft stand-up pouch. The transparent window lets the product do the selling.", "Макет на крафтовом пакете. Прозрачное окно позволяет продукту продавать себя."), "shot narrow"),
       fig("fd-back", 512, 964, "Back label in English and Arabic with net weight, ingredients, nutrition facts, storage, dates, producer, barcode, QR code and the EAC mark.", ("Back label in two scripts", "Оборотная этикетка на двух письменностях"), ("Dense information in a ruled table with an equal weight for both languages.", "Плотная информация в таблице с линиями, оба языка равны по весу."), "shot narrow")],
 note=NOTE_CLIENT)

# 5 JIGSAW
add("case-jigsaw", label=LBL(GR),
 lead=("A flat box design for a 500-piece jigsaw puzzle made from a satellite image of Singapore.", "Развёртка коробки для пазла из 500 деталей по спутниковому снимку Сингапура."),
 meta=[(CL, ("OnyX Space, Singapore, under the Reem Jigsaw label", "OnyX Space, Сингапур, под маркой Reem Jigsaw")), (DI, ("Packaging design", "Дизайн упаковки")), (SC, ("Box top with sides, box back with specifications, colour options", "Крышка коробки с боковинами, оборот с характеристиками, варианты цвета")), (LG, ("English", "Английский"))],
 glance=[(("Problem", "Задача"), ("Make a puzzle box that feels like a window onto space, not a toy shop product.", "Сделать коробку, которая похожа на окно в космос, а не на товар из магазина игрушек.")),
         (("Solution", "Решение"), ("Deep ocean blues, the image shown with a thin frame and big white type for the facts that matter.", "Глубокие океанские синие, снимок в тонкой рамке и крупный белый шрифт для главных фактов.")),
         (("Facts", "Факты"), ("500 pieces, finished size 61 by 46 cm, age 12+.", "500 деталей, готовый размер 61 на 46 см, от 12 лет."))],
 sections=[sec(("Decisions", "Решения"), [],
   steps=[(("The picture is the hero.", "Главный герой — снимок."), ("The satellite image fills most of the top. Titles sit in the corners and under the picture, so nothing covers the island.", "Спутниковый снимок занимает почти всю крышку. Заголовки стоят в углах и под картинкой, поэтому ничто не закрывает остров.")),
          (("Sides that read on a shelf.", "Боковины читаются на полке."), ("The box edges repeat JIGSAW PUZZLE, 500 PCS and 12+ in large letters, upside down on the far edge so the pile reads from any side.", "На боках крупно повторяется JIGSAW PUZZLE, 500 PCS и 12+, на дальнем краю перевёрнуто, чтобы стопка читалась с любой стороны.")),
          (("A back with a story.", "Оборот с историей."), ("The back tells why the picture is rare, a nearly cloud-free view taken on 24 July 2023, and lists the satellite, resolution, size and pieces.", "Оборот объясняет, почему снимок редкий: почти безоблачный вид от 24 июля 2023 года. Там же указаны спутник, разрешение, размер и число деталей."))])],
 figs=[fig("jig-front", 1600, 1306, "Flat box front: a satellite image of Singapore on a deep blue ocean, with Jigsaw Puzzle, 500 PCS and 12+ lettering on the sides.", ("Box top and sides", "Крышка и боковины коробки"), ("The die-line is shown flat. The image sits inside a frame, with the brand at the top left and the title at the top right.", "Развёртка показана плоской. Снимок лежит в рамке, бренд вверху слева, название вверху справа.")),
       fig("jig-back", 1600, 1306, "Flat box back with the OnyX Space logo, a description of Singapore from space, specifications, a barcode and a QR code.", ("Box back", "Оборот коробки"), ("Three zones: the manufacturer, the story and the specifications, with codes at the bottom.", "Три зоны: производитель, история и характеристики, коды внизу."))],
 note=NOTE_CLIENT)

# 6 HONEY
add("case-honey", label=("Web design · Case study", "Веб-дизайн · Кейс"),
 lead=("A website and online shop for an Armenian honey brand, built around real photography and a warm yellow.", "Сайт и интернет-магазин армянского бренда мёда: настоящие фотографии и тёплый жёлтый цвет."),
 meta=[(CL, ("honey.am, Armenia", "honey.am, Армения")), (DI, ("Web design, e-commerce", "Веб-дизайн, e-commerce")), (SC, ("Home, Products, Gallery, Partners, Contact Us, Shop, cart and checkout", "Главная, продукция, галерея, партнёры, контакты, магазин, корзина и оформление заказа")), (("Screen sizes", "Размеры экранов"), ("1920, 1280, 834 and 390 px", "1920, 1280, 834 и 390 px"))],
 glance=[(("Problem", "Задача"), ("A producer with 26 honeys needs to tell a trust story and also sell online.", "Производителю с 26 видами мёда нужно рассказать историю доверия и ещё продавать онлайн.")),
         (("Solution", "Решение"), ("A short story page, a filterable product catalogue and a shop with a clear add to cart.", "Короткая страница-история, каталог с фильтрами и магазин с понятной кнопкой добавления в корзину.")),
         (("Tone", "Тон"), ("100% natural honey from Armenia, and the line that it is never cooked.", "100% натуральный мёд из Армении и фраза о том, что он никогда не нагревается."))],
 sections=[sec(("What the pages do", "Что делают страницы"), [],
   steps=[(("Home.", "Главная."), ("A bold headline, the pill-shaped photo collage, a statement line, product highlights, partner and certification logos, and three short blocks on how the honey is made.", "Крупный заголовок, коллаж из фото в форме капсул, строка-утверждение, избранная продукция, логотипы партнёров и сертификатов и три коротких блока о том, как делают мёд.")),
          (("Products.", "Продукция."), ("A category panel with counts, tags such as Bear Gift, and cards that show the size and the claims natural and no sugar.", "Панель категорий со счётчиками, теги вроде Bear Gift и карточки с размером и пометками «натуральный» и «без сахара».")),
          (("Online shop.", "Интернет-магазин."), ("Featured products, a sale badge, prices in AMD, filter chips and a favourite star on every card. Cart and checkout screens follow the same cards.", "Избранные товары, значок скидки, цены в драмах, чипы фильтров и звезда избранного на каждой карточке. Корзина и оформление заказа используют те же карточки."))])],
 figs=[fig("honey-home", 488, 1400, "Home page of honey.am with a headline, a collage of honey photographs, a products section, partner logos and a How we work section.", ("Home", "Главная"), ("The full page, scrollable. The photo collage in rounded pills echoes the shape of a honey drop.", "Вся страница с прокруткой. Коллаж из фото в закруглённых капсулах повторяет форму капли мёда."), "shot scroll narrow"),
       fig("honey-products", 725, 1400, "Products page with a category panel, tags and a three-column grid of honey cards.", ("Products", "Продукция"), ("A two-level system: a left filter panel and a card grid. Pagination sits under the grid.", "Двухуровневая система: фильтры слева и сетка карточек. Пагинация под сеткой."), "shot scroll narrow"),
       fig("honey-shop", 602, 1400, "Online Honey Shop page with featured products, filter chips and a grid of product cards with prices in AMD.", ("Online shop", "Интернет-магазин"), ("Filter chips above the grid, price and Add to cart on every card. Empty cards are placeholders for future products.", "Чипы фильтров над сеткой, цена и кнопка «в корзину» на каждой карточке. Пустые карточки — заглушки для будущих товаров."), "shot scroll narrow")],
 note=("Page shows placeholder text and cards in places.", "Местами на странице стоят текст и карточки-заглушки."))

# 7 UX STUDY
RUN_SQ = [("ux-fight1", "FIGHT, part 1: Figma against Adobe, drawn in pixel art."), ("ux-fight2", "FIGHT, part 2."), ("ux-fitts", "Fitts’s law."), ("ux-hick", "Hick’s law."), ("ux-doherty", "Doherty threshold."), ("ux-jakob", "Jakob’s law."), ("ux-aesthetic", "Aesthetic-usability effect.")]
RU_SQ = {"ux-fight1": "FIGHT, часть 1: Figma против Adobe в пиксель-арте.", "ux-fight2": "FIGHT, часть 2.", "ux-fitts": "Закон Фиттса.", "ux-hick": "Закон Хика.", "ux-doherty": "Порог Доэрти.", "ux-jakob": "Закон Якоба.", "ux-aesthetic": "Эффект эстетической привлекательности."}
sq = '    <div class="sq-grid">' + ''.join(f'<figure><img src="{{{{img:{k}}}}}" width="1080" height="1080" alt="{A(a, RU_SQ[k])}"></figure>' for k, a in RUN_SQ) + '</div>'
add("case-uxstudy", label=LBL(GR),
 lead=("A series of square posts for LinkedIn that explain UX laws in a few words and one bold picture.", "Серия квадратных постов для LinkedIn, где законы UX объяснены парой слов и одной яркой картинкой."),
 meta=[(("Channel", "Канал"), ("LinkedIn, then Instagram", "LinkedIn, затем Instagram")), (DI, ("Social graphics, education", "Графика для соцсетей, обучение")), (SC, ("A two-part pixel-art battle between Figma and Adobe, and five UX law posts", "Двухчастный пиксельный бой Figma и Adobe и пять постов о законах UX")), (("Format", "Формат"), ("1080 by 1080 px", "1080 на 1080 px"))],
 glance=None,
 sections=[sec(("Why I made it", "Зачем я это сделала"),
   [("UX laws are easy to quote and hard to remember. Each post keeps one law, one short rule of thumb and one picture, so a reader can take it in during a scroll.", "Законы UX легко цитировать и трудно запомнить. В каждом посте один закон, одно короткое правило и одна картинка, чтобы читатель успел воспринять их за время прокрутки."),
    ("The series opens with a playful two-part FIGHT, with Figma and Adobe drawn as pixel-art fighters, to earn attention before the laws begin.", "Серия начинается с игрового двухчастного FIGHT: Figma и Adobe нарисованы пиксельными бойцами, чтобы привлечь внимание до самих законов.")])],
 figs=[sq], note=None)

# 8 CV DS
add("case-cvds", label=LBL(PR),
 lead=("My CV rebuilt as a small design system: tokens, components and patterns that turn a list of jobs into a page you can explore.", "Моё резюме, собранное как небольшая дизайн-система: токены, компоненты и паттерны, которые превращают список мест работы в страницу, которую можно изучать."),
 meta=[(CL, ("Self-initiated", "Личный проект")), (DI, ("Product design, design systems", "Продуктовый дизайн, дизайн-системы")), (SC, ("Tabs, navigation, accordions, buttons, project cards, list rows", "Вкладки, навигация, аккордеоны, кнопки, карточки проектов, строки списка")), (TL, ("Figma", "Figma"))],
 glance=[(("Problem", "Задача"), ("A PDF CV hides the work. A portfolio site needs reusable pieces, not one-off layouts.", "PDF-резюме прячет работу. Сайту-портфолио нужны повторяемые элементы, а не разовые макеты.")),
         (("Solution", "Решение"), ("Treat the CV like a product: define the components first, then fill them with experience, skills and philosophy.", "Относиться к резюме как к продукту: сначала описать компоненты, потом наполнить их опытом, навыками и философией.")),
         (("Content", "Содержание"), ("Four roles from 2017 to now, four skills lines, four principles and a personal section.", "Четыре роли с 2017 года по сегодня, четыре строки навыков, четыре принципа и личный раздел."))],
 sections=[sec(("Experience as data", "Опыт как данные"),
   [("The same row component holds every role. Dates, title and company stay in fixed places, so the career reads as a timeline.", "Один и тот же компонент строки хранит каждую роль. Даты, должность и компания стоят на своих местах, поэтому карьера читается как временная шкала.")],
   bullets=[(("10Web.", "10Web."), ("Product Designer, March 2021 to December 2024.", "Продуктовый дизайнер, март 2021 — декабрь 2024.")),
            (("SkyLab.", "SkyLab."), ("UX/UI Designer, December 2019 to February 2021.", "UX/UI-дизайнер, декабрь 2019 — февраль 2021.")),
            (("MF5.", "MF5."), ("UI/UX and Graphic Designer, June 2018 to August 2020.", "UI/UX и графический дизайнер, июнь 2018 — август 2020.")),
            (("Freelance.", "Фриланс."), ("UI/UX and Graphic Designer, August 2017 to the present.", "UI/UX и графический дизайнер, август 2017 — настоящее время."))]),
  sec(("Principles shown as components", "Принципы в виде компонентов"),
   [("Design philosophy is four cards: User-centered, Simplicity, Storytelling UI and Growth. A last card, Beyond Design, shows what shapes my taste: explorer and learner, active lifestyle, minimalist mindset and creative thinker.", "Философия дизайна — это четыре карточки: ориентация на пользователя, простота, сторителлинг в интерфейсе и рост. Последняя карточка «За пределами дизайна» показывает, что формирует мой вкус: исследователь и ученик, активный образ жизни, минималистичное мышление и творческий подход.")])],
 figs=[fig("cv-ds-overview", 2000, 1377, "Overview of the CV design system in Figma: tabs, navigation, accordions, buttons, project cards and list rows with job and skill content.", ("The system at a glance", "Система одним взглядом"), ("Components on the left and the finished CV sections on the right, from the same parts.", "Компоненты слева и готовые разделы резюме справа, собранные из одних и тех же деталей."))],
 note=None)

# 9 10WEB DS
add("case-10webds", label=LBL(PR),
 lead=("The updated atomic design system behind the 10Web dashboard: foundations, inputs, buttons, menus and thumbnails documented in one file.", "Обновлённая атомарная дизайн-система дашборда 10Web: основы, поля ввода, кнопки, меню и миниатюры в одном файле."),
 meta=[(CL, ("10Web", "10Web")), (DI, ("Product design, design systems", "Продуктовый дизайн, дизайн-системы")), (SC, ("Typography, inputs, calendar, toggles, checkboxes, buttons, dashboard header, sidebar, left menu, thumbnails, assets", "Типографика, поля ввода, календарь, переключатели, чекбоксы, кнопки, шапка дашборда, сайдбар, левое меню, миниатюры, ассеты")), (TL, ("Figma", "Figma"))],
 glance=[(("Problem", "Задача"), ("A product with dozens of screens drifts apart unless every part has one source.", "Продукт с десятками экранов расползается, если у каждой детали нет одного источника.")),
         (("Solution", "Решение"), ("A documented atomic system: small parts, with states, that compose into menus, headers and cards.", "Документированная атомарная система: небольшие детали с состояниями, из которых собираются меню, шапки и карточки.")),
         (("Scope", "Объём"), ("Foundations, form controls, dashboard parts and assets, each in its own labelled section.", "Основы, элементы форм, части дашборда и ассеты, каждый в своём подписанном разделе."))],
 sections=[sec(("How the system is built", "Как устроена система"), [],
   steps=[(("Foundations first.", "Сначала основы."), ("Open Sans in a nine-step scale from Display 4XL at 36 px with a 50 px line height down to Display XS at 12 px with 18 px, each in four weights.", "Open Sans в девятиступенчатой шкале: от Display 4XL в 36 px со строкой 50 px до Display XS в 12 px со строкой 18 px, в четырёх начертаниях.")),
          (("Every control has every state.", "У каждого элемента есть все состояния."), ("Inputs show default, focus, filled, disabled and error. A password field adds a rules panel with a strength meter. Dropdowns add search, tags and checkboxes.", "Поля ввода показаны в состояниях: обычное, фокус, заполнено, отключено и ошибка. Поле пароля получает панель правил с индикатором надёжности. Выпадающие списки дополнены поиском, тегами и чекбоксами.")),
          (("Buttons in a grid.", "Кнопки в сетке."), ("Filled and outline, with and without an icon, in five widths plus an icon-only square.", "Залитые и контурные, с иконкой и без, пяти ширин плюс квадратная кнопка только с иконкой.")),
          (("Dashboard parts built from the atoms.", "Части дашборда из атомов."), ("The left menu, submenus, header, workspace switcher and website thumbnails reuse the same colours and spacing.", "Левое меню, подменю, шапка, переключатель рабочих пространств и миниатюры сайтов используют те же цвета и отступы."))])],
 figs=[fig("ds10-typo", 2400, 3082, "Typography page of the 10Web design system, showing Open Sans and the Display scale from 4XL to XS in four weights.", ("Typography", "Типографика"), ("One typeface, one scale. Font size and line height are listed next to each step.", "Одна гарнитура, одна шкала. Размер и интерлиньяж указаны рядом с каждой ступенью."), "shot scroll narrow"),
       fig("ds10-buttons", 1380, 500, "Grid of black filled buttons and white outline buttons in five widths, with and without an icon, and square icon-only buttons.", ("Buttons", "Кнопки"), ("A compact grid that shows every size and variant at once.", "Компактная сетка, показывающая все размеры и варианты сразу.")),
       fig("ds10-inputs", 5080, 7747, "Inputs page with text fields, password fields with a strength panel, text areas, dropdowns, search and a calendar, each in several states.", ("Inputs", "Поля ввода"), ("Dense by design. The page is a reference for developers, so every state is on screen.", "Плотная по замыслу. Страница служит справочником для разработчиков, поэтому все состояния видны сразу."), "shot scroll narrow"),
       fig("ds10-thumb", 2732, 2477, "Thumbnail page with website preview cards in several colour variants, performance score badges and Live environment, Multisite and AI Assistant labels.", ("Website thumbnails", "Миниатюры сайтов"), ("Preview cards with a performance score, a WordPress badge, an environment label and a domain pill.", "Карточки предпросмотра с оценкой скорости, значком WordPress, меткой окружения и плашкой домена."))],
 note=NOTE_CLIENT)

# 10 CONNECTAI
add("case-connectai", label=("Product design · On hold", "Продуктовый дизайн · На паузе"),
 lead=("Web and app designs for an Armenian startup that matches people into friendships with AI. The project is on hold, so only part of it was drawn.", "Веб- и приложение-дизайн для армянского стартапа, который подбирает людям друзей с помощью ИИ. Проект на паузе, поэтому нарисована только часть экранов."),
 meta=[(CL, ("ConnectAI, also shown as Social Mirror, an Armenian startup", "ConnectAI, он же Social Mirror, армянский стартап")), (DI, ("Product design, web", "Продуктовый дизайн, веб")), (SC, ("Landing page, sign-up and code screens, profile onboarding, dashboard shell, loading animation", "Лендинг, регистрация и экраны кода, онбординг профиля, оболочка дашборда, анимация загрузки")), (("Status", "Статус"), ("On hold. Matching, chats and the AI helper are not designed yet.", "На паузе. Подбор, чаты и ИИ-помощник пока не нарисованы."))],
 glance=[(("Problem", "Задача"), ("Making friends as an adult is hard. The product asks about you, then proposes people.", "Взрослым трудно заводить друзей. Продукт спрашивает о вас и затем предлагает людей.")),
         (("Solution", "Решение"), ("A friendly landing, a long but calm profile form, and a dashboard with three areas: Overview, Matching and Chats.", "Дружелюбный лендинг, длинная, но спокойная анкета и дашборд с тремя областями: обзор, подбор и чаты.")),
         (("Next", "Дальше"), ("Matching cards, chats and the floating AI button need to be designed when the project restarts.", "Карточки подбора, чаты и плавающую кнопку ИИ нужно будет нарисовать, когда проект возобновится."))],
 sections=[sec(("Decisions", "Решения"), [],
   steps=[(("Blue to violet.", "От синего к фиолетовому."), ("A blue-violet gradient on the headline and the AI button marks everything that is powered by AI. The rest stays black and white.", "Сине-фиолетовый градиент на заголовке и кнопке ИИ отмечает всё, что работает на ИИ. Остальное остаётся чёрно-белым.")),
          (("Three areas, three colours.", "Три области, три цвета."), ("The sidebar uses blue for Overview, violet for Matching and green for Chats, so each area has an identity.", "В сайдбаре обзор синий, подбор фиолетовый, чаты зелёные, поэтому у каждой области своя идентичность.")),
          (("A profile form in small groups.", "Анкета небольшими группами."), ("Basic information, languages, connection preferences and interests are separate blocks with chips, sliders and one custom tag field.", "Основные данные, языки, предпочтения общения и интересы разнесены по блокам с чипами, ползунками и одним полем для своего тега."))])],
 figs=[fig("cai-landing", 738, 1400, "Landing page for Social Mirror with a gradient headline Find Your Perfect Friend Match, statistics, six feature cards and a four-step how it works section.", ("Landing page", "Лендинг"), ("Headline, three numbers, six benefits and four steps. Statistics here are placeholder copy.", "Заголовок, три цифры, шесть преимуществ и четыре шага. Статистика здесь — тестовый текст."), "shot scroll narrow"),
       fig("cai-onboarding", 1440, 1094, "Complete Your Profile form with basic information, language chips, an age range slider and interest chips.", ("Profile onboarding", "Онбординг профиля"), ("The longest screen in the flow. Chips and a slider replace most typing.", "Самый длинный экран потока. Чипы и ползунок заменяют большую часть набора текста.")),
       fig("cai-dash", 1440, 900, "Dashboard shell with a sidebar for Overview, Matching and Chats, an account block, and an empty card layout with a floating AI button.", ("Dashboard shell", "Оболочка дашборда"), ("Navigation and a masonry grid of cards, with the AI button always in reach. Cards are empty because the content is not designed yet.", "Навигация и сетка карточек, кнопка ИИ всегда под рукой. Карточки пустые, потому что содержимое ещё не нарисовано."))],
 note=("Unfinished project, shown as work in progress.", "Незавершённый проект, показан как работа в процессе."))

newpages = "\n".join(cases)

# ---- apply to src
# Merry tour cover
mt_old = '<figure class="fig"><div class="shot"><img src="{{img:mt-cards}}"'
assert mt_old in src
cover_fig = fig("mt-cover", 1800, 1351, "An orange envelope and cards from the Merry Tour set shown as a mockup.", ("The set as a mockup", "Комплект в макете"), ("The new cover image. Printed pieces from the set shown together, in one lit scene.", "Новая обложка. Печатные материалы комплекта, показанные вместе в одной сцене."))
src = src.replace(mt_old, cover_fig.strip() + "\n    " + mt_old, 1)
src = src.replace('<img data-use="mt-banner" alt="" width="1280" height="938">', '<img data-use="mt-cover" alt="" width="1800" height="1351">')
# merrytour pager next -> penza
old_next = '<a class="next" href="#work"><span class="mono">All work</span><span class="t">Back to the work index</span></a></nav>\n</div>\n\n<!-- ABOUT -->'
assert old_next in src
src = src.replace(old_next, f'<a class="next" href="#case-penza"><span class="mono">Next</span><span class="t">{names["case-penza"][0]}</span></a></nav>\n</div>\n\n' + newpages + '\n<!-- ABOUT -->', 1)
RUN[names["case-penza"][0]] = names["case-penza"][1]
# work cards
newcards = "\n".join([
 card("case-penza", "graphic", "penza-cards-mock", 1800, 1100, names["case-penza"], ("A menu and black business cards with a hummingbird mark for a restaurant in Penza.", "Меню и чёрные визитки со знаком-колибри для ресторана в Пензе."), [GR, ("Print", "Печать")]),
 card("case-papaya", "graphic", "papaya-mock", 1800, 1100, names["case-papaya"], ("Invitation, dessert sheet, score card and name tags for a pastry tasting.", "Приглашение, лист десертов, карточка оценки и таблички для дегустации выпечки."), [GR, ("Event", "Мероприятие")]),
 card("case-reemtea", "graphic", "reem-lineup", 1800, 900, names["case-reemtea"], ("A colour-coded label system for five herbal teas, in Armenian and English.", "Система цветных этикеток для пяти травяных чаёв на армянском и английском."), [GR, ("Packaging", "Упаковка")]),
 card("case-reemdried", "graphic", "fd-pouch", 1024, 1536, names["case-reemdried"], ("Pouch and bilingual labels for seven freeze-dried fruits.", "Пакет и двуязычные этикетки для семи сублимированных фруктов."), [GR, ("Packaging", "Упаковка")]),
 card("case-jigsaw", "graphic", "jig-front", 1600, 1306, names["case-jigsaw"], ("A box for a 500-piece puzzle made from a satellite image of Singapore.", "Коробка для пазла из 500 деталей по спутниковому снимку Сингапура."), [GR, ("Packaging", "Упаковка")]),
 card("case-honey", "web", "honey-home", 488, 1400, names["case-honey"], ("A website and online shop for an Armenian honey brand.", "Сайт и интернет-магазин армянского бренда мёда."), [WB, ("E-commerce", "E-commerce")]),
 card("case-uxstudy", "graphic", "ux-fight1", 1080, 1080, names["case-uxstudy"], ("A series of LinkedIn posts that explain UX laws in a picture each.", "Серия постов для LinkedIn, где каждый закон UX объяснён картинкой."), [GR, ("Social", "Соцсети")]),
 card("case-cvds", "product", "cv-ds-overview", 2000, 1377, names["case-cvds"], ("My CV rebuilt as a small design system of reusable components.", "Моё резюме, собранное как небольшая дизайн-система из повторяемых компонентов."), [PR, ("Design system", "Дизайн-система")]),
 card("case-10webds", "product", "ds10-thumb", 2732, 2477, names["case-10webds"], ("The documented atomic design system behind the 10Web dashboard.", "Документированная атомарная дизайн-система дашборда 10Web."), [PR, ("Design system", "Дизайн-система")]),
 card("case-connectai", "product", "cai-dash", 1440, 900, names["case-connectai"], ("Web and app designs for an AI friend-matching startup. On hold.", "Дизайн сайта и приложения для стартапа по подбору друзей с помощью ИИ. На паузе."), [PR, ("On hold", "На паузе")]),
])
m = re.search(r'(    <a class="card" data-kind="graphic" href="#case-merrytour">.*?</a>\n)', src)
assert m
src = src.replace(m.group(1), m.group(1) + newcards + "\n", 1)
src = src.replace("Nine case studies, each told through the real screens.", "Nineteen case studies, each told through the real work.")
src = src.replace("Case studies (9)", "Case studies (19)")
src = src.replace("Luufen, websites and landing pages, Merry Tour</span>", "Luufen, websites and landing pages, Merry Tour, Kamenka, Papaya, Reem tea, Reem freeze-dried, jigsaw, honey.am, UX laws, CV system, 10Web design system, ConnectAI</span>")
# css
css = "\n.sq-grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr)); }\n.sq-grid figure { margin: 0; border: 1px solid var(--line); border-radius: var(--r); overflow: hidden; background: #fff; }\n.sq-grid img { width: 100%; height: auto; display: block; }\n"
src = src.replace(".shot.narrow img {", css + ".shot.narrow img {", 1)
open(f"{B}/src.html", "w", encoding="utf-8").write(src)
RUN.update({"Nineteen case studies, each told through the real work. Filter by discipline.": "Девятнадцать кейсов, каждый показан через реальную работу. Фильтруйте по направлению.",
  "Case studies (19)": "Кейсы (19)", "On hold": "На паузе", "Print": "Печать", "Event": "Мероприятие", "Packaging": "Упаковка", "Social": "Соцсети", "E-commerce": "E-commerce", "Design system": "Дизайн-система",
  "Channel": "Канал", "Format": "Формат", "Status": "Статус", "Range": "Линейка", "Facts": "Факты", "Content": "Содержание", "Tone": "Тон", "Next": "Далее", "Scope": "Объём", "Result": "Результат"})
with open(f"{B}/ru_new.py", "w", encoding="utf-8") as f:
    f.write("RU.update(" + json.dumps(RUN, ensure_ascii=False, indent=0) + ")\n")
print(len(cases), "cases", len(RUN), "strings")
