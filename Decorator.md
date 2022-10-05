# Decorator
<b>Decorators</b> are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

<b>
First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
</b>

Properties of first class functions:
- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …
        
        def hello_decorator(func):
            def inner1(*args, **kwargs):
                
                print("before Execution")
                
                returned_value = func(*args, **kwargs)
                print("after Execution")
                
                return returned_value
                
            return inner1


        @hello_decorator
        def sum_two_numbers(a, b):
            print("Inside the function")
            return a + b

        a, b = 1, 2

        print("Sum =", sum_two_numbers(a, b))
