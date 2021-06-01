# define a function

def sayHello():
    print('Hello There')
    print("Welcome on Board")


sayHello()

# function with an argument


def greet_user(name, message):
    print(f"{message} {name}")


greet_user("Baraka", "Good evening")

# key-worded arguments

# return keyword


def square(n):
    return n*n


square_of_3 = square(3)
print(square_of_3)
