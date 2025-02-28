def read_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)  
        try:
            number = int(user_input)  
            if min_value <= number <= max_value:
                return number  
            print(f"You must type in an integer between {min_value} and {max_value}")
        except ValueError:
            print(f"You must type in an integer between {min_value} and {max_value}")  

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 95, 105)
    print("You typed in:", number)
