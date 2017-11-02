# Single line comments start with a number symbol.


""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""

"""
Author: Mario Negrete
Institution: CIMAT
HW: 3

"""

####################################################
# 1. Primitive Datatypes and Operators
####################################################

# You have numbers
3  # => 3

# Math is what you would expect
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
5 / 2  # => 2

# To fix division we need to learn about floats.
2.0  # This is a float
11.0 / 4.0  # => 2.75 ahhh...much better

# Result of integer division truncated down both for positive and negative.
5 // 3  # => 1
5.0 // 3.0  # => 1.0 # works on floats too
-5 // 3  # => -2
-5.0 // 3.0  # => -2.0

# Note that we can also import division module(Section 6 Modules)
# to carry out normal division with just one '/'.
from __future__ import division

11 / 4  # => 2.75  ...normal division
11 // 4  # => 2 ...floored division

# Modulo operation
7 % 3  # => 1

# Exponentiation (x to the yth power)
2 ** 4  # => 16

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True  # => True

# Note using Bool operators with ints
0 and 2  # => 0
-5 or 0  # => -5
0 == False  # => True
2 == True  # => False
1 == True  # => True

# negate with not
not True  # => False
not False  # => True

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparisons can be chained!
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too!
"Hello " + "world!"  # => "Hello world!"
# Strings can be added without using '+'
"Hello " "world!"  # => "Hello world!"

# ... or multiplied
"Hello" * 3  # => "HelloHelloHello"

# A string can be treated like a list of characters
"This is a string"[0]  # => 'T'

# You can find the length of a string
len("This is a string")  # => 16

# String formatting with %
# Even though the % string operator will be deprecated on Python 3.1 and removed
# later at some time, it may still be good to know how it works.
x = 'apple'
y = 'lemon'
z = "The items in the basket are %s and %s" % (x, y)

# A newer way to format strings is the format method.
# This method is the preferred way
"{} is a {}".format("This", "placeholder")
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
"etc" is None  # => False
None is None  # => True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.

# Any object can be used in a Boolean context.
# The following values are considered falsey:
#    - None
#    - zero of any numeric type (e.g., 0, 0L, 0.0, 0j)
#    - empty sequences (e.g., '', (), [])
#    - empty containers (e.g., {}, set())
#    - instances of user-defined classes meeting certain conditions
#      see: https://docs.python.org/2/reference/datamodel.html#object.__nonzero__
#
# All other values are truthy (using the bool() function on them returns True).
bool(0)  # => False
bool("")  # => False
