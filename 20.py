import random

n = ''
nambers = list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

a = int(input("Карой длины пароль нужен: "))

for i in range(a):
    n += random.choice(nambers)
        
print(n)

