import hashlib
import sqlite3


def get_username_from_input():
    return input("Please enter your username: ")


def get_password_from_input():
    return input("Please enter your password: ")


def check_username_if_exist(username):

    db = open_database()
    cursor = db.cursor()
    cursor.execute("SELECT username FROM userInfo WHERE username=?", (username,))  # we add the comma so sql will understand that its a tupple
    retrieved_username = cursor.fetchone()
    db.commit()
    db.close()
    if retrieved_username == None:
        return False


def verify_username(username):
    if(len(username) > 6):
        return True
    else:
        return False


def verify_password(password):
    verified = True

    if(len(password) < 8 or len(password) > 12):
        # print('The lenght of the password should be at least 8 characters or a max of 12.')
        verified = False
    elif (' ' in password):
        # print('Your password shouldn\'t include spaces.')
        verified = False
    elif (any(p.isdigit() for p in password) == False):
        # print('Your password should include at least 1 number from [0-9]')
        verified = False
    elif(not any(p.isupper() for p in password)):
        # print('Your password should include at least 1 upper case character')
        verified = False
    elif (not any(p.isalnum() for p in password)):
        # print('your password shouldn\'t include nonalphanumeric characters')
        verified = False

    return verified


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def open_database():
    return sqlite3.connect('databse-save-user-info.db')


def storing_in_database(username, hashedPassword):
    print(username, hashedPassword)
    db = open_database()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userInfo(username text, password text)''')
    cursor.execute("INSERT INTO userInfo (username, password)VALUES(?,?)", (username, hashedPassword,))
    print('saving to database completed')
    db.commit()
    db.close()


def check_longin(username_, password_):
    hashedPass = hash_password(password_)
    db = open_database()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM userInfo WHERE username=?", (username_,))
    retrieved_pass = cursor.fetchone()
    db.commit()
    db.close()
    print(retrieved_pass)
    if(hashedPass == retrieved_pass):
        return True
    else:
        return False


def open_database():
    return sqlite3.connect('databse-save-user-info.db')


def storing_in_database(username, hashedPassword):
    db = open_database()
    conn = db.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS userInfo(username text, password text)''')
    conn.execute('''INSERT INTO userInfo (username, password)VALUES(?,?)''', (username, hashedPassword,))
    print('saving to database completed')
    db.commit()
    db.close()


# cursor = open_database()
# cursor.execute('''CREATE TABLE IF NOT EXISTS userInfo(username text, password text)''')
# con = close_database()
# while True:
#     username = get_username_from_input()
#     if (check_username_if_exist(username) == Flase):
#         print("you are a new user.")

#     else:

# verify - by sending the password to the function
# if verified, move on
# otherwise, ask again


# get_username_from_input()
# while True:
#     password = get_password_from_input()
#     print(verify_password(password))
#     if (verify_password(password) == True):
#         hashedPass = hash_password(password)
#         break
#     else:
#         True


# # store password in database
# storing_in_database(hashedPass, username)


# print('please enter your username and password again to verify:')
# username_ = get_username_from_input()
# password_ = get_password_from_input()
# check_longin(password_, username_)
