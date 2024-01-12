lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]

i=1
while i <= 5:
    print(i)
    i=i+1

i=1
while i <= 5:
    print("el Weta " * i)
    i=i+1

i=0
while i < len(lenguajes):
    print(lenguajes[i])
    i=i+1

name = None
while not name:
    name=input("ingresa tu nombre: ")
print("Hola " + name)