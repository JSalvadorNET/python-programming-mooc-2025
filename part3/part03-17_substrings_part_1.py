word  = input("Please type in a string: ")
i = 0

while i < len(word)+1:
    print(f"{word[0:i]}")
    i += 1
