# python like nearly every programming language uses a variety of datatypes
# variables can be used to assign values to them and make programming a lot simpler

# the left side is a variable called 'num1' and the right side is the value '123' that is assigned to it
num1 = 123

# whenever 'num1' is used on the right side or within a function like print it will have the same meaning as it's
# associated value
# therefore the following two print statements should have the same result
print(num1)
print(123)

# it is also possible to overwrite the associated value, simply by using the 'num1 = some value' syntax
num1 = 1000
print(num1)  # -> will now print 1000 instead of 123

# there are a few datatypes in python:

num2 = 1000  # -> this is an integer (whole number)

num3 = 1.1   # -> float (has a whole number part as well as a fractional part)
# (in case you are interested in how float numbers work you can also watch the following video:)
# https://youtu.be/RuKkePyo9zk

b1 = True    # -> boolean (True or False)

s1 = "Hello World"  # -> String, some text

# -----------------------------------------------------------------------------------------------
# as you might have already noticed python doesn't require you to clarify which datatype a value is
# but finds out on its own
# the newer python versions allow you to set an expected datatype which resembles other typical programming languages
# use this whenever you can since it makes development and code maintenance easier
num4: int = 10        # the ': int' signals that we expect an integer value
num5: float = 2.15    # float
b2: bool = False      # boolean
s2: str = "Meow"      # string

# -----------------------------------------------------------------------------------------------
# you can check the datatype of a value by using the type() function which will return the datatype
print(type(2))        # should print: <class 'int'>
