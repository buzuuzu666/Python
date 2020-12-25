def my_func(name, surname, date, city, email, number):
    return " ".join([name, surname, date, city, email, number])


print(my_func(surname='Иванов', name='Иван', date='1996', city='Москва', email='маил@mail.ru',
              number='8-999-300-99-99'))
