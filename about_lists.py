# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension
array = [i**2 for i in range(1,11)]
print(array)
# Task 2. Create a list containig numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400

def is_leap(year):
    if year%4:
        return False
    else:
        if year%100:
            return True
        else:
            if year%400:
                return False
            else:
                return True


leap_years = [year for year in range(2000, 2101) if is_leap(year)]
print(leap_years)


# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2000, 'bicycle': 20, 'TRUCK': 7000, 'motorcycle': 200, 'Minivan': 1700, 'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}
vehicles_under = [name for name in vehicles if vehicles[name] < 5000]
print(', '.join(vehicles_under))


# With single list comprehension select vehicle those weight is below 5000 kg
# Convert names to upper-case within same list comprehension