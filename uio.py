# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. создать сам файл:
#  - открываем файл на дозапись

# 2. добавление контакта:
# - запросить/получить у пользователя данные (осуществить проверку на корректность)
# - подготовить форматирование данных к записи
# - открыть файл на дозапись
# - добавить новый контакт в файл

# 3. Вывод данных на экран
# - открыть файл на чтение +++
# - считать текст +++
# - вывод на экран +++

# 4. Поиск контакта:
# - запросить/получить у пользователя данные для поиска
# - открыть файл на чтение
# - произвести поиск контакта
# - вывести на экран

# 5. Интерфейс:
# - создать файл +++
# - вывод на экран меню пользователя +++
# - запросить/получить у пользователя вариант режима работы (1 -4) +++
# - вызов соответствующей функции +++
# - осуществление выхода из программы +++
import os

def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()



def input_name():
    return input("Введите фамилию контакта:").title()

def input_surname():   
    return input("Введите имя контакта:").title()

def input_patronymic():  
    return input("Введите отчество контакта:").title()

def input_phone():
    return input("Введите номер телефона контакта:").title()

def input_address():
    return input("Введите адрес контакта:").title()

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"

def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact_str)    
        
def search_contact():
    print("Варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4", "5"):
        print("Неккоректный ввод, повторите запрос")
        command = input("Выберите вариант поиска: ")

    i_search = int(command)-1    
    search = input("Введите данные для поиска:").lower()
    print()
    
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")            
    
    check_cont = False    
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()         
        if search in lst_contact[i_search]: 
            print(contact_str) 
            print() 
            check_cont = True

    if not check_cont: 
        print("Такого контакта нет.")    

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

def copy_contact(source_file, destination_file, contact_number):
    with open(source_file, "r", encoding="utf-8") as source:
        lines = source.read().rstrip().split("\n\n")

    if 0 < contact_number <= len(lines):
        contact_to_copy = lines[contact_number - 1]
        
        with open(destination_file, "a", encoding="utf-8") as destination:
            destination.write(contact_to_copy + "\n\n")

        print(f"Контакт номер {contact_number} скопирован в файл {destination_file}")
    else:
        print("Некорректный номер контакта")


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command !="5":        
        print("Меню пользователя:\n"
            "1. Вывод данных на экран\n"
            "2. Добавить контакт\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5"):
            print("Неккоректный ввод, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2": 
                add_contact()
            case "3":
                search_contact()
            case "4":
                source_file = "phonebook.txt"
                destination_file = "copied_phonebook.txt"
                contact_number = int(input("Введите номер контакта для копирования: "))
                copy_contact(source_file, destination_file, contact_number)                
            case "5":
                print("Завершение программы")       
        print()

if __name__ == "__main__":
    interface()


