#Conteo de vocales:
cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador = sum(1 for letra in cadena if letra in vocales)
print("Número de vocales:", contador)