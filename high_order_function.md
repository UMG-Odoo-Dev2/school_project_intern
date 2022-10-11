# High Order Function In Python
## Introduction

A function is called Higher Order Function if it contains other functions as parameters or returns functions. It is an important concept of functional programming. Python, as a very flexible programming language, supports the usages of higher order functions. There are some build-in higher order functions in Python and we can also define higher order functions by ourselves.

This post will introduce it by Python’s build-in functions and explain how it works by simple examples.

## Map, Reduce and Filter Functions

These three functions are common used build-in higher order functions in Python. Many other programming languages also have build-in functions like them. Applying these three functions well can help us avoid too much for loops in our code and makes it more elegant and readable.

They all receive two parameters which makes them a little similar. However, they have different consequences and usage scenarios. Let’s have a look at them.

## The Map Function

The ```map()``` function receives two parameters, one is a function and the other is Iterable. It applies the initialized function to each element of the sequence in turn, and returns the result as a new Iterator.

For example, if we need to calculate the square of each number in a list, we can use ```map()``` :
```bash
    def f(x):
        return x * x
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

Output:[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Actually, we can get it by just one line with the lambda function:
```bash
    r = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```
Obviously, using ```map()``` function can make our code more elegant and clear than using a for loop.

Another example: Use the ```map()``` function to change the non-standard English name to the canonical names:

```bash
    names = ['yAnG', 'MASk', 'thoMas', 'LISA']
    names = map(str.capitalize, names)
    print(list(names))
Output:['Yang', 'Mask', 'Thomas', 'Lisa']
```
## The Reduce Function

The ```reduce()``` method also has two parameters, one is a function and the other is Iterable. It applies a function to a sequence, this function must receive two parameters, reduce continues the result and performs the cumulative calculation with the next element of the sequence. Finally, it returns the result of the cumulative calculation.

The consequence of a ```reduce()``` function is the same as using the function again and again for an Iterable.
```bash
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

For example, if we want to convert a list ```['L','o','n','d','o','n',2,0,2,0]``` to a string ```"London2020”``` , using reduce is a good idea.
```bash
    from functools import reduce

    city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
    city_to_str = reduce(lambda x, y: str(x) + str(y), city)
    print(city_to_str)
# London2020
```
## The Filter Function

Similar to ```map()```, the ```filter()``` function also receives a function and a sequence. Unlike ```map()```, ```filter()``` applies the incoming function to each element in turn, and then decides whether to keep or discard the element based on whether the return value is True or False.

For example, let’s delete the names longer than four letters in previous example:
```bash
    names = ['yAnG', 'MASk', 'thoMas', 'LISA']
    names = map(str.capitalize, names)
    names = filter(lambda x: len(x) <= 4, names)
    print(list(names))
# ['Yang', 'Mask', 'Lisa']
```
The same as ```map()``` function, the ```filter()``` function returns an Iterator, which is a “lazy sequence”, so to force it to complete the calculation results, we need to use the list function to get all the results and return the list.

## The Sort Function in Python
Sorting is also an algorithm often used in programs. Whether using bubble sorting or quick sorting, the core of sorting is to compare elements. If it is a number, we can directly compare, but if it is a string or “dict”? Therefore, the process of comparison must be abstracted through functions.

Python’s build-in ```sorted``` method, which is a higher order function, has a ```key``` parameter receiving a function which defines how to compare the elements.

For example, let’s sort a list including names by their length:
```bash
    names = ['Yang', 'Robert', 'Tom', 'Gates']
    names = sorted(names, key=len)
    print(names)
# ['Tom', 'Yang', 'Gates', 'Robert']
```
Note: There are two ways for using sort function, we should understand the differences and use them properly:

#1. Using the ```sorted``` directly and it will return a new sorted list.
```bash 
    names = sorted(names, key=len)
```
#2. Call sort() function by the sequence. This will sort it in place and nothing will be returned.
```bash
    names.sort(key=len)
```
## Return a Function

The above functions receive other functions as their parameter. As we said at the beginning, a function returning another function is also called higher order function. Another formal name of it is Closure. Let’s look at an example:
```bash
    def lazy_sum(numbers: list):
        def sum():
            s = 0
            for n in numbers:
                s += n
            return s

        return sum

    func = lazy_sum([1, 2, 3, 4, 5])
    print(func)
# <function lazy_sum.<locals>.sum at 0x7ff9da4179d8>
```
As the above example shown, instead of returning the summed result, we can return the sum function. It is a lazy evaluation method which gives us more flexity. We can calculate the result whenever we need it:
```bash
    print(func()) # 15
```
Note: The ```func``` is only a reference (name) of a function, we need to call ```func()``` to make the function run. In this example, ```func``` saves the ```sum``` function which was returned by ```lazy_sum``` function. When we call ```func()``` , it calculate and return the final summation result.

After understanding the closure, it’s easy to understand decorators in Python.
## Conclusion

The higher order functions in Python give us more flexibility and make our code more readable and elegant.
