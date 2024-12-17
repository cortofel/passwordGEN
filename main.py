import random
password = ""
simbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passi = int(input("Введите длину пароля"))
for i in range(passi):
    password += random.choice(simbol)
print(password)
