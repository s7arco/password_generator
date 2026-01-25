import random
import string

def password_generator(length):
    password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return password

print("Password Generator")
user_length = int(input("Password Length: "))

password = password_generator(user_length)
print(password)


    