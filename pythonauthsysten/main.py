import json


with open("/Users/pl/work/python/practice/pythonauthsysten/users.json", "r") as file:
   users = json.load(file)




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
    with open("/Users/pl/work/python/practice/pythonauthsysten/users.json", "w") as file: 
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
            else: print("wrong password")
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