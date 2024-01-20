import json

with open("username.json") as un:
    print(f"Welcome back, {json.load(un).title()}!")
