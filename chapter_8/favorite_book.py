# 8.2. Любимая книга: напишите функцию favorite_book(), которая получает
# один параметр title. Функция должна выводить сообщение вида «One of my
# favorite books is Alice in Wonderland». Вызовите функцию и убедитесь в
# том, что название книги правильно передается как аргумент при вызове функции.

def favorite_book(book):
    """Вывод любимой книги"""
    message = 'One of my favorite books is ' + book
    return message


print(favorite_book('Alice in Wonderland'))
