# file_path = ('/Users/sergeyshevtsov/Documents/git/python_books/chapter_10/'
#              'example_1/text_files/pi_digits.txt')
file_name = 'pi_digits.txt'
file_name_million = 'pi_million_digits.txt'
with open('text_files/'+file_name) as file_object:
    lines = file_object.readline()

with open('text_files/'+file_name_million) as file_object:
    lines_million = file_object.readline()

pi_string = ''
pi_string_million = ''
for line in lines:
    pi_string += line.strip()

for line in lines_million:
    pi_string_million += line.strip()

# print(pi_string)
# print(len(pi_string))
# print(pi_string_million)
# print(len(pi_string_million))

birthday = input("Введите день вашего дня рождения:\n")
count = 0
if birthday in pi_string_million:
    count += 1
print(count)
