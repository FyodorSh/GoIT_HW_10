from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    value = None


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone=None):
        if phone is not None:
            self.value = phone


class Record:
    name = None
    phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for elem in self.phones:
            if elem.value == phone:
                self.phones.remove(elem)

    def delete_phone_index(self, index):
        self.phones.pop(index)

    def edit_phone(self, old_phone, new_phone):
        for elem in self.phones:
            if elem.value == old_phone:
                elem.value = new_phone

    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.add_phone(phone)


RECORDS = AddressBook()


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
    # RECORDS[contact_name] = contact_phone
    new_record = Record(contact_name, contact_phone)
    RECORDS.add_record(new_record)


@input_error
def change_phone(*args):
    command_list = args[0]
    if not len(command_list) == 3:
        print("Give me name, old and new phone please")
        return

    contact_name = command_list[0]
    contact_old_phone = command_list[1]
    contact_new_phone = command_list[2]
    RECORDS[contact_name].edit_phone(contact_old_phone, contact_new_phone)


@input_error
def delete_phone(*args):
    command_list = args[0]
    if not len(command_list) == 2:
        print("Give me name and phone please")
        return

    contact_name = command_list[0]
    contact_phone = command_list[1]
    RECORDS[contact_name].delete_phone(contact_phone)


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
        print(f"Name: {key} - Phone: {', '.join(phone.value for phone in data.phones)}")


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
    'change': change_phone,
    'phone': phone,
    'show': read_command_list,
    'all': show,
    'good': read_command_list,
    'bye': stop,
    'close': stop,
    'exit': stop,
    'delete': delete_phone
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
    bot()
