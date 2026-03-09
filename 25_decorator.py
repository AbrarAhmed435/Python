def logger(func):
    def wrapper():# works only with fucntion with no arguments
        print("called")
        func()
    return wrapper


@logger
def hello():
    print("Hello")

hello()



import time
def timer(func):
    def wrapper(*args,**kwargs): #works with any function
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("Execution time:",end-start)
        return result
    return wrapper

@timer
def add(a,b):
    return (a+b)

print(add(5,6))