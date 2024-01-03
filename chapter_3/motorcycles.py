motorcycles = ['yamaha', 'honda', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'yamaha'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'yral')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.append('ural')

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.append('ural')

motorcycles.remove('ural')
print(motorcycles)
