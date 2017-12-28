"""
Demonstration of simple arithmetic expression in Python.
"""

# Unary + and -
print("Unary operators")
print(+3)
print(-5)
print(+7.86)
print(-3348.63)

print("")

# Simple arithmetic
print("Addition and Subtraction")
print(1 + 2)
print(48 - 89)
print(3.45 + 2.7)
print(87.3384 - 12.35)
print(3 + 6.7)
print(9.8 - 4)

print("")

# Order of operations
print("Order of operations")
print(1 + 1)
print(2 ** 2)
print(2 + (2 ** 2))

print("")

# Integer expressions
print("Integer expressions")
print(4.5 // 2)
print(4 // 6)
print(4.5 // 2.2)

print("")

# Strings
print("Strings")
print("Hello, world")
print("This course is great!")
print("'ello")
print("[Hello]")
print("Goodbye'")

print("")

# Expressions
print("Expressions")
#print(9 - (2-(4*3))
print((7-2)/(3**2))
#print(3 * ((2-9)+4))*(2+(1-3)))
print(7/+4)
print((8 + (1 + (2 * 4) - 3)))

print("")

print("Variables")
number123 = 123
print(number123)

#my.number = 3
#print(my.number)

#16ounces = 16
#print(16ounces)

__numbers__ = 3
print(__numbers__)

oz_in_gram = 0.035274 
mass_in_ounces = 35
mass_in_grams = mass_in_ounces / oz_in_gram
print(str(mass_in_grams) + " grams in " + str(mass_in_ounces) + " oz")

ft_in_mile = 5280
miles = 5
total_ft = 5 * 5280
print(str(total_ft) + " ft in " + str(miles) + " miles")

############# quiz practice ##############

def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))

#########################

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)

#########################

def funcX(val):
  return (-5*(val**5)) + (67*(val**2)) - 47
  
print(funcX(0))
print(funcX(1))
print(funcX(2))
print(funcX(3))

##########################

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return (present_value * ((1 + rate_per_period) ** periods))
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
print("$500 at 4% compounded 10 times per year for 10 years yields $", future_value(500, .04, 10, 10))

########################

def EqTriArea(side):
  return ((3**0.5) / 4) * (side**2)
  
print(EqTriArea(1))
print(EqTriArea(2))
print(EqTriArea(3))
print(EqTriArea(4))
print(EqTriArea(5))

