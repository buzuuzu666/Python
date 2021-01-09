class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} Страт'

    def stop(self):
        return f'{self.name} Стоп'

    def turn_right(self):
        return f'{self.name} поворот направо'

    def turn_left(self):
        return f'{self.name} поворот налево'

    def show_speed(self):
        return f'Скорость {self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля {self.name} = {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую для городского автомобиля'
        else:
            return f'Скорость {self.name} в пределах допустимой '

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочей машины {self.name} = {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает допустимую для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} пренадлежит полиции'
        else:
            return f'Автомобиль {self.name} не пренадлежит полиции'


audi = SportCar(350, 'Черный', 'Audi-Q7', False)
lada = TownCar(36, 'Белый', 'Жигули', False)
Hyundai = WorkCar(70, 'Серый', 'Hyundai', True)
ford = PoliceCar(110, 'Серый',  'Ford', True)
print(Hyundai.turn_left())
print(f'{lada.turn_right()}, тогда {audi.stop()}')
print(f'{Hyundai.go()} тогда скорость равна {Hyundai.show_speed()}')
print(f'{Hyundai.name} это {Hyundai.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{Hyundai.name} полицейская машина? {Hyundai.is_police}')
print(audi.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())