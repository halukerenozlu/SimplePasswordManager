import random


def add_pasword(*args):
    passwords.append(args[0])
    return args[0]


def delete_password():
    if passwords:
        return passwords.pop()
    else:
        return 'There is no password to delete!'


def list_password() -> list:
    print(passwords)
    return passwords


def random_password():
    x = random.randint(1000, 9999)
    add_pasword(x)
    return x


passwords = []
rand_password = None
password = None
print('Rules: At least 4 digits and numeric characters.')

while True:
    answer = input('Generate random password (Y/n): ')
    if answer == 'Y':
        random_password = random_password()
        print(f'Random password: {rand_password}')
        list_password()
        break
    elif answer == 'n':
        password = int(input('Please enter password: '))
        if password <= 9999 and password >= 1000:
            add_pasword(password)
            list_password()
            break
        else:
            print('Password must be 4 digits')
            continue
    else:
        print('Invalid entry! Please enter only "Y" or "n".')

while True:
    answer = input('Do you want to delete your password? (Y/n): ')
    if answer == 'Y':
        deleted_password = delete_password()
        print(f'deleted password: {deleted_password}')
        list_password()
    elif answer == 'n':
        print(f'{password} not deleted.')
        break
    else:
        print('Invalid entry! Please enter only "Y" or "n".')


while True:
    if password is not None and password in passwords:
        if 1000 <= password <= 9999:
            print(f'Password: {password} added.')
        else:
            print(
                f'Password:{password} Password does not comply with the rules')
    else:
        print('Transaction completed!')
    break
