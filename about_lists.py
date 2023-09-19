# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension

items = [i ** 2 for i in range(1, 11)]
print('Task 1.\t', items)


# Task 2. Create a list containig numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


years = [i for i in range(2000, 2101) if is_leap(int(i))]
print('Task 2.\t', years)

# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2000, 'bicycle': 20, 'TRUCK': 7000, 'motorcycle': 200, 'Minivan': 1700,
            'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}

# With single list comprehension select vehicle those weight is below 5000 kg
# Convert names to upper-case within same list comprehension

select_vehicles = [i.upper() for i in vehicles if vehicles[i] < 5000]
print('Task 3.\t', select_vehicles)
