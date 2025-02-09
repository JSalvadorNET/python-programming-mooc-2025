'''
word  = input("Please type in a string: ")
i = 0

while i < len(word)+1:
    print(f"{word[0:i]}")
    i += 1
'''

word  = input("Please type in a string: ")
lenght = (len(word)+1)*-1
i = -1

while i > lenght:
    print(f"{word[i:]}")
    i -= 1
