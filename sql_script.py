import sys, sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()
prefix = 'insert into emp values'

def check_user():

    choice = input("existes-tu ? (y/n): ").lower().strip()

    if choice == "y":
        print("okay")
        sys.exit()

    elif choice == "n":
        name = input("entre ton nom: ")
        mdp = input("entre ton mot de passe: ")
        curs.execute(prefix + "('{}', '{}')".format(name, mdp))
    else:
        print("i don't know this")
        sys.exit()

    result = curs.execute("select user, password from emp")
    print(result.fetchall())

try:
    curs.execute('create table emp (user, password)')
except:
    pass

check_user()
