from bank import BankAccount

blank = "                                         "
usernames = []
pins = []


def account_maker(usernames, pins, blank):

    def check(username):

        digits = 0
        length = len(username)

        while digits == 0 and (len(username)) < 8:
            print("Username must contain 8 or more characters and at least 1 digit")
            for i in range(len(username)):
                if username[i].isdigit():
                    digits += 1
            username = input("Enter the username again: ")

        return username

    username = input("Create a username: ")

    check(username)

    pin = int(input("Create a 4 digit pin: "))

    while len(str(pin)) != 4:
        pin = int(input("Enter a 4 digit code: "))

    usernames.append(username)
    pins.append(pin)

    print("You successfully created an account,you can now login! *bringing you back to the main page* please wait...")
    print(blank)
    main(usernames, pins, blank)

    return username, pin


def login(usernames, pins, blank):
    logged = False

    tries = 3

    while not logged:
        username = input("Enter your username: ")
        pin = int(input("Enter your pin: "))

        for i in range(len(usernames)):
            if tries > 0:
                if username == usernames[i] and pin == pins[i]:
                    print("You successfully logged in.")
                    print(blank)
                    logged = True

                elif tries > 0:
                    print("Invalid details. Please Try Again")
                    tries -= 1
                else:
                    if tries == 0:
                        print("You have entered the wrong details 3 times in a row. Brining you back to the menu...")
                        print(blank)

                        main(usernames, pins)

    a1 = BankAccount(username, pin, usernames, pins)

    return True, username, pin, a1


def main(usernames, pins, blank):

    print("Welcome to The Rakibul Bank ltd. ")

    exist = input("Do you already have an account with us? [Y/N]: ").upper()

    while exist != "Y":

        if exist == "N":
            account_maker(usernames, pins, blank)

        elif exist != "Y":
            print("Invalid Input. Please try again.")

    logged_in, username, pin, a1 = login(usernames, pins, blank)

    def logged(logged_in, username, pin, a1):

        if logged_in is True:

            valid_option = False
            print(blank)
            print("""
            1. Check Balance
            2. Deposit Money
            3. Withdraw Money
            4. Change Pin
            """)
            print(blank)

            while not valid_option:

                option = int(input("Please Enter An Option: "))

                if option == 1:
                    a1.get_balance()
                    valid_option = True
                elif option == 2:
                    a1.deposits()
                    valid_option = True
                elif option == 3:
                    a1.withdraw()
                    valid_option = True
                elif option == 4:
                    a1.change_pin()
                    valid_option = True
                else:
                    print("Invalid Option. Please Try Again")
                    valid_option = False

            user_choice = input("Do you want to go back the menu or log out [M/L]: ").upper()

            if user_choice == "M":
                logged(logged_in, username, pin, a1)
            elif user_choice == "L":
                main(usernames, pins, blank)

        logged(logged_in, username, pin, a1)

    logged(logged_in, username, pin, a1)


main(usernames, pins, blank)
