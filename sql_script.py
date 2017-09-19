import sys, sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()
prefix = 'insert into emp values'

def add_user():
    name = input("enter your pseudo: ")
    mdp = input("enter your password: ")
    curs.execute(prefix + "('{}', '{}')".format(name, mdp))

def check_user():

    haveAccount = input("are you registered? (y/n): ").lower().strip()

    if haveAccount == "y":
        print("okay")
        sys.exit()

    elif haveAccount == "n":
        add_user()

    elif haveAccount == "q": #dev option, will not be in the final code
        sys.exit()
        
    else:
        print("i don't know this command")
        sys.exit()

    result = curs.execute("select user, password from emp")
    print(result.fetchall())


# main loop
try:
    curs.execute('create table emp (user, password)')
except:
    pass
while True:
    check_user()
