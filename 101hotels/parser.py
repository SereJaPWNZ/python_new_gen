import pycurl
from io import BytesIO


# Создаем буфер для хранения ответа
buffer = BytesIO()

# Инициализируем объект Curl
c = pycurl.Curl()

# Устанавливаем URL, который хотим получить
c.setopt(c.URL, 'http://www.python.org')

# Передаем буфер в pycurl для хранения ответа
c.setopt(c.WRITEDATA, buffer)

# Выполняем HTTP-запрос
c.perform()

# Завершаем сессию curl
c.close()

# Получаем содержимое, хранящееся в объекте BytesIO
body = buffer.getvalue()
