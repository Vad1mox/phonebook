def add_new_contact():
    contact = new_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(f"{value}; ")
        file.write('\n')
    return True

def new_data():
    s_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    p_number = input("Введите номер: ")
    contact = {'second_name' : s_name,
               'first_name' : name,
               'middle_name' : m_name,
               'phone_number' : p_number}
    return contact

def find_contact():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data = input("Введите данные искомого контакт: ")
        for line in file:
            if data in line:
                print("\t\t".join(line.split(";")))
                return line
        print("Контакт не обнаружен")

def open_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))

def coppy():
    line = find_contact()
    if line is None:
        return None
    coppy_to = input("Введите название файла, в который нужно скопировать данные: ")
    with open(coppy_to, 'a', encoding='utf-8') as file:        
        file.write(line)

def main():
    isStop = 1
    while isStop != 0:
        input("Нажмите Enter, чтобы продолжить")
        print(f"Выберите что хотите сделать:\n1 найти контакт\n2 добавить контакт\n3 открыть файл\n4 копировать данные в другой файл\n0 выход")
        isStop = int(input("> ")) 
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 3:
            open_contact()
        elif isStop == 4:
            coppy()

main()