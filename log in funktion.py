users = {}

def login():
    print("skapa din profil")
    while True:
        username = input("använarnamn")
        password = input("lösenord")
        if username in users and users[username] == password:
            print(f"Hej {username}! Du är inloggad.\n")
            return True
        else:
            print("Fel användarnamn eller lösenord. Försök igen.\n")