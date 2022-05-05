# Filename: 1-variables.py
# Created By: Mackenly Jones on 05/05/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

"""
Programming languages typically allow you to assign a value to a variable.
You can then do processing on that value and even assign it to another variable.

If you remember back to Algebra class you probably learned about vairables by solving for x.
Variables in programming are similar to algebraic variables, but instead they can hold different types of data.
"""

# Let's create a variable and assign it a value
x = 5
print(x)
# You can also assign a value to a variable using the assignment operator which is =

"""
Python is what we called a loosely typed language. Loosely typed languages allow you to assign a value to a variable
of any type. This can make it a bit complicated at scale but help simplify the code when you're just starting out.

In Python there are a few key data types you should know when starting out:
1. Numbers
2. Strings
3. Lists
4. Tuples
5. Dictionaries

We will go into the other later on, but for now let's look at Numbers and Strings.

In computer science there are two main types of numbers: Integers and Floats.
An integer is a whole number, like 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
A float is a number with a decimal point, like 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0.

All integers can be represented as a float since 1.0 is equal to 1.
But most floats can't be represented as an integer since 1.3 is not equal to 1.

Let's try working with some numbers in Python...
"""

# First let's print a simple example of a number
print(1)
print(1.0)

# Pretty easy, right?
# Let's try adding some numbers together
print(1 + 1)

# Notice how we get a float back
print(1.0 + 1)

"""
Now, let's look into strings.
Strings are sequences of characters. Characters are single units of data. Examples of characters are: A, b, C, 2, @, etc
Strings are surrounded by either single or double quotes. 
"""

string1 = "Hello"
string2 = 'world'

# You can also create strings over multiple lines
string3 = """
This is a string
that spans
multiple lines
"""

"""
Strings can be concatenated with the concatenation operator, which is +.
"""

# Notce how an extra space is added between the two strings.
# We we concatenate a string it puts together the value of the strings (which didn't have a space between them)
string3 = string1 + " " + string2 + " " + string3 + "!"
print(string3)
