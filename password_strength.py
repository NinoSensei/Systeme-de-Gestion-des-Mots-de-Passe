from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
import random
from time import sleep
import password_DB as pdb
import encryption as cry

'''
    for a password it should be:
        minimum length: 12
        complex: uppercase, lowercase, symbols and numbers
        should not be easy or guessable
        unique: not used for other accounts
        avoid common patterns: repeated words or letters, numbers...
        avoid dictionary words
        change it regularly
'''


def password_genetator(length):
    '''generates a password of a given length'''
    password = ""
    for _ in range(length):
        password += random.choice(l + u + d + p)
    return password


def strong_password_checker(password):
    '''Checks if password contains at least 1 uppercase, 1 lowercase, 1 digit and 1 symbol'''
    test = [l, u, d, p]
    for _ in test:
        if (set(password) & set(_)) == set():
            return "It's weak!"
    return "It's strong"


def choices(ch):
    if ch == 1:
        password = input("Enter your password:")
        if len(password) < 12:
            print("It's weak!")
            sleep(1)
            return 0
        else:
            print(strong_password_checker(password))
        sleep(1)
    elif ch == 2:
        while True:
            try:
                pass_length = int(input("Length of the password: "))
                if pass_length > 0 and pass_length <= 50:
                    break
                else:
                    print("Enter a number between 1 and 50")
            except:
                print("Please enter an integer!")
    elif ch == 3:
        while True:
            print('''
            \t 1- add account to DB.
            \t 2- get accounts linked to a site.
            \t 3- reset password of an account in a site.
            \t 4- update admin password.
            \t 0- exit.
            ''')
            ch2 = int(input("Enter your choice: "))
            if ch2 == 1:
                if pdb.checkEmpty():
                    print("You should add admin credentials first!")
                    sleep(1.5)
                else:
                    # print(pdb.checkEmpty())
                    site = input("Enter the site: ")
                    user = input("Enter the username: ")
                    password = input("Enter the password: ")
                    if user.lower() != "admin":

                        pdb.addUser(user, password, site)
                        print("The user is stored in the DB successfully!")
                        sleep(2)
                    else:
                        print(f"the username '{user}' is not allowed!")
            elif ch2 == 2:
                site = input("Enter the site: ")
                print("The accounts linked to this site are:")
                print(f'The usernames are: ', end='')
                pdb.accountsInSite(site)
                sleep(2)
            elif ch2 == 3:
                adminpw = input("Enter the admin password: ")
                if cry.check_password(adminpw, pdb.adminHash()):
                    site = input("Enter the site: ")
                    user = input("Enter the username: ")
                    newPass = input("Enter the new password: ")
                    pdb.resetPass(user, site, newPass)
                    print("Password is reseted!")
                else:
                    print("password is wrong! Access Denied!")
            elif ch2 == 4:
                if pdb.checkEmpty():
                    print("The user is set to 'admin'.")
                    password = input("Enter a password: ")
                    pdb.addUser("admin", password, "")
                    print("admin account is set!")
                    sleep(1)
                else:
                    adminpw = input("Enter the admin password: ")
                    if cry.check_password(adminpw, pdb.adminHash()):
                        newAdminPass = input("Enter the new admin password: ")
                        pdb.update("admin", newAdminPass, "")
                    else:
                        print("password is wrong! Access Denied!")
            elif ch2 == 0:
                break
            else:
                print("Your choice doesn't exist!")
    password = password_genetator(pass_length)
    status = strong_password_checker(password)
    print(f"possible password: {password}\nstatus: {status}")
    sleep(2)


# main program
t = True
while t:
    print('''
    welcome to the password manager:
    --------------------------------
    1-Check your password's strength.
    2-Generate a Strong password.
    3-Archeive of passwords.
    0-Exit.
    ''')
    ch = int(input("Enter your choice: "))
    if ch == 0:
        t = False
        print("See you later!")
    else:
        choices(ch)


'''
add restrection on the admin entry in the sql database
add back option when chosing the 3rd option
get accounts linked to a site.: when entring numbers or wrong entry, fix
admin, admin123
add account to DB.: when enmpty databse, don't add accounts
when looking for accounts linked to a site and the site doesn't exist, return a message!
when choosing an option, if not a number it should have alternative
use getpass module to hida password when entring it
when entring an already existing account error need to fix
'''
