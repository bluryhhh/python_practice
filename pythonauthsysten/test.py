import json

try:
 with open("/Users/pl/work/python/practice/pythonauthsysten/users.json", "r") as file:
    users = json.load(file)
except FileNotFoundError: 
    print("file not found")


def signup(): 


  print("signup!")
  while True:  
     username = input("enter ur username: ")
     if username in users: 
       print("username already taken, try a different one: ")
     else: 
       break


  password = input("enter ur password")
  users[username] = {
   "username": username,
   "password": password
 }


  with open("/Users/pl/work/python/practice/pythonauthsysten/users.json", "w") as file:
   json.dump(users, file, indent=4)
   print("user successfuly created")


def login():
  
  print("login")
  while True: 
      currentuser = input("enter ur username")
      if currentuser in users:
       currentpassword = input("enter ur password")
       if currentpassword == users[currentuser]["password"]:
     

  
         print("successfuly logged in")
         print("1 for changing your password")
         print("2 for adding an email")
         print("3 for exit")
     else:
       break
  
  decision = input()
  

        if decision == 1:
            oldpass = input("enter ur current password")
            if oldpass == users[currentuser]["password"]:
              newpass = input("enter ur new password")
              users[currentuser]["password"] = newpass
              print("password successfully reset")
            else: print("incorrect password")

            if decision == "2":
              email = input("enter ur email")
              users[currentuser]["email"] = email
              print("email successfuly added")

            if decision == "3":
             print("program ended")           


while True:
    print("1 for signup")
    print("2 for login")
    print("3 for exit")

    choice = input()
    if choice == "1":
     signup()

    elif choice == "2":
     login()

    elif choice == "3":
     print("goodbye")
    break

else: 
 print("invalid choice")

