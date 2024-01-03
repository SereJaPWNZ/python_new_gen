# Периоды жизни: напишите цепочку if-elif-else для определения периода жизни че-
# ловека. Присвойте значение переменной age, а затем выведите сообщение:
# • Если значение меньше 2 — младенец.
# • Если значение больше или равно 2, но меньше 4 — малыш.
# • Если значение больше или равно 4, но меньше 13 — ребенок.
# • Если значение больше или равно 13, но меньше 20 — подросток.
# • Если значение больше или равно 20, но меньше 65 — взрослый.
# • Если значение больше или равно 65 — пожилой человек.

age = 65

if age < 2:
    life_period = 'младенец'
elif age < 4:
    life_period = 'малыш'
elif age < 13:
    life_period = 'ребенок'
elif age < 20:
    life_period = 'подросток'
elif age < 65:
    life_period = 'взрослый'
else:
    life_period = 'пожилой человек'

print(life_period)
