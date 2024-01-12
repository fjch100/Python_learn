temp = input("Ingrese la temperatura: ")
grad = input("Ingrese Farenheit(F) o Celsius(C): ")
if grad == "C":
    temperaturaF = (float(temp) * 9/5) +32
    print("Temperatura = ", str(temperaturaF) , "F")
elif grad == "F":
    temperaturaC = (float(temp) - 32) * 5/9
    print("Temperatura = ", str(temperaturaC) , "C")
else:
    print("la escala es incorrecta")
    