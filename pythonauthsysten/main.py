
print("Welcome to Python Auth System")

users = {}

def signup():
    print("\nCreate your account")

    username = input("enter ur username: ").strip().lower()

    if username == "":
        print("username cant be empty")
        return

    if username in users:
        print("user already exists")
        return

    password = input("enter ur password: ")

    if len(password) < 6:
        print("password must be at least 6 characters")
        return

    confirm_password = input("confirm ur password: ")

    if password != confirm_password:
        print("passwords dont match")
        return

    users[username] = {
        "username": username,
        "password": password
    }

    print("user successfully created")


def login():
    print("\nLogin to your account")

    username = input("enter ur username: ").strip().lower()
    password = input("enter ur password: ")

    if username not in users:
        print("account not found")
        return

    if users[username]["password"] == password:
        print("login successful")
        print("welcome", username)
    else:
        print("incorrect password")


while True:
    print("\n1. signup")
    print("2. login")
    print("3. exit")

    choice = input("choose an option: ")

    if choice == "1":
        signup()

    elif choice == "2":
        login()

    elif choice == "3":
        print("goodbye")
        break

    else:
        print("invalid option")
