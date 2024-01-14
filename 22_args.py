# *args = parameter that will pack all arguments into a tuple
#         usefull so that a function can accept a varing amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum + sum

print(add(2,4,6)) # 24
        