# Python - Magic or Dunder Methods

Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the ```__add__()``` method will be called.

Built-in classes in Python define many magic methods. Use the dir() function to see the number of magic methods inherited by a class. For example, the following lists all the attributes and methods defined in the int class. 
```bash
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'] 
```
As you can see above, the int class includes various magic methods surrounded by double underscores. For example, the ```__add__``` method is a magic method which gets called when we add two numbers using the + operator. Consider the following example.
```bash
>>> num=10
>>> num + 5
15
>>> num.__add__(5)
15 
```
 As you can see, when you do num+10, the + operator calls the ```__add__```(10) method. You can also call num.```__add__```(5) directly which will give the same result. However, as mentioned before, magic methods are not meant to be called directly, but internally, through some other methods or actions.

Magic methods are most frequently used to define overloaded behaviours of predefined operators in Python. For instance, arithmetic operators by default operate upon numeric operands. This means that numeric objects must be used along with operators like +, -, *, /, etc. The + operator is also defined as a concatenation operator in string, list and tuple classes. We can say that the + operator is overloaded.

In order to make the overloaded behaviour available in your own custom class, the corresponding magic method should be overridden. For example, in order to use the + operator with objects of a user-defined class, it should include the ```__add__()```method.

Let's see how to implement and use some of the important magic methods.

## ```__new__() ```method

Languages such as Java and C# use the new operator to create a new instance of a class. In Python the ```__new__()``` magic method is implicitly called before the ```__init__()``` method. The ```__new__()``` method returns a new object, which is then initialized by ```__init__()```. 

### Example: ```__new__()```
```bash


    class Employee:
        def __new__(cls):
            print ("__new__ magic method is called")
            inst = object.__new__(cls)
                    return inst
        def __init__(self):
            print ("__init__ magic method is called")
            self.name='Satya'

```
The above example will produce the following output when you create an instance of the Employee class.
```bash
>>> emp = Employee()
__new__ magic method is called
__init__ magic method is called 
```
Thus, the ```__new__()``` method is called before the ```__init__()``` method.
```__str__()``` method

Another useful magic method is ```__str__()```. It is overridden to return a printable string representation of any user defined class. We have seen str() built-in function which returns a string from the object parameter. For example, str(12) returns '12'. When invoked, it calls the ```__str__()``` method in the int class. 
```bash
>>> num=12
>>> str(num)
'12'
>>> #This is equivalent to
>>> int.__str__(num)
'12' 
```
 Let us now override the __str__() method in the Employee class to return a string representation of its object.
Example: ```__str__()```
```bash
class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)
```

See how the str() function internally calls the __str__() method defined in the Employee class. This is why it is called a magic method!
```bash
>>> e1=Employee()
>>> print(e1)
name=Swati salary=$10000
```
## ```__add__() ```method

 In following example, a class named distance is defined with two instance attributes - ft and inch. The addition of these two distance objects is desired to be performed using the overloading + operator.

To achieve this, the magic method ```__add__()``` is overridden, which performs the addition of the ft and inch attributes of the two objects. The ```__str__()``` method returns the object's string representation.
Example: Override ```__add__()```
```bash

    class distance:
        def __init__(self, x=None,y=None):
            self.ft=x
            self.inch=y
        def __add__(self,x):
            temp=distance()
            temp.ft=self.ft+x.ft
            temp.inch=self.inch+x.inch
            if temp.inch>=12:
                temp.ft+=1
                temp.inch-=12
                return temp
        def __str__(self):
            return 'ft:'+str(self.ft)+' in: '+str(self.inch)
```
 Run the above Python script to verify the overloaded operation of the + operator.
 ```bash
>>> d1=distance(3,10)
>>> d2=distance(4,4)
>>> print("d1= {} d2={}".format(d1, d2))
d1= ft:3 in: 10 d2=ft:4 in: 4
>>> d3=d1+d2
>>> print(d3)
ft:8 in: 2

```
## ```__ge__() method```

The following method is added in the distance class to overload the >= operator. 

### Example: ```__ge__()```
```bash
    class distance:
        def __init__(self, x=None,y=None):
            self.ft=x
            self.inch=y
        def __ge__(self, x):
            val1=self.ft*12+self.inch
            val2=x.ft*12+x.inch
            if val1>=val2:
                return True
            else:
                return 
```

This method gets invoked when the >= operator is used and returns True or False. Accordingly, the appropriate message can be displayed
```bash
>>> d1=distance(2,1)
>>> d2=distance(4,10)
>>> d1>=d2
False 
```
# Magic Method Syntax

A method that is wrapped by two underscores on both sides is called Magic Methods. The motive behind the magic method is to overload Python’s built-in methods and its operators. Here, _syntax prevents the programmers from defining the same name for custom methods. Each magic method serves its purpose. Let’s consider an example that checks for equivalence. Example: 

```bash
    class EquivalenceClass(object):
        def __eq__(self, other):
            return type(self) == type(other)
    
    print(EquivalenceClass() == EquivalenceClass())
    print(EquivalenceClass() == 'MyClass')

Output

True
False
```
The ```__eq__  ``` method takes two arguments – self and the object – to check equality. What is important to understand is, __eq__ method is invoked when the two objects are compared using the == operator. Let’s go through some of the common magic methods in python.

# Common Magic Methods

In Python, we have a diverse range of magic methods – each serves its purpose. Here we will comb through, a few of the common magic methods:

    Creation
    Destruction
    Type Conversion
    Comparisons

## Creation

Magic Methods entangled in creation, are performed when a class instance is created. Two of the magic methods associated are ```__init__``` and ```__new__ ```methods.
```__init__ ```method

The ```__init__``` method of an object executes right away after the instance creation. Here, the method takes one positional argument – self – and any number of optional or keyword arguments. Let’s look into a simple example: Example: 
```bash
    class InitClass(object):
        def __init__(self):
            print('Executing the __init__ method.')
    
    ic = InitClass()

Output:Executing the __init__ method.
```
Here, the essential point to note is, you are not calling the ```__init__``` method. Instead, the Python interpreter makes the call upon object instantiation. Let’s consider an example, which takes an optional argument: 
```bash
    class Square(object):
        def __init__(self, number = 2):
            self._number = number
    
        def square(self):
            return self._number**2
    
    s = Square()
    print('Number: % i' % s._number)
    print('Square: % i' % s.square())

Output:

Number: 2
Square: 4
```
Here we can notice, the default value (2) is used by the ```__init__``` method in the absence of an optional argument. Let’s check some facts about the ```__init__``` method:

    The __init__ method provides initial data to the object, not to create an object.
    It only returns None; returning other than None raises TypeError.
    It customizes the instantiation of a class.

Next, we will proceed to the ```__new__``` method. 
```__new__``` method

The ```__new__``` method creates and returns the instance of a class. The primary argument of the ```__new__``` method is the class that has to be instantiated, and the rest are the arguments mentioned during the class call. Let’s explore through an example: Example: 
```bash
    class Students(object):
        def __init__(self, idNo, grade):
            self._idNo = idNo
            self._grade = grade
    
        def __new__(cls, idNo, grade):
            print("Creating Instance")
            instance = super(Students, cls).__new__(cls)
            if 5 <= grade <= 10:
                return instance
            else:
                return None
    
        def __str__(self):
            return '{0}({1})'.format(self.__class__.__name__, self.__dict__)
    
    
    stud1 = Students(1, 7)
    print(stud1)
    
    stud2 = Students(2, 12)
    print(stud2)

    Output

 
Creating Instance
Students({'_idNo': 1, '_grade': 7})
Creating Instance
None
```
In most cases, we do not need to define a __new__ method. If we go for a ```__new__``` method implementation, then referencing the superclass is a must. Another essential point to note, the ```__init__``` method of the instantiated class get executes, only if the ```__new__```  method returns an instance of the same class.
# Destruction
```__del__``` method

The```__del__``` method is invoked on destroying an instance of a class – either through direct deletion or memory restoration by the garbage collector. Let’s examine the below code: 
```bash
    class MyClass(object):
        def __del__(self):
            print('Destroyed')
    
    MyClass()
    'Immutable String - not assigned to a variable'

Output

Destroyed
```
What happens when we create an object without assigning them to a variable? The garbage collector will keep the record of objects, which is not referenced to a variable, and delete it when another program statement executes. Here, we created an object of MyClass without assigning it to a variable. Upon execution of the program statement (Immutable String – not assigned to a variable), the garbage collector destroys the MyClass object. The same happens, when we delete the object directly; But here the deletion happens immediately. Just try the below code. x = MyClass() del x
## Type Conversion

Type Conversion refers to the conversion of one data type to another; Python provides several magic methods to handle the conversion.
```

    __str__ method
    __int__, __float__ and __complex__ methods
    __bool__ method
```
## ```__str__``` method

The ```__str__``` method requires one positional argument – self – and it returns a string. It is called when an object is passed to the str() constructor. Let’s consider an example: 
```bash
    class MyString(object):
        def __str__(self):
            return 'My String !'
    
    print(str(MyString()))

Output

My String!
```
Let’s take a look at another situation that invokes the ```__str__``` method. The scenario is the usage of %s in a format string, which in turn invokes the ```__str__``` method. 
```bash
    class HelloClass(object):
        def __str__(self):
            return 'George'
    
    print('Hello, % s' % HelloClass())

Output

Hello, George
```
## ```__int__```,``` __float__``` and ```__complex__``` methods ##

The ```__int__``` method executes upon calling the int constructor, and it returns an int; It converts the complex objects into primitive int type. Likewise, ```__float__``` and ```_complex__```methods execute on passing the object to float and complex constructor, respectively.
```__bool__``` method

The ```__bool__``` magic method in python takes one positional argument and returns either true or false. Its purpose is either to check an object is true or false, or to explicitly convert to a Boolean.
Comparisons

Comparisons magic methods are invoked, when we check for equivalence ```(==, !=)``` or relations ```(<, and > =)```. Each of this operator in python is mapped to its corresponding magic methods. 
Binary Equality

1. ```__eq__``` method The ```__eq__``` method executes when two objects are compared using == operator. It takes two positional arguments – the self, and the object to check the equality. In most cases, if the object on the left side is defined, then its equivalence is checked first. Let’s see through an example: 
```bash
    class MyEquivalence(object):
        def __eq__(self, other):
            print('MyEquivalence:\n'
                '% r\n % r' %(self, other))
            return self is other
    
    class YourEquivalence(object):
        def __eq__(self, other):
            print('Your Equivalence:\n'
                '% r\n % r' %(self, other))
            return self is other
    
    eq1 = MyEquivalence()
    eq2 = YourEquivalence()
    # checking for equivalence where eq1 is at the left side
    print(eq1 == eq2)
    # checking for equivalence where eq2 is at the left side
    print(eq2 == eq1)
```
```
Output

MyEquivalence:
<__main__.MyEquivalence object at 0x7fa1d38e16d8>
<__main__.YourEquivalence object at 0x7fa1d1ea37b8>
False
Your Equivalence:
<__main__.YourEquivalence object at 0x7fa1d1ea37b8>
<__main__.MyEquivalence object at 0x7fa1d38e16d8>
False
```
The ordering rule isn’t applicable if one object is a direct subclass of the other. Let’s examine through an example: 
```bash
    class MyEquivalence(object):
        def __eq__(self, other):
            print('MyEquivalence:\n'
                '% r\n % r' %(self, other))
            return self is other
    
    class MySubEquivalence(MyEquivalence):
        def __eq__(self, other):
            print('MySubEquivalence:\n'
                '% r\n % r' %(self, other))
            return self is other
    
    eqMain = MyEquivalence()
    eqSub = MySubEquivalence()
    
    # eqMain at the right side
    print(eqMain == eqSub)
    
    # eqSub at the right side
    print(eqSub == eqMain)
```
```bash
output:
<__main__.MySubEquivalence object at 0x7f299ce802b0>
 <__main__.MyEquivalence object at 0x7f299e8be6d8>
False
MySubEquivalence:
<__main__.MySubEquivalence object at 0x7f299ce802b0>
 <__main__.MyEquivalence object at 0x7f299e8be6d8>
False
```

***2. ```__ne__``` method The ```__ne__```magic method executes, when != operator is used. In most cases, we don’t need to define the ```__ne__``` method; Upon using the != operator, the python interpreter will execute the ```__eq__ ```method and reverse the result.***
Relative Comparisons – ```__lt__``` & ```__le__```, ```__gt__``` & ```__ge__``` methods

The ```__lt__``` and ```__le__``` methods are invoked when < and <= operators are used, respectively.And, the ```__gt__ ```and ```__ge__``` methods are invoked on using  > and >= operators, respectively. However,  it’s not necessary to use all these 4 methods; usage of ```__lt__ ```and ```__gt__``` methods will meet the purpose. Just examine the below points to understand why we don’t require all these methods: 1. The ```__ge__``` and ```__le__``` methods can be replaced with the inverse of ```__lt__``` and ```__gt__``` methods, respectively. 2.  The disjunction of ```__lt__``` and ```__eq__``` methods can be used instead of the ```__le__``` method, and similarly, the ```__gt__``` and``` __eq__``` methods for ```__ge__``` method. Let’s take a look at the below example. Here, we will compare the object based on its creation time. 
```bash
    import time
    class ObjectCreationTime(object):
        def __init__(self, objName):
            self._created = time.time()
            self._objName = objName
    
        def __lt__(self, other):
            print('Creation Time:\n'
                '% s:% f\n % s:% f' %(self._objName, self._created,
                                    other._objName, other._created))
            return self._created < other._created
    
        def __gt__(self, other):
            print('Creation Time:\n'
                '% s:% f\n % s:% f' %(self._objName, self._created,
                                    other._objName, other._created))
            return self._created > other._created
    
    obj1 = ObjectCreationTime('obj1')
    obj2 = ObjectCreationTime('obj2')
    print(obj1 < obj2)
    print(obj1 > obj2)
```
```bash
Output

Creation Time:
obj1:1590679265.753279
obj2:1590679265.753280
True
Creation Time:
obj1:1590679265.753279
obj2:1590679265.753280
False
```

