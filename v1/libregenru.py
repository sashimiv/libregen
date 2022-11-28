import random

chars = '+-/*!&$#?=@<>[\]{^_a}bcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('number of passwords?'+ "\n")
length = input('password length?'+ "\n")

number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
     password = random.choice(chars)
    print(password) 
    
