# 8.10. Отправка сообщений: начните с копии вашей программы из упражнения 8.9.
# Напишите функцию send_messages(), которая выводит каждое сообщение и перемещает его
# в новый список с именем sent_messages. После вызова функции выведите оба списка
# и убедитесь в том, что перемещение прошло успешно.


def send_messages(input, output):
    """Выводит каждое сообщение и перемещает его в новый список"""
    while input:
        sent_messages.append(input.pop())
    return output


# Создаем список сообщений
messages = [
    "Python - простой, универсальный и мощный",
    "Python поддерживает модульность и повторное использование кода",
    "Python - один из самых популярных языков программирования",
    "Python имеет чистый и понятный синтаксис",
    "Python подходит для разработки веб-приложений, научных и инженерных вычислений, анализа данных и многих других "
    "областей"
]

# Создаем пустой список для отправленных сообщений
sent_messages = []

# Вызываем функцию send_messages()
send_messages(messages[:], sent_messages)

# Вывод двух списков
print('Исходные сообщения:', messages, end='\n')
print('Отправленные сообщения:', sent_messages)
