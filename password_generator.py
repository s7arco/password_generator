import random
import string

def password_generator(length):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

print("Password Generator")
user_length = int(input("Password Length: "))

password = password_generator(user_length)
print(password)


    