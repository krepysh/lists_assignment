# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension
lis=[(i+1)**2 for i in range(10)]

print(lis)

# Task 2. Create a list containig numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400

def is_leap(year):
    if year%4 == 0:
        if year%400 == 0:          
            return True
        elif year%100 == 0:
            return False
        else:
            return True
    else:
        return False

leap_years=[i for i in range(2000,2101) if is_leap(i)]

print(leap_years)


# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2000, 'bicycle': 20, 'TRUCK': 7000, 'motorcycle': 200, 'Minivan': 1700, 'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}

# Withff single list comprehension select vehicle those weight is below 5000 kg

liss = [i.upper() for i,j in vehicles.items() if j <5000]
print(liss)