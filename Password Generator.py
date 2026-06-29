import random
import string
length = int(input("Enter the length:"))
characters = string.ascii_uppercase + string.ascii_lowercase  + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Password:", password)
