# 10.7. Калькулятор: заключите код из упражнения 10.6 в цикл while, чтобы пользователь
# мог продолжать вводить числа, даже если он допустил ошибку и ввел текст вместо числа.

while True:
    try:
        number_1 = input("\nВведите первое число или 'q' для выхода:\n")
        if number_1.lower() == "q" or number_1 == "":
            print("Программа завершена.")
            break
        number_2 = input("Введите второе число или 'q' для выхода:\n")
        if number_2.lower() == "q" or number_2 == "":
            print("Программа завершена.")
            break
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print("Один или оба введенных значения не являются числами."
              "Пожалуйста, попробуйте еще раз.")
    except KeyboardInterrupt:
        exit()
    else:
        sum_numbers = number_1 + number_2
        print(f"Сумма равняется = {sum_numbers}")
