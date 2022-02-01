import random

char = "1234567890-=_+!@#$%^&*()±§qwertyuiop[]asdfghjkl;`zxcvbnm,.QWERTYUIOPASDFGHJKLZXCVBNM"
print("     Password generator")
number = int(input("Number of passwords: "))
dlin = int(input('How long is the password needed: '))
for i in range(number):
    password = ''

    for j in range(dlin):
        password += random.choice(char)

    print(password)
