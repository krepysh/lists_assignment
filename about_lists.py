# Task 1. Create a list containing squares for number from 1 up to 10.
# Use list comprehension
def squares():
    new_list = [i**2 for i in range(1,11)]
    return new_list

print(squares())







# if year % 4 == 0 and year % 100 != 0:
#     return True
# else:
#     return False   

# Task 2. Create a list containig numbers leap years in the future from 2000 up to 2100
# Use list comprehension with if condition
# Hint: leap year is a year divisible by 4, but not by 100, unless it is divisible by 400

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False  
    
newlist = [i for i in range(2000,2100) if is_leap(i) ] 
print(newlist)

# Task 3. You are given a dictionary with vehicles and their weights:
vehicles = {'sedan': 1550, 'Pickup': 2, 'bicycle': 70, 'TRUCK': 7000, 'motorcycle': 2979, 'Minivan': 17000, 'SUV': 2500, 'van': 3500, 'Semi': 12000, 'Bus': 3000}

# With single list comprehension select vehicle those weight is below 5000 kg
# Convert names to upper-case within same list comprehension

# def small_car(vehicles):
#     if vehicles < 5000:
#         return True
#     else:
#         False

car_list = [name for name in vehicles if vehicles[name] < 5000]
print(car_list)