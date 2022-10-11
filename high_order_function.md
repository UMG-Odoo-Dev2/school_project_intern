# Higher Order Functions in Python

A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as a parameter or returns a function as a result. Python too supports the concepts of higher order functions.

## Properties of higher-order functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …

## Functions as objects
In Python, a function can be assigned to a variable. This assignment does not call the function, instead a reference to that function is created. Consider the below example, for better understanding.

<b>Example:</b>

```py
# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()
	
print(shout('Hello'))
	
# Assigning function to a variable
yell = shout
	
print(yell('Hello'))
```

Output:

HELLO<br>
HELLO

In the above example, a function object referenced by shout and creates a second name pointing to it, yell.

## Passing Function as an argument to other function
Functions are like objects in Python, therefore, they can be passed as argument to other functions. Consider the below example, where we have created a function greet which takes a function as an argument.

<b>Example:</b>

```py
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()
	
def whisper(text):
	return text.lower()
	
def greet(func):
	# storing the function in a variable
	greeting = func("Hi, I am created by a function \
	passed as an argument.")
	print(greeting)
	
greet(shout)
greet(whisper)
```

Output:

    HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
    hi, i am created by a function passed as an argument.

## Returning function
As functions are objects, we can also return a function from another function. In the below example, the create_adder function returns adder function.

<b>Example:</b>
```py
# Python program to illustrate functions
# Functions can return another function
	
def create_adder(x):
	def adder(y):
		return x + y
	
	return adder
	
add_15 = create_adder(15)
	
print(add_15(10))

```