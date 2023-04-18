import mysql.connector
import encryption as cry


pwDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="passManager"
)
c = pwDB.cursor()


def addUser(username, password, site):
    password, salt = cry.encrypt_password(password)
    c.execute(
        f'Insert into users(username, password, site, salt) values("{username}", "{password.decode()}", "{site}", "{salt.decode()}");')
    pwDB.commit()
    c.fetchall()


def matchUser(username, password, site):
    test = c.execute(
        f'select password from table where username="{username}" and site="{site}";'
    )
    c.fetchall()
    if cry.check_password(password, test[0]):
        print(f"you are logged to {site}")
    else:
        print("credentials are wrong!")


def accountsInSite(site):
    c.execute(f'select username from users where site="{site}";')
    test = c.fetchall()
    print(*test)


def adminHash():
    c.execute(f'select password from users where username="admin"')
    test = c.fetchone()[0]
    # print(test)
    # print(type(test))
    return test


def resetPass(site, username, password):
    _pass, salt = cry.encrypt_password(password)
    c.execute(
        f'update users set password="{_pass.decode()}" and salt="{salt.decode()}" where username="{username}" and site="{site}";')
    pwDB.commit()


def checkEmpty():
    c.execute(
        f'select username from users where username="admin";'
    )
    test = c.fetchone()
    if test == None:
        return True
    else:
        return False


def update(user, newpw, site):
    newpw, salt = cry.encrypt_password(newpw)
    c.execute(
        f'update users set password="{newpw}", salt="{salt}" where username="{user}" and site="{site}";'
    )
    pwDB.commit()


def getSalt(site, username):
    c.execute(
        f'select salt from users where username="{username}" and site="{site}";'
    )
    test = c.fetchone()[0]
    # print(test)
    return test
