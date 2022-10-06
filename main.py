# Завдання
# У цій домашній роботі ми продовжимо розвивати нашого віртуального асистента з CLI інтерфейсом.
#
# Наш асистент вже вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи та
# виконуючи потрібні дії. У цьому завданні треба буде попрацювати над внутрішньою логікою асистента, над тим, як
# зберігаються дані, які саме дані і що з ними можна зробити.
#
# Застосуємо для цих цілей об'єктно-орієнтоване програмування. Спершу виділимо декілька сутностей (моделей) з якими
# працюватимемо.
#
# У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий
# набір полів.
#
# Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо
# їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.
#
# Користувач взаємодіє з книгой контактів, додаючи, видаляючи та редагуючи записи. Також користувач повинен мати
# можливість шукати в книзі контактів записи за одному або декількома критеріями (полям).
#
# Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email
# наприклад). Також записи можуть містити декілька полів одного типу (декілька телефонів наприклад). Користувач повинен
# мати можливість додавати/видаляти/редагувати поля у будь-якому записі.
#
# В цій домашній роботі ви повинні реалізувати такі класи:
#
# Клас AddressBook, який успадковується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
# Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
# обов'язкового поля Name.
# Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
# Клас Name, обов'язкове поле з ім'ям.
# Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
# Критерії прийому
# Реалізовано всі класи із завдання.
# Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується
# значення Record.name.value.
# Record зберігає об'єкт Name в окремому атрибуті.
# Record зберігає список об'єктів Phone в окремому атрибуті.
# Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
# AddressBook реалізує метод add_record, який додає Record у self.data.

from collections import UserDict

RECORDS = {}


class AddressBook(UserDict):
    pass



class Field:

    value = ""

    def __init__(self, value):
        self.value = value

class Records:

    def __init__(self, name):
        self.name = name

    def add(self):
        pass

    def delete(self):
        pass

    def edit(self):
        pass


class Name(Field):
    name = ""

# Decorators


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            print("Wrong command")
        except IndexError:
            print("Wrong command")
    return wrapper


# Procedures


def hello():
    print("How can I help you?")


@input_error
def add(*args):
    command_list = args[0]
    if not len(command_list) == 2:
        print("Give me name and phone please")
        return
    contact_name = command_list[0]
    contact_phone = command_list[1]
    RECORDS[contact_name] = contact_phone


@input_error
def change(*args):
    command_list = args[0]
    if not len(command_list) == 2:
        print("Give me name and phone please")
        return
    contact_name = command_list[0]
    contact_phone = command_list[1]
    RECORDS[contact_name] = contact_phone


@input_error
def phone(*args):
    command_list = args[0]
    if not len(command_list) == 1:
        print("Enter user name")
        return

    contact_name = args[0][0]
    print(RECORDS[contact_name])


@input_error
def show():
    for key, data in RECORDS.items():
        print(f"Name: {key} - Phone: {data}")


def stop():
    print("Good bye!")
    quit()


@input_error
def get_handler(command_list):
    return read_command_list(command_list)


def read_command_list(command_list: list):
    command = OPERATIONS[command_list.pop(0).lower()]
    command = read_command_list(command_list) if command == read_command_list else command
    return command


OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show': read_command_list,
    'all': show,
    'good': read_command_list,
    'bye': stop,
    'close': stop,
    'exit': stop
}


def bot():
    while True:
        command = input("Enter command: ")
        command_list = command.split(sep=" ")
        handler = get_handler(command_list)
        if handler is not None:
            if not command_list:
                handler()
            else:
                handler(command_list)


if __name__ == '__main__':

    user_name = Name("John")
    print(user_name.name)

    bot()
