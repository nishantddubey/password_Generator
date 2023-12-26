import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$$$%^&*"

while True:
    
    paswd_length = int(input('Enter the Length of Password: '))
    paswd_count = int(input("Enter the numbers of required password: "))

    for _ in range(paswd_count):
        password = ""
        for _ in range(paswd_length):
            pass_char = random.choice(char)
            password+=pass_char
        print(password)
    repeat = input("Do you want to generate more password: ")
    if repeat=='no' or repeat=='NO':
        print("Thankyou")
        break