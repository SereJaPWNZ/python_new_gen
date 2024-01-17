filename = "alice.txt"

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
