pass1 = input("Password: ")
 
while True:
    pass2 = input("Repeat password: ")
    if pass1 != pass2:
        print("They do not match!")
    else:
        print("User account created!")
        break
 