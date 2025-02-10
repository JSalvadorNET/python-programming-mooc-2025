def palindromes(word):
    return word == word[::-1]
 
while True:
    palindrome = input("Please type in a palindrome: ")
    
    if palindromes(palindrome):
        print(f"{palindrome} is a palindrome!")
        break
    else:
         print("that wasn't a palindrome")
 
 
 