import random as random

char = "abcdefghijklmnopqrstuvwxyz1234567890?!@#$%*()"

length = int(input("Enter the length of the password you need : "))
password = ""

for i in range(length):
    password += random.choice(char)
print(password)    
