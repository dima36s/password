import random

char = "1234567890-=_+!@#$%^&*()±§qwertyuiop[]asdfghjkl;`zxcvbnm,.QWERTYUIOPASDFGHJKLZXCVBNM"
print("     Программа генератора паролей")
number = int(input("Количесвто паролей: "))
dlin = int(input('Длинна стороки: '))
for i in range(number):
    password = ''

    for j in range(dlin):
        password += random.choice(char)

    print(password)
