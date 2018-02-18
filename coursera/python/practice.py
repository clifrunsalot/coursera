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


add_break_and_title("encrypt")

# Part 1 - Use a dictionary that represents a substition cipher to
# encrypt a phrase
# Example of a cipher dictionary 26 lower case letters plus the blank
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def encrypt(phrase, cipher_dict):
    """
    Take a string phrase (lower case plus blank)
    and encypt it using the dictionary cipher_dict

    Usage:
    encrypt(phrase, cipher_dict)
    where phrase is the string to encrypt and
        cipher_dict is the dictionary letters and their corresponding
        values.
    """
    ret_val = ""
    for c in phrase:
        ret_val += cipher_dict[c]
    return ret_val

plain_text = "pig"
print(plain_text + " encrypted into " + str(encrypt(plain_text, CIPHER_DICT)))
plain_text = "hello world"
print(plain_text + " encrypted into " + str(encrypt(plain_text, CIPHER_DICT)))

add_break_and_title("make_decipher_dict")

def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher

    Usage:
    make_decipher_dict(cipher_dict)
    where cipher_dict is the original cipher.
    """
    ret_val = {}
    for k,v in cipher_dict.items():
        ret_val[v] = k
    return ret_val

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

print("CIPHER_DICT: " + str(CIPHER_DICT))
print("DECIPHER_DICT: " + str(DECIPHER_DICT))
plain_text = "pig"
enc = encrypt(plain_text, CIPHER_DICT)
dec = encrypt(encrypt(plain_text, CIPHER_DICT), DECIPHER_DICT)
print("{:>15} encrypted to {:15}".format(plain_text, enc))
print("{:>15} decrypted to {:15}".format(enc, dec))

plain_text = "hello world"
enc = encrypt(plain_text, CIPHER_DICT)
dec = encrypt(encrypt(plain_text, CIPHER_DICT), DECIPHER_DICT)
print("{:>15} encrypted to {:15}".format(plain_text, enc))
print("{:>15} decrypted to {:15}".format(enc, dec))

add_break_and_title("count_letters")

def count_letters(word_list):
    """
    This function should return the lower case letter that appears
    most frequently (total number of occurrences) in the words in
    word_list. In the case of ties, return the earliest letter in
    alphabetical order.

    Usage:
    count_letters(word_list)
    where word_list is a list of words.

    """
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0

    ltr_sum = 0;
    for wd in word_list:
        for ch in wd:
            letter_count[ch] += 1

    return letter_count

my_list = ['hello','world']
my_count = count_letters(my_list)
print("Original list: " + str(my_list))
print("dict of letter counts: " + str(my_count))

my_count_clean = {}
for k,v in my_count.items():
    if v > 0:
        my_count_clean[k] = v

print(my_count)
print(my_count_clean)

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
my_list = monty_quote.split(" ")
my_count = count_letters(my_list)
print("Original list: " + str(my_list))
print("dict of letter counts: " + str(my_count))

my_count_clean = {}
for k,v in my_count.items():
    if v > 0:
        my_count_clean[k] = v

print(my_count)
print(my_count_clean)

add_break_and_title("Tables: Lists of Lists")

popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
                ["Java", 1 ,2, 1, 1, 15, 0, 0],
                ["C", 2, 1, 2, 2, 1, 1, 1],
                ["C++", 3, 3, 3, 3, 2, 2, 5],
                ["C#", 4, 4, 7, 13, 0, 0, 0],
                ["Python", 5, 7, 6, 11, 27, 0, 0],
                ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
                ["PHP", 7, 6, 4, 5, 0, 0, 0],
                ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
                ["Perl", 9, 8, 5, 4, 4, 10, 0]]

print("Original table:")
print(popularity)
print("")
print("Formatted table: ")
format_string = "{:<18} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4} {:>4}"
headers = popularity[0]
header_row = format_string.format(*headers)
print(header_row)
print("-" * len(header_row))
for lang in popularity[1:]:
    print(format_string.format(*lang))

def find_row(table, lang):
    """
    Returns the row index for lang in table.
    """
    row = -1
    for row in range(len(table)):
        if lang in table[row][0]:
            return row
    return row

add_break_and_title("find_row")
lang = "Java"
print("Row for " + str(lang) + " in popularity table")
print(find_row(popularity, lang))

lang = "Perl"
print("Row for " + str(lang) + " in popularity table")
print(find_row(popularity, lang))

def find_col(table, year):
    """
    Returns the column index for the year in the table.
    """
    return table[0].index(year)

add_break_and_title("find_col")
yr = 2017
print("column for " + str(yr) + " in popularity table")
print(find_col(popularity, yr))

yr = 2012
print("column for " + str(yr) + " in popularity table")
print(find_col(popularity, yr))

yr = 2002
print("column for " + str(yr) + " in popularity table")
print(find_col(popularity, yr))

lang = "C++"
yr = 1997
rw = find_row(popularity,lang)
cl = find_col(popularity,yr)
print("Popularity of " + str(lang) + " in the year " + str(yr) + ": "
    + str(popularity[rw][cl]))

lang = "Python"
yr = 2012
rw = find_row(popularity,lang)
cl = find_col(popularity,yr)
print("Popularity of " + str(lang) + " in the year " + str(yr) + ": "
    + str(popularity[rw][cl]))

add_break_and_title("Tables: Dictionary of Dictionaries")

my_dict = {
    'Android':{'vendor':'Google',
                'type':'Operating System',
                'number': 564},
    'Linux Kernel':{'vendor':'Linux',
                    'type':'Operating System',
                    'number': 367},
    'Imagemagick':{'vendor':'Imagemagick',
                    'type':'Application',
                    'number':307}
}

print("Original dictionary: ")
print(my_dict)
print("")
print("Formatted dictionary: ")
print("{:20} {:15} {:20} {:5}".format("Product","Vendor","Type","Number"))
print("-" * (20+15+20+15))
for product, value in my_dict.items():
    row = "{:20} {:15} {:20} {:5}".format(product, value['vendor'], value['type'], value['number'])
    print(row)
print("")
os = 'Linux Kernel'
val = 'vendor'
print("Find " + val + " value of the os " + os)
print(my_dict[os][val])
os = 'Imagemagick'
val = 'number'
print("Find " + val + " value of the os " + os)
print(my_dict[os][val])

def find_greatest_number(my_dict):
    """
    Returns the greatest number in my_dict.
    """
    max_nbr = 0;
    max_pdt = None;

    for product, values in my_dict.items():
        if values['number'] > max_nbr:
            max_nbr = values['number']
            max_pdt = product
    return (max_pdt, max_nbr)

add_break_and_title("find_greatest_number")
prd_nbr = find_greatest_number(my_dict)
print(prd_nbr[0])

add_break_and_title("dict_copies")

def dict_copies(my_dict_, num_copies_):
    """
    Given a dictionary my_dict and an integer num_copies,
    returns a list consisting of num_copies of my_dict.
    """
    my_list = []
    for cp in range(num_copies_):
        my_list.append(dict(my_dict_))

    return my_list

my_dict = {'a':1, 'b':2}
print("Original dictionary")
print(my_dict)
print("dictionary copies")
num_cpy = 0
print(dict_copies(my_dict, num_cpy))
num_cpy = 1
print(dict_copies(my_dict, num_cpy))
num_cpy = 2
print(dict_copies(my_dict, num_cpy))
num_cpy = 3
print(dict_copies(my_dict, num_cpy))
print("check for reference issues")
print("original dic")
test_dict = dict_copies(my_dict, num_cpy)
print(test_dict)
print("changing a value with")
print("test_dict[1]['a']=3")
test_dict[1]['a']=3
print("Afterwards. No issues if only one of the 'a' values matches the change")
print(test_dict)

add_break_and_title("make_grade_table")

students = ['Joe','Scott','John']
grades = [['Joe',100,98,100,13],
            ['Scott',75,59,89,77],
            ['John',86,84,91,78]]

def make_grade_table(name_list, grades_list):
    """
    Takes list of names name_list and list of grade grades_list
    and returns a dictionary whose keys corresponds to names
    name_list and whose corresponding values are the items grades_list.
    """
    out_dict={}
    for name, grades in zip(name_list, grades_list):
        if name == grades[0]:
            out_dict[name] = list(grades[1:])
    return out_dict

print("Original student grade list")
for s in grades:
    print(s)
grades_table_dict = make_grade_table(students, grades)
print("Formatted student grade list converted into a dictionary")
print("{:10} {:10} {:10} {:10} {:10}".format("Student","Assign #1","Assign #2","Assign #3","Assign #4"))
print("-" * (10*6))
for k,v in grades_table_dict.items():
    rw = "{:10} {:10} {:10} {:10} {:10}".format(k,*v)
    print(rw)

NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)
 
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end = " ")
    print()
    
matrix_3 = {1: {1: 2, 7: 2, 3: 2, 8: 2, 0: 2, 5: 2, 2: 2, 6: 2, 4: 2}, 2: {5: 4, 1: 4, 8: 4, 0: 4, 3: 4, 2: 4, 4: 4, 7: 4, 6: 4}, 3: {4: 6, 2: 6, 1: 6, 5: 6, 0: 6, 7: 6, 8: 6, 3: 6, 6: 6}, 0: {0: 0, 5: 0, 6: 0, 8: 0, 1: 0, 3: 0, 2: 0, 4: 0, 7: 0}, 4: {3: 8, 8: 8, 7: 8, 5: 8, 4: 8, 1: 8, 2: 8, 6: 8, 0: 8}}
if my_matrix == matrix_3:
	print("matrix_3 matches")
	
matrix_4 = {1: {7: 7, 4: 4, 3: 3, 8: 8, 6: 6, 5: 5, 2: 2, 0: 0, 1: 1}, 0: {0: 0, 7: 0, 3: 0, 4: 0, 8: 0, 6: 0, 5: 0, 1: 0, 2: 0}, 2: {0: 0, 8: 16, 5: 10, 2: 4, 7: 14, 4: 8, 1: 2, 3: 6, 6: 12}, 3: {1: 3, 7: 21, 2: 6, 8: 24, 3: 9, 4: 12, 6: 18, 0: 0, 5: 18}, 4: {3: 12, 7: 28, 0: 0, 2: 8, 1: 4, 4: 16, 6: 24, 5: 20, 8: 32}}
if my_matrix == matrix_4:
	print("matrix_4 matches")

matrix_1 = {2: {6: 12, 2: 4, 0: 0, 7: 14, 5: 10, 3: 6, 8: 16, 4: 8, 1: 2}, 4: {0: 0, 3: 12, 2: 8, 6: 24, 4: 16, 5: 20, 8: 32, 7: 28, 1: 4}, 1: {2: 2, 5: 5, 3: 3, 8: 8, 4: 4, 1: 1, 7: 7, 0: 0, 6: 6}, 3: {4: 12, 0: 0, 8: 24, 6: 18, 7: 21, 3: 9, 5: 15, 1: 3, 2: 6}, 0: {8: 0, 1: 0, 6: 0, 2: 0, 4: 0, 5: 0, 3: 0, 0: 0, 7: 0}}
if my_matrix == matrix_1:
	print("matrix_1 matches")
	
matrix_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 2, 4, 6, 8, 10, 12, 14, 16], [0, 3, 6, 9, 12, 15, 18, 21, 24], [0, 4, 8, 12, 16, 20, 24, 28, 32]]
if my_matrix == matrix_2:
	print("matrix_2 matches")


add_break_and_title("Calculate trace value a square matrix")

def construct_square_matrix(num):
	"""
	Returns a matrix with equal rows and columns.
	"""
	my_matrix = []
	for row in range(num):
		new_row = []
		for col in range(num):
			new_row.append(row * col)
		my_matrix.append(new_row)
	return my_matrix

def print_matrix(matrix):
	"""
	Pretty prints a matrix.
	"""
	for row in my_matrix:
		cols = len(my_matrix[0])
		spacer = "{:4} " * cols
		print(spacer.format(*row))

def trace(matrix):
	"""
	Calculates the trace value of the square matrix provided, which 
	means taking the sum of all values in the diagonal created
	in the squared matrix.
	"""
	trace_val = 0;
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if row == col:
				trace_val += matrix[row][col]
	return trace_val
	
# construct a matrix
NUM_ROWS = 5
NUM_COLS = NUM_ROWS
print("Constructing square matrix of " + str(NUM_ROWS) + "x" + str(NUM_COLS))
my_matrix = construct_square_matrix(NUM_ROWS)
print("Original matrix")
print(my_matrix)
print("Formatted matrix")
print_matrix(my_matrix)    
print("The trace value: " + str(trace(my_matrix)))

NUM_ROWS = 6
NUM_COLS = NUM_ROWS
print("Constructing square matrix of " + str(NUM_ROWS) + "x" + str(NUM_COLS))
my_matrix = construct_square_matrix(NUM_ROWS)
print("Original matrix")
print(my_matrix)
print("Formatted matrix")
print_matrix(my_matrix)    
print("The trace value: " + str(trace(my_matrix)))

NUM_ROWS = 7
NUM_COLS = NUM_ROWS
print("Constructing square matrix of " + str(NUM_ROWS) + "x" + str(NUM_COLS))
my_matrix = construct_square_matrix(NUM_ROWS)
print("Original matrix")
print(my_matrix)
print("Formatted matrix")
print_matrix(my_matrix)    
print("The trace value: " + str(trace(my_matrix)))

NUM_ROWS = 25
NUM_COLS = NUM_ROWS
print("Constructing square matrix of " + str(NUM_ROWS) + "x" + str(NUM_COLS))
my_matrix = construct_square_matrix(NUM_ROWS)
print("Original matrix")
print(my_matrix)
print("Formatted matrix")
print_matrix(my_matrix)    
print("The trace value: " + str(trace(my_matrix)))
