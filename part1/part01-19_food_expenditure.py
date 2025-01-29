cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_cost = float(input("How much money do you spend on groceries in a week? "))
 
# Calculate the weekly food expenditure (cafeteria cost + grocery cost)
weekly_expenditure = (cafeteria_visits * lunch_price) + groceries_cost
# Calculate the daily food expenditure (weekly expenditure divided by 7)
daily_expenditure = weekly_expenditure / 7
 
print("\nAverage food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")