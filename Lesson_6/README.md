# Python
Homework for Python

   * [Содержание](#table-of-contents)
      * [Home Work #1](#Home-Work-1)
      * [Home Work #2](#Home-Work-2)
      * [Home Work #3](#Home-Work-3)
      * [Home Work #4](#Home-Work-4)
      * [Home Work #5](#Home-Work-5)
      

## Home Work #1
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).<br>
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.<br>
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, <br>
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке<br>
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.<br>
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.<br>

## Home Work #2
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).<br> 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. <br>
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. <br>
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, <br>
толщиной в 1 см * число см толщины полотна. <br>
Проверить работу метода.<br>
Например: 20м * 5000м * 25кг * 5см = 12500 т<br>

## Home Work #3
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), <br>
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, <br>
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. <br>
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения<br>
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). <br>
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, <br>
проверить значения атрибутов, вызвать методы экземпляров).<br>

## Home Work #4
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). <br>
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).<br>
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. <br>
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. <br>
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) <br>
должно выводиться сообщение о превышении скорости.<br>
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. <br>
Выполните вызов методов и также покажите результат.<br>

## Home Work #5
5. Реализовать класс Stationery (канцелярская принадлежность). <br>
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” <br>
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). <br>
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.<br>
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.<br>