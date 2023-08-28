#importing required libraries
import random
import string

# function for password generation
def password(length=8):
    character=string.ascii_letters + string.digits + string.punctuation
    passwd = random.choice(string.ascii_letters)  # First character is an alphabet
    passwd += "".join(random.choice(character) for i in range(length-1))
    return passwd
#main body
l=int(input("Enter the length of the password:-"))
p=password(l)
print("Generated password is:-" + p)
