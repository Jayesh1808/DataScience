import random

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = uppercase.lower()
digits = '0123456789'
symbols = '!@#$%^&*'
print('Enter the length for password: ')
n = int(input())
print('Your Randomly Genrated password: ')
upper, lower, num, sym = True, True, True, True

password = ''
if upper:
    password += uppercase
if lower:
    password += lowercase
if num:
    password += digits
if sym:
    password += symbols

length = n

for i in range(1):
    pss = "".join(random.sample(password, length))
    print(pss)
