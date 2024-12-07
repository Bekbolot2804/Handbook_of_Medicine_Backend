from django.shortcuts import render
from datetime import date

data = {'services': [
            { 'id': 1, 
             'src_road': 'http://localhost:9000/miniolab1/image/1.png',
             'htitle': 'Как делать сердечно-легочную реанимацию', 
             'title': 'Иногда проведение сердечно-легочной реанимации позволяет спасти жизнь человеку, пока едет скорая помощь. Обсудим основные правила проведения СЛР, какие ошибки чаще всего совершают неподготовленные люди и к чему они могут привести',
             'description': 'Каждый день в мире сотни человек умирают от внезапной остановки сердца. Настоящими счастливчиками можно считать тех, с кем рядом оказался человек, владеющий навыками базовой сердечно-легочной реанимации (СЛР). Алгоритм СЛР, который предложил в середине ХХ века австрийский анестезиолог Петер Сафар, включал искусственное дыхание «рот в рот» и непрямой массаж сердца. Современные протоколы СЛР рекомендуют сконцентрировать усилия на массаже сердца.'},
            { 'id': 2, 
             'src_road': 'http://localhost:9000/miniolab1/image/2.png',
             'htitle': 'Как делать искусственное дыхание', 
             'title': 'Бывают ситуации, когда для спасения человеческой жизни счет идет на минуты. Вместе с врачом скорой помощи обсудим, как правильно провести сердечно-легочную реанимацию и выполнить искусственное дыхание.',
             'description': '''Искусственное дыхание — это важная процедура, которая может помочь спасти жизнь в экстренной ситуации. 
1. Убедись в безопасности: Проверь, что место безопасно для оказания помощи. 
2. Проверь реакцию пострадавшего: Потряси его за плечи и спрашивай, слышит ли он тебя.
3. Вызови скорую помощь: Если пострадавший не реагирует, позвони в скорую.
4. Освободи дыхательные пути: Положи пострадавшего на спину, запрокинь его голову, подняв подбородок.
5. Проверь дыхание: Посмотри, прислушайся и ощути движение воздуха на щеке в течение 10 секунд.
6. Начни искусственное дыхание:
    - Закрой нос пострадавшего.
    - Плотно обхвати его губы своими и сделай два спокойных выдоха, чтобы грудная клетка слегка поднялась.
    - Каждый вдох должен длиться около 1 секунды.
7. Переходи к массажу сердца, если нужно: В сочетании с искусственным дыханием применяют непрямой массаж сердца (30 надавливаний на грудную клетку и 2 вдоха).
Примечание: Если ты не обучен или не уверен в своих действиях, лучше сосредоточиться на непрямом массаже сердца и вызвать специалистов.'''},
            {'id': 3, 
             'src_road': 'http://localhost:9000/miniolab1/image/3.png',
             'htitle': 'Как наложить бинт на локоть или колено', 
             'injuries': 'physical',
             'title': 'Травмы локтя и колена, такие какрастяжения и вывихиможно поддерживать с помощью бинта-валика. Чтобы обеспечить эффективную поддержку, слегка согните сустав, а затем наложите бинт восьмеркой. Работайте изнутри наружу верхней поверхности сустава и растягивайте бинт достаточно далеко с каждой стороны, чтобы обеспечить равномерное давление вокруг травмы.',  
             'ht':'Наступил на ржавый гвоздь', 
             'description':'''Что делать
Поддерживайте травмированную ногу и убедитесь, что она находится в удобном положении и частично согнута.

Расположите конец бинта с внутренней стороны сустава и начните накладывать бинт поверх травмы и вокруг нее.
Сделайте полтора оборота так, чтобы конец бинта зафиксировался и сустав оказался закрыт.
Пропустите бинт на внутреннюю сторону конечности чуть выше сустава. Сделайте оборот вокруг конечности так, чтобы верхняя половина бинта была покрыта.

Пропустите бинт с внутренней стороны верхней части конечности чуть ниже сустава. Затем сделайте один диагональный оборот ниже сустава, чтобы закрыть нижнюю половину бинта.

Продолжайте накладывать повязку по диагонали, выше и ниже места повреждения сустава в виде восьмерки. Расширяйте область повязки каждый раз, когда вы обматываете ее вокруг сустава.

Чтобы закончить повязку, сделайте два прямых оборота вокруг конечности и закрепите конец повязки булавкой или лейкопластырем.

Проверьте кровообращение за пределами повязки сразу же после окончания процедуры и перепроверяйте каждые 10 минут.

Для этого надавите на кожу за пределами края повязки и проверьте, восстановится ли цвет кожи в течение 2 секунд.
При необходимости ослабьте повязку и наложите ее заново.'''},
            {'id': 4, 
             'src_road': 'http://localhost:9000/miniolab1/image/4.png',
             'htitle': 'Проведение первичного медицинского осмотра',
             'title': 'Первичный опрос — это быстрый способ узнать, как лечить любые опасные для жизни состояния, которые могут быть у пострадавшего, в порядке приоритета. Для этого мы можем использовать DRABC: Опасность, Реакция, Дыхательные пути, Дыхание и Кровообращение.', 
             'description':'''Что делать
Бородатый мужчина в одиночку
Опасность. Прежде чем приблизиться к пострадавшему, всегда убеждайтесь, что местность безопасна.

Первичный осмотр — реагирование — проверьте, реагирует ли пострадавший на внешние раздражители или нет.
Реакция. Проверьте, реагирует ли пострадавший или нет. Когда вы приближаетесь к нему, представьтесь и задайте ему вопросы, чтобы увидеть, сможете ли вы получить ответ. Встаньте на колени рядом с его грудью и осторожно потрясите его за плечи, спрашивая: «Вы в порядке?», «Вы можете открыть глаза?».

Если пострадавший открывает глаза или делает другой жест, он реагирует.
Если они никак на вас не реагируют, значит, они невосприимчивы и на них следует обратить внимание как можно быстрее.
Если наблюдается сильное кровотечение (огромное количество крови, льющейся, хлещущей или вырывающейся струей из-за серьезной травмы), его необходимо остановить, прежде чем переходить к дыхательным путям.
Лечите катастрофическое кровотечение, применяя прямое давление на рану , прежде чем управлять дыхательными путями. Позвоните по номеру 999 или 112 для получения экстренной помощи.
Первичный осмотр — дыхательные пути — проверьте, открыты ли и свободны ли дыхательные пути.
Дыхательные пути. Далее необходимо проверить, что дыхательные пути открыты и свободны. Откройте дыхательные пути, положив одну руку на лоб, чтобы запрокинуть голову назад, и двумя пальцами другой руки приподнимите подбородок.

 

Первичный осмотр - дыхание - проверьте, нормально ли дышит пострадавший.
Дыхание. Теперь вам нужно проверить, дышит ли пострадавший нормально. Держите дыхательные пути открытыми, расположите ухо над его ртом и посмотрите вниз на его грудь. Прислушайтесь к звукам дыхания и почувствуйте, чувствуете ли вы его дыхание на своей щеке. Посмотрите, двигается ли его грудь. Делайте это не более 10 секунд.

Пожалуйста, обрати внимание:

В течение первых минут остановки сердца около половины пострадавших будут делать то, что называется «агональным храпом». Они могут открывать рот, вытягивать шею и делать обычно медленные, иногда шумные вдохи. Это не нормальное дыхание и, у пациента без признаков жизни, является признаком остановки сердца.

Если они не реагируют и не дышат нормально, вам необходимо позвонить по номеру 999 или 112 для получения экстренной помощи и начатьСЛРНемедленно. Попросите помощника найти и принести дефибриллятор (АЭД).
Если они реагируют и дыхание нормальное, переходите к кровообращению.
Первичное обследование - кровообращение - проверка на наличие сильного кровотечения
Кровообращение. Как только вы убедитесь, что они дышат нормально, посмотрите и проверьте, нет ли признаковсильное кровотечение.

Если кровотечение сильное, вам нужно будет остановить и лечить кровотечение, применяя прямое давление на рану. Позвоните по номеру 999 или 112 для получения экстренной помощи.
Если они не реагируют и дышат нормально, но кровотечения нет, поместите их вположение восстановленияи позвоните по номеру 999 или 112 для получения экстренной помощи.
После завершения первичного обследования и лечения всех опасных для жизни состояний вы можете перейти к следующему этапу.вторичный осмотр(обследование с головы до ног).'''},
            {'id': 5, 
             'src_road': 'http://localhost:9000/miniolab1/image/5.png',
             'htitle': 'Проведение вторичного медицинского осмотра', 
             'title': 'Вторичный осмотр представляет собой методическую проверку для оценки пострадавшего, находящегося в сознании, на предмет наличия у него других травм или заболеваний.', 
             'description':'''Что делать
После того, как вы закончилипервичное обследованиеи лечили любые угрожающие жизни состояния, переходите к вторичному обследованию. Задайте пострадавшему и окружающим его людям вопросы о любых инцидентах, которые могли произойти. Ваша цель — узнать больше об истории, признаках и симптомах пострадавшего. Если возможно, запишите их ответы.

Оставьте пострадавшего в найденном положении до тех пор, пока вы не убедитесь, что его можно безопасно переместить в положение, более подходящее для его травмы или заболевания.
История – узнайте больше о истории пострадавшего. Используйте мнемонику AMPLE как простое напоминание. Обратите внимание на любые медицинские предупреждающие украшения, которые могут предоставить информацию об истории болезни или любых аллергиях.

Аллергия – Есть ли у них какие-либо аллергии? Например, на орехи или какие-либо лекарства, такие как пенициллин или аспирин?
Лекарства – принимают ли они какие-либо лекарства?
Предыдущая история болезни – страдают ли они какими-либо заболеваниями, такими как диабет, эпилепсия или болезни сердца? Были ли у них какие-либо травмы или операции?
Последний прием пищи – когда они в последний раз ели или пили?
История событий – что и где произошло? Инцидент произошел из-за болезни или несчастного случая? Спросите любого человека поблизости, что произошло, и поищите любые подсказки, которые могут дать вам больше информации.
Признаки  – посмотрите, послушайте, пощупайте и понюхайте любые признаки травмы, такие как отек, деформация, кровотечение, изменение цвета или необычные запахи. При проверке всегда следует сравнивать травмированную сторону тела с неповрежденной. Могут ли они выполнять обычные функции, такие как стояние или движение конечностей? Во время проверки отмечайте любые поверхностные травмы, которые нужно лечить после завершения осмотра.

Симптомы  – задайте пострадавшему короткие, простые вопросы о любых симптомах и ощущениях, которые он может испытывать. Он должен ответить как можно подробнее. Например, спросите его:

У вас что-нибудь болит?
Где боль?
Когда началась боль?
Можете ли вы описать боль: она постоянная или нерегулярная, острая или тупая?
Усиливается ли боль при движении или дыхании?'''
             },
             {'id': 6, 
              'src_road': 'http://localhost:9000/miniolab1/image/6.png', 
              'htitle': 'Управление сложной ситуацией оказания первой помощи', 
              'title': 'Убедитесь, что вы заботитесь о своем здоровье и будьте бдительны, если вы начинаете чувствовать стресс. Необходим спокойный, внимательный ответ, чтобы вы могли успокоить пострадавшего и узнать от него необходимую информацию.', 
              'description': '''Что делать
Будьте спокойны в своем подходе.

Помните о рисках для себя и окружающих и не подвергайте себя опасности.

Общайтесь спокойно и четко. У некоторых людей могут быть особые потребности или трудности в общении.

Создайте и поддерживайте доверие как со стороны пострадавшего, так и со стороны прохожих. Помните, что люди могут вести себя нехарактерно, когда они напуганы или встревожены тем, что с ними происходит.

В первую очередь лечите самые серьезные, опасные для жизни состояния.

Если вы обеспокоены, немедленно позвоните по номеру 999 или 112 для получения экстренной помощи.

Найдите время для себя после окончания чрезвычайной ситуации, чтобы обсудить случившееся и свои ощущения с кем-то, кому вы доверяете. Нормально испытывать целый спектр эмоций после того, как адреналин успокоится. Обратитесь к врачу, если вы испытываете постоянные беспокойные чувства.'''},
             {'id': 7, 
              'src_road': 'http://localhost:9000/miniolab1/image/7.png', 
              'htitle': 'Как сделать повязку для руки',
              'title': 'Повязка для руки удерживает предплечье в поднятом или горизонтальном положении и может поддерживать травмированную верхнюю часть руки, предплечье и запястье. Повязка также является полезным визуальным предупреждением для других о том, что кто-то получил травму.', 
              'description': '''Что делать
Перевязь для руки — вершина треугольника должна находиться под локтем, а длинная сторона — под рукой.
Попросите пострадавшего поддержать руку другой рукой. Осторожно проведите треугольную повязку под рукой. Острие треугольника должно находиться под локтем травмированной руки. Проведите верхний конец повязки вокруг задней части шеи.

Перевязь для руки — нижний конец загните вверх через предплечье к шее с той же стороны, где находится травма.
Загните нижний конец бинта вверх на предплечье так, чтобы он соединился с верхней частью бинта на плече травмированной стороны.

Повязка на руку — свяжите два конца вместе рифовым узлом.
Завяжите два конца бинта вместе рифовым узлом над ключицей и заправьте свободные концы.

Повязка для руки — отрегулируйте повязку так, чтобы она поддерживала руку до мизинца.
Отрегулируйте повязку так, чтобы она поддерживала руку ребенка до конца мизинца.

Перевязь для руки — перекрутите и заправьте край бинта в область локтя.
Убедитесь, что край повязки у локтя надежно закреплен, скрутив ткань и заправив ее внутрь или закрепив ее английской булавкой.

Повязка на руку — проверьте кровообращение в кончиках пальцев
Проверяйте кровообращение в кончиках пальцев каждые 10 минут. Нажмите на ноготь на пять секунд, пока он не побледнеет, затем отпустите, чтобы посмотреть, вернется ли цвет в течение двух секунд.'''},
             {'id': 8, 
              'src_road': 'http://localhost:9000/miniolab1/image/8.png', 
              'htitle': 'Как надеть маску для лица',
              'title': '''Узнайте, как надевать и снимать хирургическую маску и другие средства индивидуальной защиты (СИЗ) в учреждениях здравоохранения и социальной помощи.''', 
              'description': '''Надевание хирургических масок
Прежде чем надевать маску, убедитесь, что ваши руки чистые: воспользуйтесь спиртосодержащим средством для обработки рук, гелем или тщательно вымойте руки водой с мылом в течение не менее 20 секунд.
Убедитесь, что вы пьете достаточно жидкости и не носите никаких украшений, браслетов, часов или колец с камнями.

Наденьте фартук и убедитесь, что он надежно завязан сзади.

Наденьте хирургическую маску. Если она завязывается сзади, убедитесь, что она надежно завязана на макушке и затылке. Когда она закроет нос, убедитесь, что вы растянули ее, чтобы закрыть рот и подбородок.

Надевайте защитные очки, если есть риск разбрызгивания.

Наденьте нестерильные нитриловые перчатки.

Снятие хирургических масок
Хирургические маски предназначены для одноразового использования, другие СИЗ, такие как перчатки и фартук, следует менять между пациентами.
Снимите перчатки, взявшись за внешнюю часть манжеты перчатки и сняв ее. Держите перчатку в оставшейся руке в перчатке, вставьте палец под нее и снимите вторую перчатку.

Обработайте руки спиртосодержащим средством для обработки рук, гелем или тщательно вымойте руки водой с мылом в течение не менее 20 секунд.

Снимите другие СИЗ, такие как фартук, защелкнув или расстегнув завязки фартука вокруг шеи и позволив ему упасть вперед. При необходимости снимите защитные очки.

Обработайте руки спиртосодержащим средством для обработки рук, гелем или тщательно вымойте руки водой с мылом в течение не менее 20 секунд.

Снимите хирургическую маску.

Тщательно мойте руки водой с мылом не менее 20 секунд.'''},
             {'id': 9, 
              'src_road': 'http://localhost:9000/miniolab1/image/9.png', 
              'htitle': 'Как использовать холодный компресс', 
              'title': '''Что такое холодный компресс?
Охлаждение травмы, например растяжения или ушиба, может помочь уменьшить отек и боль. Существует два типа компрессов: пакеты со льдом и холодные подушечки, которые можно сделать, смочив ткань холодной водой.''', 
              'description': '''Что делать
Холодная подушка
Смочите чистую ткань или фланель в холодной воде. Затем слегка отожмите и сложите в тампон.

Плотно прижмите его к травмированному участку.
Повторно смачивайте ткань каждые пару минут, чтобы она оставалась прохладной.

Не охлаждайте травму более 20 минут.
Пакет со льдом
Используйте упаковку замороженных овощей или частично заполните пластиковый пакет небольшими кубиками льда или колотым льдом. Оберните пакет сухой тканью.

Приложите компресс к травмированному месту и добавьте лед, чтобы охладить его.

Не охлаждайте травму более 20 минут.'''},
             {'id': 10, 
              'src_road': 'http://localhost:9000/miniolab1/image/10.png', 
              'htitle': 'Как использовать дефибриллятор', 
              'title': 'Используя дефибриллятор до приезда скорой помощи, вы можете значительно повысить шансы на выживание. Узнайте, что делать.', 
              'description': '''Что делать
Первая помощь — позвоните по номеру 999 или 112 для экстренной помощи.
После выполненияпервичное обследованиеи вы видите, что кто-то не реагирует и не дышит нормально, попросите помощника позвонить по номеру 999 или 112 и вызвать скорую помощь, пока вы начинаетеСЛР. Попросите помощника найти и принести дефибриллятор, если таковой имеется.

Не оставляйте пострадавшего искать дефибриллятор самостоятельно, а если рядом есть кто-то еще, отправьте его за ним. Консультант по экстренной медицинской помощи 999/112 может подсказать, где находится ближайший дефибриллятор.
Если вы одни, используйте функцию громкой связи на телефоне, чтобы можно было начать сердечно-легочную реанимацию, одновременно разговаривая с диспетчером скорой помощи.
Снятие одежды для АВД
Когда помощник вернется с дефибриллятором, попросите включить его (некоторые будут иметь кнопку включения/выключения, а другие будут включаться при открытии их корпуса). После включения следуйте устным инструкциям дефибриллятора. Ваш помощник должен снять или разрезать одежду, чтобы добраться до обнаженной груди пострадавшего. Высушите грудь, если она мокрая, и положите электроды, как показано, пока вы продолжаете СЛР.

 

Прохожие положили АЭД на грудь женщины
Они должны прикрепить подушечки к груди пострадавшего, удалив подложку. Приложите подушечки в указанных положениях, не прекращая компрессии грудной клетки.

Первая подушечка должна располагаться вверху справа под ключицей.
Вторая подушечка должна располагаться с левой стороны пострадавшего ниже и на одной линии с подмышечной впадиной.
Некоторые подушечки имеют датчик, который помещается под руки массажиста грудной клетки в середине груди. Если у вас есть такие подушечки, вам придется на короткое время прекратить компрессию грудной клетки, чтобы разместить датчик.
Женщина с подключенным АЭД
После того, как электроды будут наложены, дефибриллятор скажет вам прекратить СЛР и проанализировать сердечный ритм. Убедитесь, что никто не касается пострадавшего. Затем он даст ряд визуальных и вербальных подсказок, которым вам следует следовать.

Если дефибриллятор сообщает, что необходим разряд, скажите людям отойти. Дефибриллятор скажет вам, когда нажать кнопку разряда. После подачи разряда дефибриллятор скажет вам продолжать СЛР в течение двух минут, прежде чем он выполнит повторный анализ.
Если дефибриллятор сообщает, что разряд не требуется, продолжайте СЛР в течение двух минут, прежде чем дефибриллятор выполнит повторный анализ.
Некоторые дефибрилляторы полностью автоматизированы и не имеют кнопки разряда. Вместо того, чтобы сказать вам нажать кнопку разряда, они предупредят вас, что собираются подать разряд пациенту, когда они уже подали разряд и, как и полуавтоматический дефибриллятор, когда следует продолжить непрямой массаж сердца.
Женщина с подключенным АЭД
Если пострадавший проявляет признаки восстановления сознания, например, кашляет, открывает глаза или говорит, и начинает нормально дышать, поместите его вположение восстановления. Оставьте дефибриллятор подключенным. Следите за уровнем реакции и дыхания и будьте готовы начатьСЛРеще раз, если необходимо.'''},
             {'id': 11, 
              'src_road': 'http://localhost:9000/miniolab1/image/11.png', 
              'htitle': 'Как накладывать повязку', 
              'title': '''Бинты можно использовать для поддержки травмированных суставов, фиксации повязок и остановки кровотечения.''', 
              'description': '''Что делать
Успокойте их и объясните, что вы собираетесь делать.

Помогите им сесть или лечь в удобное положение.
Перед наложением повязки поддерживайте конечность или травмированную часть тела.
Начните бинтование с передней и травмированной стороны пострадавшего. Наложите повязку плотно, но не слишком туго, чтобы не нарушить кровообращение.

Оставьте пальцы рук и ног открытыми, чтобы было легче контролировать кровообращение.
При наложении бинта на конечность используйте спиральные витки, двигаясь изнутри наружу конечности.

Используйте булавки или липкую ленту для фиксации бинтовых повязок. В противном случае вы можете надежно заправить повязку.

Используйте рифовый узел, чтобы завязать треугольную повязку: правый конец поверх левого и под ним, затем левый конец поверх правого и под ним.

Закончив завязывать повязку, обязательно проверьте кровообращение, нажав на палец руки или ноги пострадавшего в течение пяти секунд, пока он не побледнеет.

Если цвет не восстановится через две секунды, значит, повязка слишком тугая, и вам придется наложить ее более свободно.
Проверяйте циркуляцию каждые 10 минут.'''},
             {'id': 12, 
              'src_road': 'http://localhost:9000/miniolab1/image/12.png', 
              'htitle': 'Как правильно забинтовать руку', 
              'title': 'Если вы повредили руку, вы можете использовать бинт, чтобы зафиксировать повязку на месте или поддержать вывихнутое запястье. Узнайте, что делать.', 
              'description': '''Что делать
Начните с того, что положите конец бинта на внутреннюю сторону запястья, под основание большого пальца. Оберните бинт вокруг запястья дважды.

Затем оберните бинт с внутренней стороны запястья, по диагонали через тыльную сторону ладони до ногтя мизинца. Затем проведите бинт прямо через переднюю часть пальцев.

Проведите бинт по диагонали через тыльную сторону ладони к внешней стороне запястья. Затем оберните его под запястьем.

Повторяйте эту восьмерку, пока наружу не будут выглядывать только кончики пальцев. При обертывании покрывайте только две трети предыдущего слоя, так чтобы с каждым новым слоем вы покрывали треть новой кожи.

Когда вы накроете руку, оберните повязку вокруг запястья дважды и закрепите конец с помощью английской булавки, липкой ленты или заправив его внутрь.

Закончив, проверьте кровообращение. Это можно сделать, нажав ногтем на руку на пять секунд, пока она не побледнеет. Если цвет не вернется в течение двух секунд, повязка слишком тугая, поэтому вам придется ослабить ее и наложить снова. Продолжайте проверять кровообращение каждые 10 минут.'''}
],
'defeats': [
    {
        'id': 1,
        'name': 'Перелом конечностей',
    },
    {
        'id': 2,
        'name': 'Кровотечения',
    },
    {
        'id': 3,
        'name': 'Инсульт',
    },
],
'relations': [
  {
      'id_defeats': 1,
      'id_services': [
          {
            'id': 1,
            'time': 23,
            'comment': 'Выполнять острожно'
          },
          {
            'id': 2,
            'time': 13,
            'comment': 'Выполнять острожно'
          },
          {
            'id': 12,
            'time': 29,
            'comment': 'Выполнять острожно'
          }
      ],
  }
]
}

def GetServices(request):
    input_text = request.GET.get('text', "").lower()
    matched_cards = []
    if input_text:
        for current_text in data['services']:
            if input_text in current_text['htitle'].lower():
                matched_cards.append(current_text)
    else:
        matched_cards = data['services']
    context = {
            'input_text': input_text,
            'services': matched_cards,
            'defeats': data['defeats'],
            'relations': data['relations']
        }
    return render(request, 'services.html', context)


def GetService(request, id):
    service = None
    for current_service in data['services']:
        if current_service['id'] == id:
            service=current_service
            break
    return render(request, 'service.html', service)

def GetAppl(request):
    relations = data['relations']
    services = data['services']
    defeats = data['defeats']

    # Список для хранения объединенных данных
    matched_services = []
    selected_defeats = None

    # Проходим по всем relations
    for relation in relations:
        # Ищем категорию defeats
        selected_defeats = next((o for o in defeats if o['id'] == relation['id_defeats']), None)

        if selected_defeats:
            # Ищем и объединяем связанные заказы
            for id_service_data in relation['id_services']:
                service_id = id_service_data['id']
                matched_service = next((o for o in services if o['id'] == service_id), None)

                if matched_service:
                    # Добавляем дополнительные поля time и comment
                    matched_service = matched_service.copy()  # Создаем копию объекта, чтобы не изменять оригинал
                    matched_service['time'] = id_service_data['time']
                    matched_service['comment'] = id_service_data['comment']

                    # Добавляем в список
                    matched_services.append(matched_service)

    # Формируем context для шаблона
    context = {
        'defeats': selected_defeats,  # Категория (например, 'Перелом конечностей')
        'services': matched_services,    # Объединенные данные заказов
    }

    return render(request, 'application.html', context)
