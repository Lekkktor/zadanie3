import os

path = './text_files/'

def readfile(path: str):
    files_list = os.listdir(path)
    text = {}
    for some_file in files_list:
        if some_file.rfind('.txt', -4):
            with open(os.path.join(path, some_file), 'r', encoding='utf-8') as file:
                text[some_file] = file.readlines()

    with open('mytext.txt', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(text.items(), key=lambda x: len(x[-1])):
            file.write(file_name)
            file.write(str(len(rows)) + '\n')
            count = 0
            for line in rows:
                count += 1
                file.write(f'Строка номер {count} файла {file_name} {line} \n')

readfile(path)