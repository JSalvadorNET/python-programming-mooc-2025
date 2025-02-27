def largest():
    largest_num = 0
    with open("numbers.txt") as new_file:
        for number in new_file:
            number = int(number.strip())
            if number > largest_num:
                largest_num = number
    return largest_num

if __name__ == "__main__":
    print(largest())
