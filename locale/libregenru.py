import random

chars = '+-/*!&$#?=@<>[\]•^_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
for n in range(number):
    password =''
    for i in range(length):
        password = random.choice(chars)
    print(password) 
    print("copyright 2022 sashimiv")
    print("github.com/sashimiv/libregen")
    print("telegram: @sashimiv")
    
