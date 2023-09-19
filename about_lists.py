# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension
nums = [x**2 for x in range(1, 11)]

# Task 2. Create a list containing numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400
leap_year = [year for year in range(2000, 2101) if (year % 4 == 0 and year % 100) or year % 400 == 0]


# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2000, 'bicycle': 20, 'TRUCK': 7000, 'motorcycle': 200, 'Minivan': 1700, 'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}

# With single list comprehension select vehicle those weight is below 5000 kg
# Convert names to upper-case within same list comprehension
selected_vehicles = [vehicle.upper() for vehicle, weight in vehicles.items() if weight < 5000]
print(selected_vehicles)