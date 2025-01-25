import random
import string

pwd_length = int(input("Password Length: "))
pwd_no = int(input("Number of Passwords: "))

def pwd_generator(pwd_length, pwd_no):
    generated_passwords = []
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(pwd_no):
        password = ''.join(random.choice(characters) for i in range(pwd_length))
        generated_passwords.append(password)
    
    return generated_passwords

passwords = pwd_generator(pwd_length, pwd_no)

print("Generated Passwords:\n")
for idx, pwd in enumerate(passwords, 1):
    print(f"{idx}: {pwd}")