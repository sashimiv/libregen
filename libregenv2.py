import random
chars = '+-/*!&$#?=@<>[\]{^_a}bcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = int(input('password length?'))
print("  ")
print("github.com/sashimiv/libregen")
print("  ")
for i in range(length):
   password = random.choice(chars)
   print(password) 
