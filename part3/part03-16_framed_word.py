word = input("Word: ")
length = len(word)

total_padding = 28 - length  
left_padding = total_padding // 2
right_padding = total_padding - left_padding

print("*" * 30)
print(f"*{' ' * left_padding}{word}{' ' * right_padding}*")
print("*" * 30)
