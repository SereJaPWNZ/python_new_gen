from name_function import get_formatted_name

print("\nВведите 'q' для выхода.")
while True:
    first = input("Введите ваше имя:\n")
    if first.lower() == "q" or first.lower() == "й":
        break
    last = input("Введите вашу фамилию:\n")
    if last.lower() == "q" or last.lower() == "й":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\n\tNeatly formatted name: {formatted_name}.")
