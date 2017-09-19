import sys, sqlite3

# database sqlite3 pour les pseudos + pswrds -> database permanente
# ou la fonction read de python, w/ read & write
# implementer la fonction rate_me.py

users = {}

def account_check():

    print("")
    haveAccount = input("do you have an account ? (y/n) ").lower().strip()

    if haveAccount == "y":

        pseudo = input("enter your pseudo: ").lower()

        if pseudo in users:

            password = input("enter your password: ")

            if password in users[pseudo]:

                print("")
                print("it's ok, welcome {} !".format(pseudo.capitalize()))

            else:

                print("")
                print("sorry, wrong password !")

        else:

            print("")
            print("who are you ? :/")

    elif haveAccount == "n":

        print("")
        choice = input("do you want to register? (y/n) ").lower().strip()

        if choice == "y":

            pseudo = input("enter your pseudo: ").lower()

            if pseudo not in users:

                password = input("enter your password: ")
                users[pseudo] = password
                print("")
                print("you're in the database, welcome !")

            else:

                print("")
                print("/!\ this pseudo is taken !")

        elif choice == "n":

            print("see ya!")
            sys.exit()

        else:

            print("unknown command!")

    else:

        print("unknown command!")
        sys.exit()

while True:
    account_check()
