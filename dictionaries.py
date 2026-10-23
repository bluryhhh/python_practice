account = {
    "1username": "razi",
    "1balance": 1000, 
    "1account_type": "savings"
}
print(account["1username"])
account["1balance"] = 75000
account["1currency"] = "pkr"
print(account)


#signup 
newAccount = {
    "username": "",
    "password": "",
}
signupUsername = input("enter your username: ")
signupPassword = input("enter ur password: ")
newAccount["password"] = signupPassword
newAccount["username"] = signupUsername

print("account created: ", newAccount)