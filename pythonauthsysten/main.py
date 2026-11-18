import json
file_path = "/Users/pl/work/python/practice/pythonauthsysten/users.json"

try: 
 with open(file_path, "r") as file:
  users = json.load(file)
except FileNotFoundError: 
   print("file not found, creating a new database")
   users = {}
except json.JSONDecodeError:
 print("database is corrupted")
 users = ()
   



  


def signup():
    while True: 
     username = input("enter ur username: ")
     if username in users:
        print("username alreay taken try a differennt one")
     else: 
       break
    
    password = input("enter ur pass: ")
    users[username] = {
            "username": username,
            "password": password
        }
    with open(file_path, "w") as file: 
     json.dump(users, file, indent=4)
    print("user successfuly created")

def login():
    currentuser = input("enter ur user: ")
    if currentuser in users:
        currentpass = input("enter ur password: ")

        if currentpass == users[currentuser]["password"]: 
                changepass = input("would you like to change your password, enter yes or no: ")

                if changepass == "yes":
                    oldpass = input("enter ur old password: ")

                    if oldpass == users[currentuser]["password"]:
                     newpass = input("enter ur new password: ")
                     users[currentuser]["password"] = newpass

                    

                print("successfuly logged in, would u like to enter an email aswell? (optional): ")

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

while True:
    print("1 for login")
    print("2 for signup")
    print("3 for exit")

    choice = input("")

    if choice == "1":
        login()

    elif choice == "2":
        signup()

    elif choice == "3":
        print("program ended")
        break

    else:
        print("false choice")