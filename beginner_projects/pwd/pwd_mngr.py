import random 
import string 

pwd_length = int(input("Length of Password: "))
pwd_no = int(input("How many Passwords do you need?: "))

def pwd_generator(pwd_length, pwd_no):
    # initialization of the stuff to make the password generator
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_passwords = []

    for i in range(pwd_no):
        password = ''.join(random.choice(characters) for i in range(pwd_length))
        generated_passwords.append(password)
    
    return generated_passwords

passwords = pwd_generator(pwd_length, pwd_no)

print ("\nGenerated Passwords:")
for idx, pwd in enumerate(passwords, 1):
    print(f"{idx}: {pwd}")