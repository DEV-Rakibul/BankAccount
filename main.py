class BankAccount:
    def __init__(self, username, pin, usernames, pins):

        self.username = username
        self.pin = pin
        self.usernames = usernames
        self.pins = pins
        self.balance = 0

    def deposits(self):

        print("You can only print in 10s.")
        print("                           ")

        deposit_amount = int(input("How much are you depositing: $"))

        while (deposit_amount % 10) != 0:
            print("Invalid amount")
            print("                           ")
            deposit_amount = int(input("How much are you depositing: $"))

        self.balance += deposit_amount

        return self.balance

    def withdraw(self):
        withdraw_amnt = int(input("How much are you withdrawing: $"))

        money_left = self.balance - withdraw_amnt
        if money_left < 0:
            print("Not enough money!")
            print("you have $", self.balance, "in your account")
            amount = int(input("Enter amount withdrawing: $"))
        else:
            self.balance -= withdraw_amnt

    def get_balance(self):
        print(self.username, "you have $", self.balance, "in your account")

    def change_pin(self):
        new_pin = int(input("Enter the new pin: "))

        while len(str(new_pin)) != 4:
            new_pin = int(input("Enter a 4 digit code: "))

        for i in range(len(self.usernames)):
            if self.usernames[i] == self.username and self.pins[i] == self.pin:
                self.pins[i] = new_pin
                print("Pin has been changed.")

        return self.pins
