from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year:"))

if year >= 2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    user_born = datetime(year, month, day)
    millenium = datetime(1999, 12, 31)
    days_for_millenium =  millenium - user_born
    print(f"You were {days_for_millenium.days} days old on the eve of the new millennium.")