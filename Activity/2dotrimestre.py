#Activadad inicial segundo trimestre

#1. Función que dice hola con el nombre
"""
name = input ("Ingresa tu nombre: ")
print ("Hola", name, "que tal")
"""


#2. Función que dice si un número es mayor a 10
"""
number = float (input ("Ingresa un número: "))
if number < 10:
    print ("El número ingresado es menor que 10."),
else:
    print ("El número ingresaso es mayor que 10.")
"""


#3.Función que suma dos números
"""
number1 = float (input ("Ingresa el primer número: "))
number2 = float (input ("Ingresa el segundo número: "))
result = (number1 + number2)
print ("El resultado de la suma es: ", int (result))
"""


#4.Función que cuenta hasta un número
"""
number = float (input("Ingresa un número: "))
i = 1
while i <= number:
    print (i)
    i += 1
"""

#5. Función que dibuja una carita feliz

"""

number= float (input("Ingresa un número del 1 a 2: " ))

if number > 1:
    print ("Estás :D"),
else:
    print ("Estás :(") 
"""



#6. Función que multiplica y devuelve el resultado
#Objetivo: Usar return para guardar resultados
"""
def multiplicar(a, b):
    
    resultado = a * b
    
    return resultado

resultado_multiplicacion = multiplicar(5, 3)

print("El resultado de la multiplicación es:", resultado_multiplicacion)
"""


"""
for i in range (10, 0, -1):
    print (-i)
"""