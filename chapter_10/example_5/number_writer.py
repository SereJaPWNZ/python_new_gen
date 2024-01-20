import json

numbers = [1, 5, 12, 15, 22, 56]

filename = "numbers.json"
with open(filename, "w") as f:
    json.dump(numbers, f)
