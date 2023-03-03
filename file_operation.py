import json

import Note


def write_file(filename, array):
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        buf_array = []
        for notes in array:
            buf_array.append(Note.Note.to_file(notes))
        json.dump(buf_array, f)


def read_file(filename):
    try:
        array = []
        file = open(f'{filename}.json', 'r', encoding='utf-8')
        notes = json.load(file)
        for n in notes:
            note = Note.Note(
                id=n[0], title=n[1], body=n[2], date=n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array

# def write_file(array, mode):
#     with open("notes.csv", mode='w', encoding='utf-8') as file:
#         file.seek(0)
#     with open("notes.csv", mode=mode, encoding='utf-8') as file:
#         for notes in array:
#             file.write(Note.Note.to_string(notes))
#             file.write('\n')
#
#
# def read_file():
#     try:
#         array = []
#         file = open("notes.csv", "r", encoding='utf-8')
#         notes = file.read().strip().split("\n")
#         for n in notes:
#             split_n = n.split(';')
#             note = Note.Note(
#                 id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
#             array.append(note)
#     except Exception:
#         print('Нет сохраненных заметок...')
#     finally:
#         return array
