#1 Declara dos variables con números y muestra su suma, resta, multiplicación y división.

'''
a = 10
b = 73

suma = (a + b)
multiplicacion = (a * b)
division = (a / b)

print ('La suma es: ', suma, 'La multiplicación es: ', multiplicacion, 'y la dicisión es: ', division)
'''

#2 Pide al usuario su nombre y edad

'''
name = input('Ingrese su nombre: ')
age = input('Ingrese su edad: ')

print ('Hola', name, 'tienes', age, 'años')
'''

#3 Pide al usuario dos números

'''
number1 = int(input('Ingresa el 1er número: '))
number2 = int(input('Ingrese el 2do número: '))

result = (number1 * number2)

if result > 100:
    print(result, 'Es mayor que 100')
else:
    print(result, 'Es menor que 100')
'''

#4
''''' 
dolares = float(input("Introduce la cantidad en dolares: "))
tasa_conversion = 0.85 # Ejemplo de sa de conversión
print("Cantidad en Euros:", dolares * tasa_conversion)
'''
#5
''''
num = int(input("Digite un numero: "))
if num % 2 == 0:
    print("número es par.")
else:
    print("es impar.")
'''
#6
'''
import math
radio = float(input("Introduce el radio del circulo: "))
area = math.pi * radio ** 2
print("Área del circulo:", area)
'''
#7
'''
age = int(input("Digite el año de nacimiento: "))
currentage = int(2025 - age)
print("Tu edad actual es: ", currentage)
'''
#8
'''
import math

num = int(input("Ingresa un número: "))
doble = int(num * 2)
triple = int(num * 3)
raiz = math.sqrt(num)

print ("El doble es:", doble, "El triple es:", triple, "y la raiz cuadrada es: ", raiz)
'''
#9
'''
name = input("Ingresa tu nombre completo: ")
name_mayus = name.upper()

print ("Nombre en mayúsculas:", name_mayus)
'''
#10
'''
fruits = ["Manzana", "Limon", "Lulo", "Mango", "Guanabana"]

print ("La segunda fruta es:", fruits[1])
'''
#11
'''
fruits = ["Manzana", "Limon", "Lulo", "Mango", "Guanabana"]
new_fruits = input("Ingresa una nueva fruta: ")
fruits.append(new_fruits)
print("Lista de frutas actualizadas:", fruits)
'''
#12
'''
number_list = [1, 2, 3, 4, 5]
#[-1] accede al último elemento (los índices negativos cuentan desde el final).
print ("El primero es:", number_list[0], "y el ultimo es:", number_list[-1])
'''
#13
'''
word = input("Escribe una palabra: ")
letters = len(word)
print("Tiene", letters, "letras" )
'''
#14
'''
number1 = float(input("Ingresa un número: "))
number2 = float(input("Ingresa el segundo un número: "))

if number1 > number2:
    print("El primer número es mayor")
elif number1 < number2:
    print("El segundo número es mayor")
else:
    print("Los dos son iguales")
    '''
#15

num = int(input("Ingresa un número: "))

for i in range(num +1):
    print (i)