from donations_pkg import homepage
from donations_pkg.user import login, register
from donations_pkg.homepage import donate, show_donations

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)
    option = input("Choose an option: ")

    if option == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif option == "3":
        if authorized_user == "":
            print("\nYou are not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(str(donation))
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("Leaving DonateMe...")
        break

