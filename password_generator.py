import random
import string

def password_generator(password, length=5):
    password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return password

print(password_generator(5))

    