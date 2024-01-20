import json

with open("numbers.json") as n:
    numbers = json.load(n)

print(numbers)