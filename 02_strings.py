texto = "Hola Mundo"

print(texto.upper())
print(texto.lower())
print(texto.find("M"))
print(texto.find("m"))# retorna -1
print(texto.replace("Mun", "chanchito feliz"))# replace retorna un nuevo texto 
nuevoTexto = texto.replace("Mundo", "Tierra")
print(texto, nuevoTexto)
print("Mundo" in texto)



