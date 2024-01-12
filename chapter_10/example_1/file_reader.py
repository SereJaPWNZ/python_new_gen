# file_path = ('/Users/sergeyshevtsov/Documents/git/python_books/chapter_10/'
#              'example_1/text_files/pi_digits.txt')
file_name = 'pi_digits.txt'
with open('text_files/'+file_name) as file_object:
    lines = file_object.readline()

for line in lines:
    print(line.rstrip())
