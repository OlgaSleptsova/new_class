class Аnimals:
    food = 'stop eating'
    voice = 'stop speak'
    color = 'white'
    size = 'small'
    age = 0
    weight = 0
    name = 'no name'

    def start_eat(self):
        self.food = 'start eating'

    def stop_eat(self):
        self.food = 'stop eating'

    def start_publish_a_voice(self):
        self.voice = 'start speak'

    def stop_publish_a_voice(self):
        self.voice = 'stop speak'
        pass


class Birds(Аnimals):
    eggs = 'not lay eggs'

    def __init__(self, food, voice, color, weight, name):
        self.food = 'stop eating'
        self.voice = 'stop speak'
        self.color = 'white'
        self.weight = 0
        self.name = 'no name'

    def lay_eggs(self):
        self.eggs = 'lay eggs'

    def stop_lay_eggs(self):
        self.eggs = 'not lay eggs'

    pass


class Сows_and_goats(Аnimals):
    milk = 'no'

    def __init__(self, food, voice, color, weight, name):
        self.food = 'stop eating'
        self.voice = 'stop speak'
        self.color = 'white'
        self.weight = 0
        self.name = 'no name'

    def to_give_milk(self):
        self.milk = 'yes'

    def do_not_give_milk(self):
        self.milk = 'no'

    pass


class Sheeps(Аnimals):
    wool = 'no'

    def __init__(self, food, voice, color, weight, name):
        self.food = 'stop eating'
        self.voice = 'stop speak'
        self.color = 'white'
        self.weight = 0
        self.name = 'no name'

    def cut_hair(self):
        self.wool = 'yes'

    def do_not_cut_hair(self):
        self.wool = 'no'

    pass


goose1 = Birds()
goose1.start_eat()
goose1.lay_eggs()
goose1.name = 'Серый'
goose1.weight = 10

goose2 = Birds()
goose2.start_eat()
goose2.lay_eggs()
goose1.name = 'Белый'
goose1.weight = 20

cow = Сows_and_goats()
cow.start_eat()
cow.to_give_milk()
cow.name = 'Манька'
cow.weight = 50

sheep1 = Sheeps()
sheep1.start_eat()
sheep1.cut_hair()
sheep1.name = 'Барашек'
sheep1.weight = 15

sheep2 = Sheeps()
sheep2.start_eat()
sheep2.cut_hair()
sheep2.name = 'Кудрявый'
sheep2.weight = 14

chicken1 = Birds()
chicken1.start_eat()
chicken1.lay_eggs()
chicken1.name = 'Ко-ко'
chicken1.weight = 4

chicken2 = Birds()
chicken2.start_eat()
chicken2.lay_eggs()
chicken2.name = 'Кукареку'
chicken2.weight = 5

goat1 = Сows_and_goats()
goat1.start_eat()
goat1.to_give_milk()
goat1.name = 'Рога'
goat1.weight = 10

goat2 = Сows_and_goats()
goat2.start_eat()
goat2.to_give_milk()
goat2.name = 'Копыта'
goat2.weight = 11

duck = Birds()
duck.start_eat()
duck.lay_eggs()
duck.name = 'Кряква'
duck.weight = 6
print(duck.weight)
