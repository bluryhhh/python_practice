users = ["razi", "ali", "hamza"]
newUser = input("enter ur name: ")
users.append(newUser)

#to replace 
users[1] = "admin"

#to remove
users.remove("razi")
print(users)