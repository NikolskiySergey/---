# Напишем свой класс
class User:
    # Создадим функцию-конструктор с набором аргумнтов (ФИО, возраст и словарь этих дпнных)
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None
        self.dict = {
            "First name": self.f_name,
            "Middle name": self.m_name,
            "Last name": self.l_name,
            "Age": self.age
        }

    # Создадим функцию, вводящую с клавиатуры ФИО
    def input_fio(self):
        self.f_name = input("Input First name: ")
        self.m_name = input("Input Middle name: ")
        self.l_name = input("Input Last name: ")

    # Создадим функцию, вводящую с клавиатуры возраст
    def input_age(self):
        self.age = input("Input Age: ")

    # Создадим функцию, создающую из ФИО и возраста словарь
    def input_dic(self):
        self.dict = {
            "First name": self.f_name,
            "Middle name": self.m_name,
            "Last name": self.l_name,
            "Age": self.age
        }

    # Создадим функцию, сериализующую данные в строку для вывода на экран
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n" \
               "Last name: {}\n" \
               "Age : {}\n" \
            .format(self.f_name, self.m_name, self.l_name, self.age)

    # Создадим функцию сериализации этого Словаря в файл методом dump модуля json
    def save(self):
        import json
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        filik = input("Введите имя файла: ")
        with open(filik, "w") as f:
            json.dump(self.dict, f)

    # Создадим функцию десериализации данных из файла в Словарь методом load модуля json
    def load(self):
        import json
        # Создаём словарь для записи десериализированной из файла информации:
        drinker = {}
        # Вводим с клавиатуры имя файла для записи нашей сериализированной информации
        filik = input("Введите имя файла: ")
        # Указываем файл:
        with open(filik, "r") as f:
            # Записываем инфу из этого файла в созданный словарь
            drinker = json.load(f)
        return print(drinker)

# Создаём экземпляр класса User - оъект chelovek и поочерёдно вызываем все его методы (т.е. функции внутри класса)
chelovek = User()
chelovek.input_fio()
chelovek.input_age()
chelovek.input_dic()
chelovek.save()
chelovek.load()