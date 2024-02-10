# Импортируем модуль pycurl для работы с HTTP-запросами и обменом данными по протоколу HTTP
from encodings import utf_8
import pycurl
import re
import time


start_time = time.perf_counter()

response_body = []

# Функция обратного вызова для игнорирования данных
def write_data(data):
    """Функция обратного вызова для игнорирования данных."""
    response_body.append(data)

# Создание объекта curl
curl = pycurl.Curl()

# Настройка функции обратного вызова для игнорирования данных
curl.setopt(pycurl.WRITEFUNCTION, write_data)

# Задаем список урлов
url = ["https://101hotels.com/main/cities/moskva"]
# Задаем значения URL
curl.setopt(pycurl.URL, url[0])

# Выполнение get запроса
curl.perform()

# Получение статус кода
response_code = curl.getinfo(pycurl.RESPONSE_CODE)
print(f"Response code: {response_code}\n")

# Получение времени ответа сервера
ttfb = curl.getinfo(pycurl.STARTTRANSFER_TIME)
print(f'TTFB: {ttfb} c\n')

# Получение Total Time
total_time = curl.getinfo(pycurl.TOTAL_TIME)
print(f'Total time: {total_time} c\n')

# Вычисляем размер скаченного документа


# Вычисляем размер документа
size_html_doc = "%.2f" % (curl.getinfo(pycurl.SIZE_DOWNLOAD) / 1024)
print(f'Resource Size HTML: {size_html_doc}\n')

# Закрытие соединения
curl.close()

# Преобразование и вывод response_body в человекочитаемом виде
response_body_str = b"".join(response_body).decode('utf_8')
# print(response_body_str)

# получение title
title_match = re.search(r'<title>(.*?)</title>', response_body_str, re.DOTALL)

if title_match:
    title = title_match.group(1)
    print(f'{title}\n')
else:
    print("Title не найден\n")

# получение description
description_match = re.search(r'<meta name="description" content="(.*?)"', response_body_str, re.DOTALL)

if description_match:
    description = description_match.group(1)
    print(f'{description}\n')
else:
    print("Description не найден")

end_time = time.perf_counter()
time = end_time - start_time
print(time)