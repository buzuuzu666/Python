class Road:
    __length = None
    __width = None
    __thickness = None
    __weigth = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def payment(self):
        self.weigth = 25
        self.thickness = 0.05
        outcome = self.__length * self.__width * self.weigth * self.thickness / 10
        print(f"масса асфальта, необходимого для покрытия всего дорожного полотна = {int(outcome)}т")


# Например: 20м * 5000м * 25кг * 5см = 12500 т
a = Road(20000, 5)
a.payment()
