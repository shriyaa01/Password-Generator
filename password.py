import random
chars="qwertyuiopasdfghjklzxcvbnm1234567890QAZXSWEDCVFRTGBNHYUJMKIOPL@#$&"
password=""
length=int(input("length of the password"))
for i in range(length):
    password+=random.choice(chars)
print(password)