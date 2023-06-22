import json
import datetime


# получение текущей даты
def get_date():
    day = str(datetime.date.today().day)
    month = str(datetime.date.today().month)
    year = str(datetime.date.today().year)
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    return f'{day}.{month}.{year}'


# Чтение файла
def read():
    with open('notes.json', encoding='utf-8') as f:
        all_file = json.load(f)
    return all_file


# Запись новой заметки
def create(name, body):
    newnote = {
        "name": name,
        "body": body,
        "date": get_date(),
        "time": str(datetime.datetime.now().time())[0:5]
    }
    notes = read()
    lastindex = sorted(notes.keys())
    newindex = str(int(lastindex[-1]) + 1)
    notes[newindex] = newnote
    with open('notes.json', 'w', encoding='utf-8') as f:
        json.dump(notes, ensure_ascii=False, fp=f, indent=4)
    return


# Редактирование заметок
def update(index, name, body):
    try:
        notes = read()
        notes[index]["name"] = name
        notes[index]["body"] = body
        notes[index]["date"] = get_date()
        notes[index]["time"] = str(datetime.datetime.now().time())[0:5]
        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump(notes, ensure_ascii=False, fp=f, indent=4)
        print('Информация изменена')
    except:
        print('Заметки не существует')
    return


# Удаление заметок
def delete(index):
    notes = read()
    try:
        del notes[index]

        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump(notes, ensure_ascii=False, fp=f, indent=4)
        print("Заметка удалена")
    except:
        print("Заметки не существует")
    return


# функция выборки по дате
def select_data(date_select):
    notes = read()
    list_del = []
    for keys, values in notes.items():
        if date_select != values['date']:
            list_del.append(keys)
    for i in list_del:
        del notes[i]
    return notes

# Вывод заметки
def printnote(index):
    notes = read()
    try:
        print(f'Идентификатор: {index}\n Заголовок: {notes[index]["name"]}, '
              f'\n Тело заметки: {notes[index]["body"]} ' \
              f'\n Дата создания или изменения заметки: {notes[index]["date"]}, {notes[index]["time"]}')
        return

    except:
        return "Заметки не существует"