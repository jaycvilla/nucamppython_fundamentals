def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("\nWelcome back", username + "!")
            return username
        print("\nIncorrect password for", username + ".")
        return ""
    print("\nUser not found. Please register.")
    return ""

def register(database, username):
    if username in database:
        print("\nUsername already registered")
        return ""
    else:
        print("\n ", username, " has been registered")
        return username

