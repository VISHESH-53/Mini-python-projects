import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter password length: "))

password = "".join(random.choice(chars) for _ in range(length))
print("Your password is:", password)
