#learning sets 
users = {"razi", "ali", "babar"}

users.add("hamza")
users.add("razi")

users.remove("ali")

newUser = input("enter ur username: ")

if newUser in users:
    print("username exists")
else:
    print("username doesnt exists")