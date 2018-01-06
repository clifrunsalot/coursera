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

##########################

def strComp(s1, s2):
	if (s1 > s2):
		return "after"
	elif (s1 < s2):
		return "before"
	else:
		return "equal"

s1 = "A"
s2 = "a"
print(s1, "is ", strComp(s1,s2), s2)

s1 = "a"
s2 = "A"
print(s1, "is ", strComp(s1,s2), s2)

s1 = "a"
s2 = "a"
print(s1, "is ", strComp(s1,s2), s2)

################ practical exercises ################

def is_even(number):
	return (number % 2) == 0
	
number = 5
print(str(number) + " is even: " + str(is_even(number)))
number = 2
print(str(number) + " is even: " + str(is_even(number)))

def is_cool(name):
	"""
	Returns True if name is either:
	"Joe," "John," or "Stephen.
	"""
	return name in ["Joe", "John", "Stephen"]
	
name = "Stephen"
print(name + " is cool: " + str(is_cool(name)))
name = "Jack"
print(name + " is cool: " + str(is_cool(name)))
name = "Joe"
print(name + " is cool: " + str(is_cool(name)))
name = "John"
print(name + " is cool: " + str(is_cool(name)))

def is_lunchtime(hr, is_morning):
	"""
	Returns True if hr is either 11am to 12pm.
    """
	if is_morning and hr == 11:
		return True
	elif not is_morning and hr == 12:
		return True
	else:
		return False
	
def is_lunchtime_test(hour, is_am):
	"""
	Tests the is_lunchtime function.
	"""
	print(hour, end = "")
	if is_am:
		print("AM", end = "")
	else:
		print("PM", end = "")
	if is_lunchtime(hour, is_am):
		print(" is lunchtime.")
	else:
		print(" is not lunchtime.")

is_lunchtime_test(11,True)
is_lunchtime_test(12,True)
is_lunchtime_test(11,False)
is_lunchtime_test(12,False)
is_lunchtime_test(10, False)

def is_leap_year(year):
	"""
	Returns True if year is a Leap Year.
	"""
	if year % 4 != 0:
		return False
	elif (year % 100) != 0:
		return True
	elif (year % 400) != 0:
		return False
	else:
		return True


year = 2000
print(str(year) + " is a leap year: " + str(is_leap_year(year)))
year = 1996
print(str(year) + " is a leap year: " + str(is_leap_year(year)))
year = 1800
print(str(year) + " is a leap year: " + str(is_leap_year(year)))
year = 2013
print(str(year) + " is a leap year: " + str(is_leap_year(year)))

def interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
	"""
	Return true if int1 intersects with int2
	"""
	return int2_lower <= int1_upper and int1_lower <= int2_upper
	
int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 1, 2
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

int1_lower, int1_upper, int2_lower, int2_upper = 1, 2, 0, 1
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 2, 3
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

int1_lower, int1_upper, int2_lower, int2_upper = 2, 3, 0, 1
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

int1_lower, int1_upper, int2_lower, int2_upper = 0, 3, 1, 2
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

int1_lower, int1_upper, int2_lower, int2_upper = 1, 3, 0, 2
print("int1(" + str(int1_lower) + "," + str(int1_upper) + ") intersects (" + str(int2_lower) + "," + str(int2_upper) + "): " + str(interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper)))

def print_digits(number):
	if len(str(number)) == 2:
		tens = str(number)[0]
		ones = str(number)[1]
		print("tenths=" + tens + ",ones=" + ones)
	elif len(str(number)) == 1:
		print("tenths=0" + ",ones=" + str(number))
	else:
		print("Error: Input in not a two-digit number")
	
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)

print("#############")

#
# (b**2) - (4*a*c)
#

def smaller_root(coeff_a, coeff_b, coeff_c):
	"""
	Returns the value of the discriminant.
	"""
	discriminant = (coeff_b ** 2) - (4 * coeff_a * coeff_c)
	if discriminant >= 0:
		return discriminant
	else:
		return "Error: No real solutions"
		

coeff_a, coeff_b, coeff_c = 1,2,3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2,0,-10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

print(True)
print(False)
print(1)

print("#############")

def myexpr(p, q):
	"""
	Returns true if the expression is true.
	"""
	return not (p or not q)
	
p = True
q = True
print(myexpr(p,q))

p = True
q = False
print(myexpr(p,q))

p = False
q = True
print(myexpr(p,q))

p = False
q = False
print(myexpr(p,q))

print("#############")

def myexpr1(bool1, bool2):
	"""
	Returns true if true.
	"""
	if bool1:
		if bool2:
			return False
		else:
			return True
	else:
		return True

bool1 = True
bool2 = True
print("=============")
print("* " + str(myexpr1(bool1,bool2)))
print("=============")
print("1 " + str(bool1 and bool2))
print("2 " + str(bool1 or bool2))
print("3 " + str(not(bool1 and bool2)))
print("4 " + str(not(bool1 or bool2)))
bool1 = True
bool2 = False
print("=============")
print("* " + str(myexpr1(bool1,bool2)))
print("=============")
print("1 " + str(bool1 and bool2))
print("2 " + str(bool1 or bool2))
print("3 " + str(not(bool1 and bool2)))
print("4 " + str(not(bool1 or bool2)))
bool1 = False
bool2 = False
print("=============")
print("* " + str(myexpr1(bool1,bool2)))
print("=============")
print("1 " + str(bool1 and bool2))
print("2 " + str(bool1 or bool2))
print("3 " + str(not(bool1 and bool2)))
print("4 " + str(not(bool1 or bool2)))
bool1 = False
bool2 = True
print("=============")
print("* " + str(myexpr1(bool1,bool2)))
print("=============")
print("1 " + str(bool1 and bool2))
print("2 " + str(bool1 or bool2))
print("3 " + str(not(bool1 and bool2)))
print("4 " + str(not(bool1 or bool2)))

print("######################")
def collatz(n):
	val = 0;
	if (n == 1):
		print(val)
		return
	elif (n%2) == 0:
		val = (n//2)
		return (val)
	else:
		val = (3*n + 1)
		return (val)

# 12, 6, 3, 10, 5, 16, 8, 4, 2, 1
print(collatz(collatz(collatz(collatz(collatz(collatz(collatz(674))))))))

#
print(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(1071)))))))))))))))

################ Week 4 #####################

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

