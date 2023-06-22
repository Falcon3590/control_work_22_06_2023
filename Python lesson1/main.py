"""
Функционал:
1. Создание заметок
2. Сохранение заметок
3. Чтение списка заметок
4. Редактирование заметок
5. Удаление заметок
6. Возможномть выборки по дате
7. Вывести на экран выбранную заметку
8. Выводить на экран весь список заметок


Структура заметки:
1. Идентификатор
2. Заголовок
3. Тело заметки
4. Дата создания или изменения заметки

"""

from function import *


def rules():
    print()
    print('Работа с заметками: ')
    print('1. Создание заметки')
    print('2. Чтение списка всех заметок')
    print('3. Редактирование заметки')
    print('4. Удаление заметки')
    print('5. Выборка заметки по дате')
    print('6. Вывод информации о заметке')
    print('7. Выход')


run = True
while run:
    rules()
    action = input("Введите номер дейтсвия:\n")
    if action == '7':
        run = False
    elif action == '1':
        print("Создание новой заметки")
        print("Напишите название заметки:")
        name = input()
        print("Напишите заметку:")
        body = input()
        create(name, body)
    elif action == '2':
        print("Все заметки представлены ниже")
        file = read()  # Вывод в консоль
        for keys, values in file.items():
            print("Идентификатор:", keys, "\n Заголовок:", values["name"], "\n Тело заметки:",
                  values["body"], "\n Дата создания или изменения заметки:", values["date"]+',', values["time"])
    elif action == '3':
        print('Напишите идентификатор изменяемой заметки')
        index1 = input()
        print("Напишите название заметки")
        name1 = input()
        print("Напишите заметку")
        body1 = input()
        update(index1, name1, body1)
    elif action == '4':
        print('Напишите идентификатор изменяемой заметки')
        index2 = input()
        delete(index2)
    elif action == '5':
        print('Напишите дату заметки(-ок)')
        data_sort = input()
        notes = select_data(data_sort)
        if len(notes) == 0:
            print('Заметки не были найдены')
        else:
            for keys, values in notes.items():
                print("Идентификатор:", keys, "\n Заголовок:", values["name"], "\n Тело заметки:",
                      values["body"], "\n Дата создания или изменения заметки:", values["date"]+',', values["time"])
    elif action == '6':
        print('Напишите идентификатор заметки')
        index3 = input()
        printnote(index3)
    else:
        print('Действие не было найдено')