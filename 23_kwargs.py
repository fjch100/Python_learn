# **kwargs = parameter that will pack all arguments into a  dictionary
#            useful so that a function can accept a varing amount of keyword arguments

def hello(**kwargs):
    print("Hello", end= " ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr", first="Bro", middle="Dude", last="Code") # Hello Mr Bro Dude Code 
