def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Данного файла нет в данной директории!")
    else:
        #
        words = contents.split()
        nuw_words = len(words)
        print(f"{filename} {nuw_words}")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']

for filename in filenames:
    count_words(filename)
