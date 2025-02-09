string = input("Please type in a string: ")
star = "*"
length = int(len(string))

print(f"{(star * (20 - length))}{string}")