import sys, sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()
prefix = 'insert into emp values'

def check_user():

    haveAccount = input("are you registered? (y/n): ").lower().strip()

    if haveAccount == "y":
        print("okay")
        sys.exit()

    elif haveAccount == "n":
        name = input("enter your pseudo: ")
        mdp = input("enter your password: ")
        curs.execute(prefix + "('{}', '{}')".format(name, mdp))

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

check_user()
