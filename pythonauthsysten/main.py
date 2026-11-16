users = {}
def signup():
    username = input("enter ur username: ")
    password = input("enter ur pass: ")
    if username in users:
        print("username alreay taken try a differennt one")
    else: 
        users[username] = {
            "username": username,
            "password": password
        }
        print("user successfuly created")
        print(users.get(username))
        print(users.get("email"))

def login():
    currentuser = input("enter ur user: ")
    if currentuser in users:
        currentpass = input("enter ur password: ")
        if currentpass == users[currentuser]["password"]: 
         print("successfuly logged in, would u like to enter an email aswell? (optional)")
         decision = input("write yes or no: ")
         if decision == "yes":
            email = input("enter ur email: ")
            users[currentuser]["email"] = email
         elif decision == "no":
            print("no problem, enjoy")
        else: 
            print("password is incorrect")
    else: 
     print("user does not exist")    
signup()
login()
print(users)