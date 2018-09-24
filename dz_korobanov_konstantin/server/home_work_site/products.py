class Product:
    def __init__(self, name='Без названия', description='Описание отсутствует', sex='Унисекс', color=['Неопределен'],
                 type='Универсальные', size=['Неизвестны'], detailed_description='Детальное описание отсутствует'):
        self.name = name
        self.description = description
        self.sex = sex
        self.color = color
        self.size = size
        self.type = type
        self.detailed_description = detailed_description


adidas_performance = Product(
    name='Adidas performance',
    description='Спортивные кроссовки Adidas Performance',
    sex='Мужские',
    color=['Синий', 'Белый'],
    size=[45, 42, 41, 40],
    detailed_description='Удобные кроссовки, которые подойдут для любых целей. Они достаточно легкие и упругие, для того чтобы в них бегать. В тоже время достаточно теплые для осенних прогулок. Ткань выполнена из инновационного материала, пропускающего воздух.'
)
asics_gel_pulse_9 = Product(
    name='Asics Gel Pulse 9',
    description='Спортивные кроссовки Asics  Gel-Pulse 9 ',
    sex='Мужские',
    color=['Серый + салатовый'],
    type='Беговые',
    size=[46, 44, 42, 41],
    detailed_description='Новая модель разработанная компанией Asics, специально для занятий спортивной хотьбой. В ней реализована усиленная поддержка голеностопа, чтобы во время занятий вы не получили травму'
)
asics_gel_solution_sped = Product(
    name='Asics gel solution speed',
    description='Беговые кроссовки Asics gel solution speed',
    sex='Женские',
    color=['Розовый'],
    type='Беговые',
    size=[40, 38, 36],
    detailed_description='Кроссовки расчитанные на занятия спортивным бегом. Самая мягкая подошпа в мире. Самые легкие во всей линейке беговых кросовок от компании Asics. Имеют 5 наград в том числе, как лучшие беговые кроссовки 2017 года.'
)

nike_flex_contact = Product(
    name='Nike Flex Contact',
    description='Универсальные кроссовки Nike Flex Contact',
    color=['Черный', 'Серый'],
    size=[46, 42, 39],
    detailed_description='Кроссовки Nike Flex Contact подходят для любых видов спорта будь то бег или кроссфит. В них вы везде будете чувствовать себя как дома на мягком и теплом ковре'
)

products_dict = {
    'Adidas_Performance': adidas_performance,
    'Asics_Gel_Pulse_9': asics_gel_pulse_9,
    'asics_gel_solution_speed': asics_gel_solution_sped,
    'Nike_Flex_Contact': nike_flex_contact
}
