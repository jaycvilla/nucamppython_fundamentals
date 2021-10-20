

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password   

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def deposit(self, amount):
        self.balance += float(amount)
        self.show_balance()

    def withdraw(self, amount):
        self.balance -= float(amount)
        self.show_balance()       

    def transfer_money(self, amount):
        print("\nYou are transferring", amount, "to", bankuser2.name)
        print("Authentication required")
        pin = input("Enter your PIN: ")
        if bankuser1.pin == pin:
            bankuser1.balance -= float(amount)
            bankuser2.balance += float(amount)
            print("Transferring", amount, "to", bankuser2.name,)
        else:
            print("Invalid PIN. Transaction canceled.")
        
    def request_money(self, amount):
        print(f"\nYou are requesting {amount} from {bankuser1.name}")
        print("Authentication required")
        pin = input(f"Enter {bankuser1.name} PIN: ")
        if bankuser1.pin == pin:
            password = input("Enter your password: ")
            if bankuser2.password == password:
                print("Request Authorized")         
                bankuser1.balance -= float(amount)
                bankuser2.balance += float(amount)
                print(bankuser1.name, " sent ", amount)
            else:
                print("Invalid Password. Transaction canceled.")
        else:
            print("Invalid Pin. Transaction canceled.")




"""Driver Code for Task 5"""
bankuser1 = BankUser("Bob", "123", "password")
bankuser2 = BankUser("Alice", "321", "wrongpassword")
bankuser1.deposit(5000)
BankUser.show_balance(bankuser2)
bankuser1.transfer_money(250)
BankUser.show_balance(bankuser1)
BankUser.show_balance(bankuser2) 
bankuser1.request_money(250)
BankUser.show_balance(bankuser1)
BankUser.show_balance(bankuser2)              


"""Driver Code for Task 2""" 
#user1 = User("Bob", 123, "password")
#print(user1.name, user1.pin, user1.password)
#user1.change_name("Bobby")
#user1.change_pin(4321)
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)

"""Driver Code for Task 3""" 
#user1 = BankUser("Bob", 123, "password")
#print(user1.name, user1.pin, user1.password, user1.balance)

"""Driver Code for Task 4"""
#bankuser1 = BankUser("Bob", 123, "password")
#print(user1.name, user1.pin, user1.password, user1.balance)
#user1.show_balance
#user1.deposit(1000)
#user1.show_balance
#user1.withdraw(500)
#user1.show_balance
