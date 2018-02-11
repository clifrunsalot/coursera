"""
Demonstration of simple arithmetic expression in Python.
"""
import random

def add_break_and_title(title):
    """
    Prints a formatted string that represents the following:

    ************* title **************

    Usage:
    add_break_and_title(title)
        where title is a string.

    """
    print()
    print("************ " + title + " *************")

add_break_and_title("Simple unary operators")
def unary_example():
    """
    Simple unary operators.
    """
    print(+3)
    print(-5)
    print(+7.86)
    print(-3348.63)
unary_example()

add_break_and_title("Simple arithmetic")
def add_minus():
    """
    Simple add and subtract.
    """
    print(1 + 2)
    print(48 - 89)
    print(3.45 + 2.7)
    print(87.3384 - 12.35)
    print(3 + 6.7)
    print(9.8 - 4)
add_minus()

add_break_and_title("add_minus")
add_minus()

def order_of_operations():
    """
    Simple operator precedence.
    """
    print("Order of operations")
    print(1 + 1)
    print(2 ** 2)
    print(2 + (2 ** 2))

add_break_and_title("Order of operations")
order_of_operations()

def integer_expressions():
    """
    Simple integer expressions.
    """
    print("Integer expressions")
    print(4.5 // 2)
    print(4 // 6)
    print(4.5 // 2.2)

add_break_and_title("Integer expressions")
integer_expressions()

def simple_strings():
    """
    Simple string expressions.
    """
    print("Strings")
    print("Hello, world")
    print("This course is great!")
    print("'ello")
    print("[Hello]")
    print("Goodbye'")

add_break_and_title("String expressions")
simple_strings()

def simple_math_expressions():
    """
    Simple math expressions.
    """
    print((7-2)/(3**2))
    print(7/+4)
    print((8 + (1 + (2 * 4) - 3)))

add_break_and_title("Simple math expressions")
simple_math_expressions()

def variables():
    """
    Simple variables.
    """
    number123 = 123
    print(number123)

add_break_and_title("Simple variables")
variables()

def convert_oz_to_grams(ounces):
    """
    Returns ounces converted to grams.

    Usage:
    convert_oz_to_grams(ounces)
        where ounces is an integer or float and >= 0.

    """
    oz_in_gram = 0.035274
    mass_in_grams = ounces / oz_in_gram
    return mass_in_grams

add_break_and_title("convert grams to oz")
mass_in_oz = 35
print("There are " + str(mass_in_oz) + "oz in " + str(convert_oz_to_grams(mass_in_oz)) + " grams")

def convert_ft_to_miles(ft):
    """
    Returns feet converted to miles.
    """
    ft_per_mile = 5280
    return ft / 5280

add_break_and_title("convert to ft to miles")
ft = 10000
print("There are " + str(ft) + "ft in " + str(convert_ft_to_miles(ft)) + " miles")

ft = 5280
print("There are " + str(ft) + "ft in " + str(convert_ft_to_miles(ft)) + " miles")

def convert_miles_to_ft(miles):
    """
    Returns miles converted to feet.
    """
    ft_per_mile = 5280
    return miles * ft_per_mile

add_break_and_title("convert miles to ft")
miles = 10
print("There are " + str(10) + " miles in " + str(convert_miles_to_ft(miles)) + " ft")

def max_of_2(val1, val2):
    """
    Returns the max of val1 and val2
    """
    if val1 > val2:
        return val1
    else:
        return val2

def max_of_3(val1, val2, val3):
    """
    Returns the max of val1, val2, and val3.
    """
    return max_of_2(val1, max_of_2(val2, val3))

add_break_and_title("find max value out of three")
v1 = 345
v2 = 123
v3 = 7
print("The max value between "
        + str(v1) + ", " + str(v2) + ", " + str(v3) + " is "
        + str(max_of_3(v1, v2, v3)))

#########################

def project_to_distance(point_x, point_y, distance):
    """
    Returns the projection of x,y based on distance.
    """
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

add_break_and_title("project_to_distance")
x = 2
y = 7
dist = 4
print("x, y, dist: " + str(x)
                + ", " + str(y)
                + ", " + str(dist) + " projects to ")
project_to_distance(x, y, dist)

x = 1
y = 1
dist = 4
print("x, y, dist: " + str(x)
                + ", " + str(y)
                + ", " + str(dist) + " projects to ")
project_to_distance(x, y, dist)

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return (present_value * ((1 + rate_per_period) ** periods))

add_break_and_title("Calculate future value based on rate over years")
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
print("$500 at 4% compounded 10 times per year for 10 years yields $", future_value(500, .04, 10, 10))

def EqTriArea(side):
    """
    Returns the area of an equilateral triangle based on length side."
    """
    return ((3**0.5) / 4) * (side**2)

add_break_and_title("Calculate the area of an equilateral triangle of lengthe side.")
side = 1
print("The area of equilateral triangle with side length of " + str(side) + ": " + str(EqTriArea(side)))
side = 2
print("The area of equilateral triangle with side length of " + str(side) + ": " + str(EqTriArea(side)))
side = 3
print("The area of equilateral triangle with side length of " + str(side) + ": " + str(EqTriArea(side)))
side = 4
print("The area of equilateral triangle with side length of " + str(side) + ": " + str(EqTriArea(side)))

def strComp(s1, s2):
    """
    Returns 'after' if s1 < s2 or
    'before' if s1 > s2 or
    'equals' if s1 == s2.
    """
    if (s1 > s2):
        return "after"
    elif (s1 < s2):
        return "before"
    else:
        return "equal"

add_break_and_title("Relational comparison of strings.")
s1 = "A"
s2 = "a"
print(s1 + " is " + strComp(s1,s2) + " " + s2)

s1 = "a"
s2 = "A"
print(s1 + " is " + strComp(s1,s2) + " " + s2)

s1 = "a"
s2 = "a"
print(s1 + " is " + strComp(s1,s2) + " " + s2)

def is_even(number):
    """
    Returns true if number is even.
    """
    return (number % 2) == 0

add_break_and_title("Check if number is even")
number = 5
print(str(number) + " is even: " + str(is_even(number)))
number = 2
print(str(number) + " is even: " + str(is_even(number)))

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

add_break_and_title("Check if hour is lunchtime")
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

add_break_and_title("Check if year is a leap year")
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
    """
    Prints the ones and tens digits if number is a digit.
    """
    if len(str(number)) == 2:
        tens = str(number)[0]
        ones = str(number)[1]
        print("tenths=" + tens + ",ones=" + ones)
    elif len(str(number)) == 1:
        print("tenths=0" + ",ones=" + str(number))
    else:
        print("Error: Input in not a two-digit number")

add_break_and_title("print_digits")
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)

print("#############")

def get_discriminant(coeff_a, coeff_b, coeff_c):
    """
	Returns the value of the discriminant.

    (b**2) - (4*a*c)

    """
    discriminant = (coeff_b ** 2) - (4 * coeff_a * coeff_c)
    if discriminant >= 0:
        return discriminant
    else:
        return "Error: No real solutions"

add_break_and_title("get_discriminant")
coeff_a, coeff_b, coeff_c = 1,2,3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(get_discriminant(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2,0,-10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(get_discriminant(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
	"x + " + str(coeff_c) + " is: ")
print(str(get_discriminant(coeff_a, coeff_b, coeff_c)))

def collatz(n):
    """
    Returns f(n) based on the Collatz algorithm.
    """
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

add_break_and_title("collatz")
# 12, 6, 3, 10, 5, 16, 8, 4, 2, 1
print(collatz(collatz(collatz(collatz(collatz(collatz(collatz(674))))))))
print(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(1071)))))))))))))))

def slice_string_example():
    """
    Simple string slicing exercises.
    """
    word = "everything"

    print("word = everything")
    print("substrings")
    print("word[1:5]              => " + word[1:5])
    print("word[5:9]              => " + word[5:9])
    print("open ended slices")
    print("word[5:]               => " + word[5:])
    print("word[:4]               => " + word[:4])
    print("negative indices")
    print("word[-3:]              => " + word[-3:])
    print("word[2:-3]             => " + word[2:-3])
    print("indexing past the end")
    print("word[8:20]             => " + word[8:20])
    print("$ + word[22:29] + \"^\"  => " + "$" + word[22:29] + "^")
    print("empty slices")
    print("word[6:6]              => " + word[6:6])
    print("word[4:2]              => " + word[4:2])

add_break_and_title("slice_string_example")
slice_string_example()

def format_specifiers(name, age):
    """
    Simple format examples.
    """
    last_yr = age-1
    print("{0} is {1} years old, but {0} was {2} years old last year".format(name, age, last_yr))

add_break_and_title("format_specifiers")
format_specifiers("clif",52)

def fix_strings():
    """
    Fix the four strings below.
    """
    string1 = "It's just a flesh wound"
    string2 = "'It's just a flesh wound'"
    string3 = "\"It's just a flesh wound\""
    string4 = "\"\"It's just a flesh wound"

    print(string1)
    print(string2)
    print(string3)
    print(string4)

add_break_and_title("fix_strings")
fix_strings()

def get_first_last_characters(str1):
    """
    Returns the first and last characters of str.
    """
    return str1[0] + str1[-1]

add_break_and_title("get_first_last_characters")
print(get_first_last_characters("Hello"))
print(get_first_last_characters("Melly"))

def get_middle_characters(str1):
    """
    Returns all characters minus the first and last characters.
    """
    return str1[1:-1]

add_break_and_title("get_middle_characters")
print(get_middle_characters("annabelle"))
print(get_middle_characters("jacksonpollack"))

def get_threes(str1):
    """
    Returns a string composed of the first three and last three
    characters of the str.
    """
    first_3 = str1[:3]
    last_3 = str1[-3:]
    return first_3 + last_3

add_break_and_title("get_threes")
print(get_threes("Where in the world is Carmen San Diego"))
print(get_threes("Peter piper picked a peck of pickles"))

def echo_and_repeat(str1, nbr):
    """
    Returns the value of str1 repeated nbr times.
    """
    return (str1 + "\n") * nbr

add_break_and_title("echo and repeat")
print(echo_and_repeat("Why",3))
print(echo_and_repeat("Because",3))

def is_substring(example_string, test_string):
    """
    Returns True if test_string is a substring of example_string.
    """
    return example_string.find(test_string) > -1

add_break_and_title("is_substring")
outside_str = "Winebago"
inside_str = "eb"
print(inside_str + " is a substring of " + outside_str + ": " + str(is_substring(outside_str, inside_str)))

outside_str = "Winebago"
inside_str = "xx"
print(inside_str + " is a substring of " + outside_str + ": " + str(is_substring(outside_str, inside_str)))

outside_str = "Winebago"
inside_str = "o"
print(inside_str + " is a substring of " + outside_str + ": " + str(is_substring(outside_str, inside_str)))

outside_str = "Winebago"
inside_str = "w"
print(inside_str + " is a substring of " + outside_str + ": " + str(is_substring(outside_str, inside_str)))

outside_str = "Winebago"
inside_str = "W"
print(inside_str + " is a substring of " + outside_str + ": " + str(is_substring(outside_str, inside_str)))

def make_nametag(name, topic):
    """
    Returns a string where XXX is replaced by name
    and YYY is replaced by YYY.
    """
    return "Hi! My name is {0}. This lecture covers {1}".format(name, topic)

add_break_and_title("make_nametag")
print(make_nametag("clif","python"))
print(make_nametag("george","monkeying around"))

def make_int(int_string):
    """
    Returns the value of int_string if it is a non-negative integer
    or -1 if not.
    """
    if int_string.isdigit():
        return int(int_string)
    else:
        return -1

add_break_and_title("make_int")
int_string = "123"
print(int_string + " contains an integer: " + str(make_int(int_string)))

int_string = "00123"
print(int_string + " contains an integer: " + str(make_int(int_string)))

int_string = "12.3"
print(int_string + " contains an integer: " + str(make_int(int_string)))

int_string = "-123"
print(int_string + " contains an integer: " + str(make_int(int_string)))

def name_swap(name_string):
    """
    Returns name_string in the form of first name as Last First.
    """
    spacer = name_string.find(" ")
    first = name_string[:spacer]
    last = name_string[spacer+1:]
    return (last + " " + first).title()

add_break_and_title("name_swap")
print(name_swap("clif hudson"))

def count_vowels(word):
    """
    Returns the number of occurrences of lowercase vowels.
    """
    total = 0
    for ch in ("a","e","i","o","u"):
        total += word.count(ch.lower())

    return total

add_break_and_title("count_vowels")
word_ = "aaassseefffgggiiijjjoOOkkkuuuu"
print(word_ + " has " + str(count_vowels(word_)) + " lowercase vowels.")

word_ = "aovvouOucvicllOveeOlclOeuvvauouuvciOlsle"
print(word_ + " has " + str(count_vowels(word_)) + " lowercase vowels.")

def demystify(l1_string):
    """
    Returns a string where l is replaced by a and 1 is replaced by b.
    """
    return l1_string.replace("l","a").replace("1","b")

add_break_and_title("demystify")
word_ = "lll111l1l1l1111lll"
print(demystify(word_))

word_ = "111l1l11l11lll1lll1lll11111ll11l1ll1l111"
print(demystify(word_))

primes = [2, 3, 5, 7, 11, 13, 17]
def show_prime_indices(primes):
    """
    Display visual between list of primes and their
    corresponding indices.
    """
    print("List of primes and their indices")
    str_list = []
    for p in primes:
        str_list.append(str(p) + " [" + str(len(str_list)) + "]")
    return str_list

add_break_and_title("show_prime_indices")
print(show_prime_indices(primes))

def get_primes(primes, count):
    """
    Returns a list of primes up to the count specified.
    """
    print("Primes up to index " + str(count) + ": " + str(primes[:count]))
    return primes[:count]

def get_primes_in_list(primes, idx_list):
    """
    Returns the prime numbers in the primes list at the indices in idx_list.
    """
    print("Primes at indices " + str(idx_list))
    ret_list = []
    for itm in idx_list:
        ret_list.append(primes[itm])
    return ret_list

add_break_and_title("get_primes")
print(primes)
count = 0
idx_list = [0]
print(show_prime_indices(primes))
print(get_primes(primes, count))
print(get_primes_in_list(primes, idx_list))

count = 2
idx_list = [1,2]
print(show_prime_indices(primes))
print(get_primes(primes, count))
print(get_primes_in_list(primes, idx_list))

count = 5
idx_list = [1,3,5]
print(show_prime_indices(primes))
print(get_primes(primes, count))
print(get_primes_in_list(primes, idx_list))

def combine_first_last(lst):
    """
    Returns a list that contains the first and last elements of lst.
    """
    print("List: " + str(lst))
    ret_val = []
    ret_val.append(lst[0])
    ret_val.append(lst[-1])
    return ret_val

add_break_and_title("combine_first_last")
example_list = [2, 3, 5, 7, 11, 13]
print(combine_first_last(example_list))

example_list = [3, 5, 7, 11]
print(combine_first_last(example_list))

example_list = [5, 7]
print(combine_first_last(example_list))

example_list = [5]
print(combine_first_last(example_list))

def true_false_list():
    """
    Returns list of 16 elements where the first 8 are True
    and the last 8 are False.
    """
    lst = 8 * [True] + 8 * [False]
    return lst

add_break_and_title("true_false_list")
print(true_false_list())

def split_words_into_list(wrd):
    """
    Splits wrd into a list of words. Assume there is a space between words.
    """
    print("Words to split: " + wrd)
    return wrd.split(" ")

add_break_and_title("split_words_into_list")
print(split_words_into_list("hello my name is george."))

def word_count(txt, wrd):
    """
    Returns the count of wrd in txt.
    """
    print("Text: " + txt)
    print("Word to find: " + wrd)
    wrds = txt.split(" ")
    return wrds.count(wrd)

add_break_and_title("word_count")
find_str = "pigdog"
print(word_count("this pigdog is a fine pigdog", find_str))
find_str = "dog"
print(word_count("this pigdog is not a dog", find_str))
find_str = "pigdog"
print(word_count("this pigdog is not a pig", find_str))

def strange_sum(numbers):
    """
    Returns the sum of the values in numbers that are not divisible by 3.
    """
    print("Numbers: " + str(numbers))
    total = 0
    for n in numbers:
        if n % 3:
            total += n
    return total

add_break_and_title("strange_sum")
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(strange_sum(numbers))
numbers = list(range(123)) + list(range(77))
print(strange_sum(numbers))

def n_relation_to_m(n, m):
    """
    Returns len of range based on values of n and m.
    """
    my_list = list(range(1,n))
    final_list = my_list * m
    return len(final_list)

add_break_and_title("n_relation_to_m")

lens_ = []
for n in list(range(6)):
    for m in list(range(6)):
        result = n_relation_to_m(n,m)
        val = "{:>5} {:>5} {:>5} {:>5}".format(n,m,result,m*(n-1))
        lens_.append(val)

print('my_list = list(range(1,n))')
print('final_list = my_list * m')
print('len(final_list)')

print("{:>5} {:>5} {:>5} {:>5}".format("n", "m", "len",'m*(n-1)'))
print("\n".join(lens_))

def convert_to_tuple(lst):
    """
    Converts list lst into a tuple and returns it.
    """
    print("Original lst: " + str(lst))
    return tuple(lst)

lst1 = list(range(5))
add_break_and_title("convert_to_tuple")
print("converted to tuple: " + str(convert_to_tuple(lst1)))

def convert_to_list(tup):
    """
    converts tuple tup into a list and returns it.
    """
    print("Original tuple: " + str(tup))
    return list(tup)

add_break_and_title("convert_to_list")
tup1 = (5,6,7,8,9)
print("Converted to list: " + str(convert_to_list(tup1)))

def change_list_value(lst, idx, new_val):
    """
    Updates the value of lst at the idx.
    """
    print("Original list: " + str(lst))
    print("Set idx " + str(idx) + " to " + str(new_val))
    lst[idx] = new_val
    return lst

add_break_and_title("change_list_value")
lst = [1,2,3,4,5]
idx = 3
new_val = 0
print("Updated list: " + str(change_list_value(lst, idx, new_val)))

def change_list_with_slice(lst, fromIdx, toIdx, new_val):
    """
    Updates the list lst at indices fromIdx, toIdx with new_val.
    """
    print("Original list: " + str(lst))
    print("Slice to use: '" + str(fromIdx) + ":" + str(toIdx) + "'")
    print("with this value: " + str(new_val))
    lst[fromIdx:toIdx] = new_val
    return lst

add_break_and_title("change_list_with_slice")
lst = [2, 3, 5, 7, 11, 13]
fromIdx = 1
toIdx = 2
new_val = [0,0,0]
print("Updated list: " + str(change_list_with_slice(lst, fromIdx, toIdx, new_val)))

def copy_list_and_append(lst, new_val):
    """
    Copies the list lst and appends new_val.
    """
    print("Original list: " + str(lst))
    print("append this value: " + str(new_val))
    print("lst.append(new_val)")
    lst.append(new_val)
    return lst

add_break_and_title("copy_list_and_append")
lst = [2, 3, 5, 7, 11, 13]
new_val = 0
print("Updated list: " + str(copy_list_and_append(lst, new_val)))

def copy_list_and_extend(lst1, new_val):
    """
    Copies list and extends copy.
    """
    print("Original list1: " + str(lst1))
    print("Values to add to copy of list: " + str(new_val))
    lst2 = list(lst1)
    print("lst2.extend(new_val)")
    lst2.extend(new_val)
    return lst2

add_break_and_title("copy_list_and_extend")
lst = [2, 3, 5, 7, 11, 13]
new_val = [0, 0, 0]
lst2 = copy_list_and_extend(lst, new_val)
print("New list: " + str(lst2))

def copy_list_and_concatenate(lst1, new_val):
    """
    Copies list and concatenate copy.
    """
    print("Original list1: " + str(lst1))
    print("Values to add to copy of list: " + str(new_val))
    lst2 = list(lst1)
    print("lst2 = lst2 + new_val")
    lst2 = lst2 + new_val
    return lst2

add_break_and_title("copy_list_and_concatenate")
lst = [2, 3, 5, 7, 11, 13]
new_val = [0, 0, 0]
lst2 = copy_list_and_concatenate(lst, new_val)
print("New list: " + str(lst2))

def copy_list_and_append_with_loop(lst1, new_val):
    """
    Copies list and appends new_val with loop.
    """
    print("Original list1: " + str(lst1))
    print("Values to add to copy of list: " + str(new_val))
    lst2 = list(lst1)
    for i in new_val:
        lst2.append(i)
    return lst2

add_break_and_title("copy_list_and_append_with_loop")
lst = [2, 3, 5, 7, 11, 13]
new_val = [0, 0, 0]
lst2 = copy_list_and_append_with_loop(lst, new_val)
print("New list: " + str(lst2))

def copy_list_and_randomize_with_shuffle(lst1):
    """
    Copies list and randomizes it with shuffle.
    """
    print("lst2 = list(lst1)")
    print("random.shuffle(lst2)")
    lst2 = list(lst1)
    random.shuffle(lst2)
    return lst2

add_break_and_title("copy_list_and_randomize_with_shuffle")
lst = [2, 3, 5, 7, 11, 13]
print("Original list1: " + str(lst1))
lst2 = copy_list_and_randomize_with_shuffle(lst)
print("New list: " + str(lst2))
lst2 = copy_list_and_randomize_with_shuffle(lst)
print("New list: " + str(lst2))
lst2 = copy_list_and_randomize_with_shuffle(lst)
print("New list: " + str(lst2))

def flatten_lists(lst_of_lists):
    """
    Returns one list that is composed of all lists.
    """
    lst2 = []
    for l in lst_of_lists:
        lst2.extend(l)
    return lst2

add_break_and_title("flatten_lists")
lst_of_lists = []
lst2 = flatten_lists(lst_of_lists)
print("{:>40} => {:<40}".format(str(lst_of_lists), str(lst2)))
lst_of_lists = [[]]
lst2 = flatten_lists(lst_of_lists)
print("{:>40} => {:<40}".format(str(lst_of_lists), str(lst2)))
lst_of_lists = [[1, 2, 3]]
lst2 = flatten_lists(lst_of_lists)
print("{:>40} => {:<40}".format(str(lst_of_lists), str(lst2)))
lst_of_lists = [["cat", "dog"], ["pig", "cow"]]
lst2 = flatten_lists(lst_of_lists)
print("{:>40} => {:<40}".format(str(lst_of_lists), str(lst2)))
lst_of_lists = [[9, 8, 7], [6, 5], [4, 3, 2], [1]]
lst2 = flatten_lists(lst_of_lists)
print("{:>40} => {:<40}".format(str(lst_of_lists), str(lst2)))

def remove_duplicate_elems(lst):
    """
    Returns a list of unique values.
    """
    updated = []
    for l in lst:
        if l not in updated:
            updated.append(l)
    return updated

add_break_and_title("remove_duplicate_elems")
orig = []
updated = remove_duplicate_elems(orig)
print("{:>60} => {:<60}".format(str(orig), str(updated)))
orig = [1, 2, 3, 4]
updated = remove_duplicate_elems(orig)
print("{:>60} => {:<60}".format(str(orig), str(updated)))
orig = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6]
updated = remove_duplicate_elems(orig)
print("{:>60} => {:<60}".format(str(orig), str(updated)))
orig = ["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]
updated = remove_duplicate_elems(orig)
print("{:>60} => {:<60}".format(str(orig), str(updated)))

def fib(lst, count):
    """
    Returns the sum after adding the total of the last two items to the list.
    """
    fibonacci = []
    total = 0
    inner_cnt = 0
    for c in range(count):
        # this loop is the iteration we are interested because it
        # loops twice for the last and last-1 positions.
        for i in lst[-2:]:
            total = total + i
            fibonacci.append(total)
            lst = list(fibonacci)
            inner_cnt = inner_cnt + 1
            print("iteration: " + str(inner_cnt) + " : " + str(total) + " : " + str(lst))
    return fibonacci

add_break_and_title("fibonacci")
orig_fib = [0,1,1]
print("Original list: " + str(orig_fib))
itr = 10
print("fibonacci sum after iterations: " + str(itr))
print(fib(orig_fib,itr))

"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound) and
    length of list.

    Usage:
    compute_primes(bound)
        where bound is an integer > 1.

    """
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        n = divisor + 1
        for nxt in range(n,bound):
            # Remove appropriate multiples of divisor from answer
            if (nxt % divisor == 0):
                if nxt in answer:
                    idx = answer.index(nxt)
                    if idx > -1:
                        del answer[idx]
    return answer

add_break_and_title("compute_primes")
number = 200
print("find primes for " + str(number))
print("Size of list: " + str(len(compute_primes(number))))
print(compute_primes(number))
number = 2000
print("find primes for " + str(number))
print("Size of list: " + str(len(compute_primes(number))))
print(compute_primes(number))

def is_exists(my_dict, ky):
    """
    Returns True if the key exists in the dictionary.

    Usage:
    is_exists(my_dict, ky)
    where my_dict is a non-empty dictionary
          ky is a value to test.
    """
    return ky in my_dict

add_break_and_title("is_exists")
my_dict_ = {'Joe':1, 'Scott': 2, 'John':3}
print("Original dictionary: " + str(my_dict_))
nm = 'Joe'
print("{:>30} {:10}".format(nm + " is in my_dict: ", str(is_exists(my_dict_, nm))))
nm = 'Scott'
print("{:>30} {:10}".format(nm + " is in my_dict: ", str(is_exists(my_dict_, nm))))
nm = 'John'
print("{:>30} {:10}".format(nm + " is in my_dict: ", str(is_exists(my_dict_, nm))))
nm = 'James'
print("{:>30} {:10}".format(nm + " is in my_dict: ", str(is_exists(my_dict_, nm))))

def is_empty(my_dict):
    """
    Returns True if the dictionary is empty.

    Usage:
    is_empty(my_dict)
    where my_dict is a dictionary reference.
    """
    return len(my_dict) == 0

add_break_and_title("is_empty")
my_dict_ = {'Joe':1, 'Scott': 2, 'John':3}
print("Original dictionary: " + str(my_dict_))
print("{:>20} {:10}".format("my_dict is empty: ", str(is_empty(my_dict_))))
my_dict_ = {}
print("Original dictionary: " + str(my_dict_))
print("{:>20} {:10}".format("my_dict is empty: ", str(is_empty(my_dict_))))

def value_sum(my_dict):
    """
    Returns the sum of value in the dictionary.

    Usage:
    value_sum(my_dict)
    where my_dict is a dictionary of values of integer type.

    """
    total = 0
    for k,v in my_dict.items():
        total += v

    return total

add_break_and_title("value_sum")
my_dict_ = {'Joe':1, 'Scott': 2, 'John':3}
print("Original dictionary: " + str(my_dict_))
print("{:>20} {:10}".format("Sum of value in my_dict_: ", str(value_sum(my_dict_))))

my_dict_ = {'Joe':1, 'Scott': 0, 'John':0}
print("Original dictionary: " + str(my_dict_))
print("{:>20} {:10}".format("Sum of value in my_dict_: ", str(value_sum(my_dict_))))

def make_dict(key_value_list):
    """
    Returns a dictionary converted from the list of tuples.

    Usage:
    make_dict(key_value_list)
    where key_value_list is a list of tuples with each
        tuple contains a key,value pair.
    """
    return dict(key_value_list)

add_break_and_title("make_dict")
my_tuples = [('Joe',1),('Scott',2),('John',3)]
print("Original list: " + str(my_tuples))
print("{:>20} {:10}".format("my_tuples converted to dict: ", str(make_dict(my_tuples))))

my_tuples = [('Joe',0),('Scott',-1),('John',99)]
print("Original list: " + str(my_tuples))
print("{:>20} {:10}".format("my_tuples converted to dict: ", str(make_dict(my_tuples))))


