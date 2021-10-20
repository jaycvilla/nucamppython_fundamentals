def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.     Register        |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations   |")
    print("------------------------------------------")
    print("|          5.     Exit                     |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("\nEnter amount to donate: ")
    donation_amt = float(donation_amt)
    donation = (username , "donated $" , donation_amt)
    print("Thank you" , username , "for donating $" , donation_amt)
    return (donation)

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == [] :
        print("Currently, there are no donations.")
    else:
        print(donations)
