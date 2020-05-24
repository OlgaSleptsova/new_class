class Animals:
    food = 'stop eating'
    voice = 'stop speak'
    color = 'white'
    size = 'small'
    age = 0
    weight = {}
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


class Birds(Animals):

    def __init__(self, food, voice, color, weight, name, eggs):
        self.food = food
        self.voice = voice
        self.color = color
        self.weight = weight
        self.name = name
        self.eggs = eggs

    def lay_eggs(self):
        self.eggs = 'lay eggs'

    def stop_lay_eggs(self):
        self.eggs = 'not lay eggs'

    def add(self):
        Animals.weight.update({self.name: self.weight})


pass


class СowsAndGoats(Animals):

    def __init__(self, food, voice, color, weight, name, milk):
        self.food = food
        self.voice = voice
        self.color = color
        self.weight = weight
        self.name = name
        self.milk = milk

    def to_give_milk(self):
        self.milk = 'yes'

    def do_not_give_milk(self):
        self.milk = 'no'

    def add(self):
        Animals.weight.update({self.name: self.weight})

    pass


class Sheeps(Animals):

    def __init__(self, food, voice, color, weight, name, wool):
        self.food = food
        self.voice = voice
        self.color = color
        self.weight = weight
        self.name = name
        self.wool = wool

    def cut_hair(self):
        self.wool = 'yes'

    def do_not_cut_hair(self):
        self.wool = 'no'

    def add(self):
        Animals.weight.update({self.name: self.weight})

    pass


goose1 = Birds('stop eating', 'stop speak', 'gray', 10, 'гусь Серый', 'not lay eggs')
goose1.start_eat()
goose1.lay_eggs()
goose1.add()

goose2 = Birds('stop eating', 'stop speak', 'white', 20, 'гусь Белый', 'not lay eggs')
goose2.start_eat()
goose2.lay_eggs()
goose2.add()

cow = СowsAndGoats('stop eating', 'stop speak', 'brown', 50, ' корова Манька', 'no')
cow.start_eat()
cow.to_give_milk()
cow.add()

sheep1 = Sheeps('stop eating', 'stop speak', 'white', 15, 'овца Барашек', 'no')
sheep1.start_eat()
sheep1.cut_hair()
sheep1.add()

sheep2 = Sheeps('stop eating', 'stop speak', 'white', 14, 'овца Кудрявый', 'no')
sheep2.start_eat()
sheep2.cut_hair()
sheep2.add()

chicken1 = Birds('stop eating', 'stop speak', 'gray', 4, 'курица Ко-ко', 'not lay eggs')
chicken1.start_eat()
chicken1.lay_eggs()
chicken1.add()

chicken2 = Birds('stop eating', 'stop speak', 'white', 5, 'курица Кукареку', 'not lay eggs')
chicken2.start_eat()
chicken2.lay_eggs()
chicken2.add()

goat1 = СowsAndGoats('stop eating', 'stop speak', 'gray', 10, 'коза Рога', 'no')
goat1.start_eat()
goat1.to_give_milk()
goat1.add()

goat2 = СowsAndGoats('stop eating', 'stop speak', 'gray', 11, 'коза Копыта', 'no')
goat2.start_eat()
goat2.to_give_milk()
goat2.add()

duck = Birds('stop eating', 'stop speak', 'white', 6, 'утка Кряква', 'not lay eggs')
duck.start_eat()
duck.lay_eggs()
duck.add()

x = max(Animals.weight.values())

for z, y in Animals.weight.items():
    if y == x:
        print(f'Самое тяжелое животное -{z}')

print(f'Вес всех животных - {sum(Animals.weight.values())}')