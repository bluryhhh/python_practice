def signup(users):
    print("\n--- create an account ---")

    username = input("enter ur username: ").strip()

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

    print("account created successfully!")
    print("welcome", username)


users = {}

signup(users)