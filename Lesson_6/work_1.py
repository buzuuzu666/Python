import time


class TrafficLight:
    _collor = None
    _collors = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 3:
            for el in TrafficLight._collors:
                if el == "Красный":
                    print(el)
                    i += 1
                    time.sleep(7)
                elif el == "Желтый":
                    print(el)
                    i += 1
                    time.sleep(2)
                else:
                    print(el)
                    i += 1
                    time.sleep(10)


traffic = TrafficLight()
traffic.running()
