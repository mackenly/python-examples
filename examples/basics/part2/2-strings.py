# Filename: 2-strings.py
# Created By: Mackenly Jones on 05/05/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

"""
As we discovered in the last lesson, strings along with variables can be very powerful.
In this lesson, we will learn how to manipulate strings.

You may be wondering, how do you add line breaks and spacing between your prints?
In Python you can use \n inside a string to insert a line break.
You can also use \t to insert a tab.

For example...
"""

print("Hello\nWorld")
print("Hello\tWorld")

# You can add line breaks to strings stored in variables too!
b = "Hello world! The quick brown \nfox jumped over \nthe lazy dog."
print(b)

# You may want to add multiple line breaks in your text like this:
c = "\nHello world!\n\n\nThe quick brown fox jumped over the lazy dog."
print(c)

"""
As you noticed in the previous example, the \ character can be used to do special things in strings.
That character is called an escape character. It is used to tell Python that you want to do something special.

Along with being able to create new lines and tabs, you can also use the \n, \t, \b, \f, \r, \v, 
\\, \", \', and \ooo to insert special characters.

When you escape a character, you must use a backslash before it.
For example, when you use a " in a string, you must use a \" to escape it.
Normally when you use a " in a string, Python will treat it as the end of your 
string since strings are enclosed inside "". Here's an example:
"""

print("Hello \"World\"")

"""
There are special methods that you can use to manipulate strings.
Here are some of the most common ones:
"""

# Let's create a string that we can manipulate:
d = "Hello world! "

print(d.upper())  # prints HELLO WORLD!
print(d.lower())  # prints hello world!
print(d.capitalize())  # prints Hello world!
print(d.title())  # prints Hello World!
print(d.swapcase())  # prints hELLO wORLD!
print(d.replace("world", "universe"))  # prints Hello universe!
print(d.count("l"))  # prints the number of l's in the string
print(d.strip())  # prints Hello world! without the spaces at the beginning and end
print(d.split(",")[0])  # prints Hello by splitting the string at the comma and taking the first element

"""
Python allows you to format string with variables.
There's an old way and a new way. First let's look at the old way.
"""
price = 10
print("The price of the product is {} and my name is {}".format(price, "Mackenly"))

# New preferred way:
print(f"The price of the product is {price} and my name is {'Mackenly'}")

"""
Finally, let's look at how you can access the characters in a string.
Strings are indexed by numbers starting at 0. For example, the first character in the string is at index 0.
We can look into a string by specifying where we want inside brackets.
Here's an example:
"""
name = "Mackenly"
print(name[0])  # prints M
print(name[1])  # prints a
print(name[0:4])  # prints Mack
print(name[:4])  # prints Mack
print(name[5:])  # prints nly
print(name[-1])  # prints y

# And to get the length of a string, you can use the len() function:
print(len(name))  # prints 8
