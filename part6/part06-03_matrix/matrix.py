def matrix_sum():
    total_sum = 0
    with open("matrix.txt") as new_file:
        for row in new_file:
            numbers = row.strip().split(",")  
            for num in numbers:  
                total_sum += int(num)  
    return total_sum

def matrix_max():
    max_number = 0
    with open("matrix.txt") as new_file:
        for row in new_file:
            numbers = row.strip().split(",")  
            for num in numbers:  
                num = int(num)
                if num > max_number:
                   max_number = num
    return max_number

def row_sums():
    row_sums = []
    with open("matrix.txt") as new_file:
        for row in new_file:
            numbers = row.strip().split(",")  
            total_row_sum = 0  
            for num in numbers:  
                total_row_sum += int(num)  
            row_sums.append(total_row_sum)  
    return row_sums
    

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())