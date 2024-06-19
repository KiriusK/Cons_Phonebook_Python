def work_with_phonebook():
    choice=show_menu()
    fileName='phon.txt'
    phone_book=read_txt(fileName)
    while choice!="9":
        match(choice):
            case("1"):
                print_result(phone_book)
            case("2"):
                last_name=input('Введите фамилию: ')
                print_result(find_by_lastname(phone_book,last_name))
            case("3"):
                number=input('Введите номер: ')
                print_result(find_by_number(phone_book,number))
            case("4"):
                user_data=list()
                user_data.append(input('Введите фамилию: '))
                user_data.append(input('Введите имя: '))
                user_data.append(input('Введите номер: '))
                user_data.append(input('Введите описание: '))
                add_user(phone_book,user_data)
                write_txt(fileName,phone_book)
            case("5"):
                last_name=input('Введите фамилию: ')
                print(change_number(phone_book,last_name))
            case("6"):
                lastname=input('Введите фамилию: ')
                print(delete_by_lastname(phone_book,lastname))
            case("7"):
                rowNum=input("Введите номер строки: ")
                newFile=input("Введите имя файла для копирования")
                copyRow(newFile, rowNum)
            case("8"):
                write_txt(fileName,phone_book)
            case _:
                print("Нет такого пункта, выберите верный пункт меню!")
        choice=show_menu()
        
        
def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента по фамилии\n",
          "3. Найти абонента по номеру телефона\n",
          "4. Добавить абонента в справочник\n",
		  "5. Изменить данные абонента\n",
		  "6. Удалить абонента\n",
		  "7. Копировать строку в другой файл\n",
          "8. Сохранить справочник в текстовом формате\n",
          "9. Закончить работу")
    choice = input()
    return choice
    
    
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            lines=line.split(',')
            lines[-1]=lines[-1][:-1]
            record = dict(zip(fields, lines))
            phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


def print_result(book):
    if isinstance(book,list):
        for e in book:
            for n,m in e.items():
                print(f"{n}{'.'*(25-len(n))}{m}")
            print("-"*50)
    else:
        print("Ничего не найдено!")


def find_by_lastname(book,name):
    res_l=list()
    for e in book:
        if name.lower() in e["Фамилия"].lower():
            res_l.append(e)
    if len(res_l)>0:
        return res_l
    else:
        return -1


def find_by_number(book,number):
    res_l=list()
    for e in book:
        if number in e["Телефон"]:
            res_l.append(e)
    if len(res_l)>0:
        return res_l
    else:
        return -1


def add_user(book,data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, data))
    book.append(record)


def change_number(book,name):
    for e in book:
        if name.lower() in e["Фамилия"].lower():
            while True:
                print("\nВыберите какие данные хотите изменить :\n",
                    "1. Фамилия\n",
                    "2. Имя\n",
                    "3. Телефон\n",
                    "4. Описание\n",
                    "5. Сохранение данных")
                choice=input()
                match(choice):
                    case("1"):
                        e["Фамилия"]=input("Введите новую фамилию: ")
                    case("2"):
                        e["Имя"]=input("Введите новое имя: ")
                    case("3"):
                        e["Телефон"]=input("Введите новый номер телефона: ")
                    case("4"):
                        e["Описание"]=input("Введите новое описание контакта: ")
                    case("5"):
                        return
                    case _:
                        print("Нет таких данных, выберите верный пункт меню!")
        else:
            print("Ничего не найдено!")
            return


work_with_phonebook()










