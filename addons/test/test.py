# code for testing decorator chaining
# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner

# def decor(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner

# @decor
# @decor1
# def num():
# 	return 10

# print(num())

# def create_adder(func):
#     def adder(a,b):
#         print("berfore")
#         return func(a,b)
#     return adder

# @create_adder
# def add(a,b):
#     print(a+b)

# add(1,2)

# def relationship_checker(func):
#     def check(a):
#         if a == "Love":
#             print('I Love You So much')
#         else:
#             print('Fuck u')

#     return check

# @relationship_checker
# def hello(a):
#     return a

# a = input("Enter a:")
# hello(a)

# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result

# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

