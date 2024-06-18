def work_with_phonebook():
    choice=show_menu()
    fileName='phon.txt'
    phone_book=read_txt(fileName)
    while choice!="9":
        match(choice):
            case("1"):
                print_result(phone_book)
            case("2"):
                last_name=input('lastname ')
                print(find_by_lastname(phone_book,last_name))
            case("3"):
                number=input('number ')
                print(find_by_number(phone_book,number))
            case("4"):
                user_data=input('new data ')
                add_user(phone_book,user_data)
                write_txt(fileName,phone_book)
            case("5"):
                last_name=input('lastname ')
                new_number=input('new  number ')
                print(change_number(phone_book,last_name,new_number))
            case("6"):
                lastname=input('lastname ')
                print(delete_by_lastname(phone_book,lastname))
            case("7"):
                rowNum=int(input("Введите номер строки: "))
                newFile=input("Введите имя файла для копирования")
                copyRow(newFile, rowNum)
            case("8"):
                write_txt(fileName,phone_book)
            case _:
                print("Нет такого пункта, выберите верный пункт меню")
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
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')






work_with_phonebook()










