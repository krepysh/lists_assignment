# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension
new_list = [x*x for x in range(10)]

print(new_list)




# Task 2. Create a list containig numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

leap_years = []

y = int(input("Enter a year: "))

if is_leap(y):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")

leap_years = [year for year in range(2000, 2101) if is_leap(year)]

print("Leap years between 2000 and 2099:", leap_years)





# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2000, 'bicycle': 20, 'TRUCK': 7000, 'motorcycle': 200, 'Minivan': 1700, 'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}

# With single list comprehension select vehicle those weight is below 5000 kg
# Convert names to upper-case within same list comprehension
new_list = [x.upper() for x in vehicles if vehicles[x] < 5000]
print(new_list)