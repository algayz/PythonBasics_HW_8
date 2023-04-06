def menu():                                
    print("\t Выберите операцию, которую хотите осуществить:")
    print()
    print("1 - Просмотреть все контакты")
    print("2 - Поиск контакта")
    print("3 - Изменить контракт")
    print("4 - Добавить контакт")
    print("5 - Удалить контакт")
    print("0 - Покинуть программу")
    print()
    isCorrect = False
    while not isCorrect:
        try:
            while not isCorrect:
                option = int(input('Ваш выбор: '))
                if option < 0 or option > 5:
                    print("Число должно быть от 0 до 5")
                else:
                    isCorrect = True
        except ValueError:
            print("Это не число!")
            option = 0
    return option

# Подпрограмма запуска модулей:

def selection():            
    isFinish = False
    while not isFinish:
        select = menu()
        print("Ваш выбор - ", select)
        if select == 1:
            print("Запускаю модуль просмотра данных")
            show_all()
        elif select == 2:
            print("Запускаю модуль поиска контакта")
            search_data()
        elif select == 3:
            print("Запускаю модуль изменения контакта")
            change_data()
        elif select == 4:
            print("Запускаю модуль добавления контакта")
            add_record()
        elif select == 5:
            print("Запускаю модуль удаления контакта")
            delete_record()
        else:
            isFinish = True
    print("Работа программы закончена. Спасибо")

# Модуль считывания данных из файла в список:

def read_data():                            
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = list(map(lambda record: record[:-1].split(';'), data))
        file.close()
    return data

def show_all():
    data = read_data()
    screen_result(data)

def screen_result(data):
    header_line = ('ID', 'Фамилия', 'Имя', 'Отчество', 'Телефон')
    print('___________________________________________________________________________________')
    print()
    print('\t\t'.join(map(str, header_line)))
    print('___________________________________________________________________________________')
    print()
    for i in range(len(data)):
        print('\t\t'.join(map(str, data[i])))

def search_data():
    data = read_data()
    print('Если поиск будет по Фамилии - наберите 1, если поиск будет по Имени - наберите 2')
    isCorrect = False
    while not isCorrect:
        try:
            while not isCorrect:
                option = int(input('Ваш выбор: '))
                if option < 1 or option > 2:
                    print("Число должно быть 1 или 2")
                else:
                    isCorrect = True
        except ValueError:
            print("Это не число!")
            option = 0
    search_text = input('Введите имя или фамилию для поиска: ')
    if option == 1:
        filtered_data = list(filter(lambda record: (record[1] == search_text), data))
    else:
        filtered_data = list(filter(lambda record: (record[2] == search_text), data))
    screen_result(filtered_data)

def change_data():
    data = read_data()
    show_all()
    record_ID = input('Введите номер записи для изменения: ')
    i = 0
    while data[i][0] != record_ID:
        i = i + 1
    change_record_index = i
    print(data[change_record_index])
    data[change_record_index][1] = input('Введите изменения в фамилии: ')
    data[change_record_index][2] = input('Введите изменения в имени: ')
    data[change_record_index][3] = input('Введите изменения в отчестве: ')
    data[change_record_index][4] = input('Введите изменения в номере телефона: ')
    print('Изменённая запись:')
    print(data[change_record_index])
    write_data(data)
    
def add_record():
    data = read_data()
    max_record_ID = data[0][0]
    for i in range(len(data)):
        if max_record_ID < data[i][0]:
            max_record_ID = data[i][0]
    new_record_ID = int(max_record_ID) + 1
    new_record = []
    new_record.append(str(new_record_ID))
    new_record.append(input('Введите фамилию: '))
    new_record.append(input('Введите имя: '))
    new_record.append(input('Введите отчество: '))
    new_record.append(input('Введите номер телефона: '))
    data.append(new_record)
    write_data(data)

def delete_record():
    data = read_data()
    show_all()
    record_ID = input('Введите номер записи для удаления: ')
    i = 0
    while data[i][0] != record_ID:
        i = i + 1
    delete_record_index = i
    print(data[delete_record_index])
    Confirmation = int(input('Введите 0 для подтверждения удаления: '))
    if Confirmation == False:
        removed_record = data.pop(delete_record_index)
        print('Элемент удалён: ', removed_record)
    else:
        print('Элемент не удалён')
    write_data(data)

# Модуль записи данных в файл:
 
def write_data(data):                           
    with open('fio.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            file.writelines(';'.join(data[i]))
            file.writelines('\n')
        file.close()

def main():
    print('\n' * 100)
    print("\t\t ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print()
    selection()

if __name__ == '__main__':
    main()