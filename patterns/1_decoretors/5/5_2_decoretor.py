def my_decorator(func):

    def wrapper():
        print("Antes")
        func()
        print("Depois")

    return wrapper

@my_decorator
def say_hi():
    print("Oi")