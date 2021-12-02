FILE_READ = "referat.txt"
FILE_WRITE = "referat2.txt"

with open(FILE_READ, 'r', encoding='utf-8') as fr:
    content = fr.read()

    print(f"Длина файла {len(content)}")
    print(f"Количество слов в файле {len(content.split())}")

    with open(FILE_WRITE, 'w', encoding='utf-8') as fw:
        fw.write(content.replace(".", "!"))
        print(f"Измененные данные сохранены в файл {FILE_WRITE}")
