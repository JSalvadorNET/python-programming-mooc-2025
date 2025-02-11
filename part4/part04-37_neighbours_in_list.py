def longest_series_of_neighbours(a_list):
    longest = 1 # longest series
    result = 1 # actual series
    for i in range(1, len(a_list)):
        if abs(a_list[i-1]-a_list[i]) == 1: # the difference between the actual number and the previous one must be exactly 1
            result += 1 # increase the series 
        else:
            result = 1 # reset the series
        longest = max(longest, result)
    return longest
 
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))