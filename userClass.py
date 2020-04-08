# Напишем свой класс
class User:
    # Создадим функцию-конструктор с набором аргумнтов (ФИО и возраст)
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None

    # Создадим функцию, вводящую с клавиатуры ФИО
    def input_fio(self):
        self.f_name = input("Input First name: ")
        self.m_name = input("Input Middle name: ")
        self.l_name = input("Input Last name: ")

    # Создадим функцию, вводящую с клавиатуры возраст
    def input_age(self):
        self.age = input("Input Age: ")

    # Создадим функцию, сериализующую данные в строку для вывода на экран
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n" \
               "Last name: {}\n" \
               "Age : {}\n" \
            .format(self.f_name, self.m_name, self.l_name, self.age)

# Создаём экземпляр класса User - оъект chelovek и поочерёдно вызываем все его методы (т.е. функции внутри класса)
chelovek = User()
chelovek.input_fio()
chelovek.input_age()
print(chelovek.serialize())
