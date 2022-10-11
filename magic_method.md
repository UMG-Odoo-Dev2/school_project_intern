# <b>Introduction to Python Magic Method</b>

<p>Magic methods are a collection of pre-defined functional method from the python library functions that cannot be declared or called directly. Instead, these functions can be called or invoked by executing some other related code snippet methods. This type of methods are simple to use and implement, as it does not require specific or any kind of extra manual effort from the programmer. Hence it is named as the ‘Magic Method’.</p>

## What is Python Magic Method?
- Python is an interpreted, object-oriented programming that gives you the ability to write procedural code and/or object-oriented as we know that creating Objects simplifies complicated data structures handling. In addition to that, magic methods eases the ability to create object-oriented programming.
- Before Diving into a magic method, let’s understand why they are created in the first place, they are created?
- Below is one example of class one using a magic method and the other is without the magic method. In the first one __init__ magic method is used, which can be used to initialize more than one instance variable in one go. A class Sports is defined as taking two instance variables into account that is name and sport.
- Both instance variables can be defined in one go using the __inti__ magic method. In case 2, the same thing is repeated, but this time we are using a set method to initialize the instance variable. Here for 2 variables, we have to call this method twice.

## Python Magic Methods
Python has many built-in magic methods to name some are:

    __init__
    __new__
    __del__
    __abs__
    __add__
    __sub__
    __mul__
We will discuss some of the magic methods to understand it better.

Now let’s take the __ to add__ magic method:

```py
    A=5
    A+3
```
Output: 8

The same can be performed with the __add__ magic method.

    A.__add__(5)

Output: 10

## Object Constructor and Initialiser
Magic Methods are used widely in python programming basics in class construction and Initialization.
As we have discussed __init__ magic method. This method has been used to define the initialization of an object in the class.
__init__ is not the first method to be invoked for object creation; however, the first magic method __new__ is invoked, which creates a new instance and then calls __init__ magic method.
Let’s See the example of the same:

```py 
class AbstractClass(object):
    def __new__(cls, a, b):
        print("calling magic method__new__")
        instance = super(AbstractClass, cls).__new__(cls)
        instance.__init__(a, b)
    def __init__(self, a, b):
        print('calling magic method__init__')
        print ("Initializing Instance", a, b)
a=AbstractClass(2,3)
```
Output:

    calling magic method__new__

    calling magic method__init__

    Initializing Instance 2 3

</br>

    __new__ can be used in a wide variety of ways, but this shows a simple example of this magic method.

## Comparison Magic methods
Python has a number of magic methods that are designed to do intuitive comparisons between objects with the use of operators.

Some are listed below:

    __lt__(self, other): is used to be called on comparison using < operator.
    __le__(self, other): is used to be called on comparison using <= operator.
    __eq__(self, other): is used to be called on comparison using == operator.
    __ne__(self, other): is used to be called on comparison using != operator.
    __ge__(self, other): is used to be called on comparison using >= operator.
## Infix Operators
Python has typical built-in binary operators as magic methods.

Some are listed below:

    __add__ (self, other): for addition
    __sub__ (self, other): for subtraction
    __mul__(self, other): for multiplication
## Advantages of Python Magic Method
Python provides “magic methods” because they really perform magic for your program.

The biggest advantages are:

It provides a simple way to make objects behave like built-in types, which means one can avoid counter-intuitive or nonstandard ways of performing basic operators. For e.g.,

we have two dictionaries, ‘dicta’ and ‘dicta.’
```PY
dicta = {1 : "XYZ"}
dictb = {2 : "LMN"}
dict1 + dict2
```
Output:

        Traceback (most recent call last):
            File"main.py", line 3, in <module>
                dict1 + dict2
            NameError: name 'dict1' is not defined

## Advantages of Python Magic Method 1
Now, this ends up with a type error because the dictionary type doesn’t support addition. Now, we can extend the dictionary class and add “__add__” magic method:
```py
class AddDict(dict):
    def __add__(self, dicts):
        self.update(dicts)
        return AddDict(self)
dicta = AddDict({1 : "XYZ"})
dictb = AddDict({2 : "LMN"})
print (dicta + dictb)
```
Now, we are getting the desired output.

    {1: 'XYZ', 2: 'LMN'}

Thus, suddenly magic happened just by adding a magic method. The error vanished, which we were getting earlier.

## Conclusion
Magic methods are invoked indirectly and are identified with dunders or double underscores like __add__. To better use Python classes, one must know at least some magic method like __init__, __new__. Comparison operator magic methods give python an edge where instances of objects can be compared for equality as well as inequality. In a nutshell magic method do magic to python programming by reducing complexity.
