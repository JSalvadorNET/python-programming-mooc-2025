'''
CALCULATE LEAP YEAR

year = int(input("Please type in a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
'''

year = int(input("Year: "))

# Find next leap year
next_leap_year = year + 1
while True:
    if (next_leap_year % 4 == 0 and next_leap_year % 100 != 0) or (next_leap_year % 400 == 0):
        break
    next_leap_year += 1

print(f"The next leap year after {year} is {next_leap_year}")