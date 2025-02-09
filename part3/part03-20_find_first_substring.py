'''
input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")
'''

word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)

if len(word) > 3:
    if char in word:
        if index == len(word) or index == (len(word)-2):
            None
        else:
            print(f"{word[index:index+3]}")
else:
    None