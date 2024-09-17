num1 = int
num2 = int
operador = str
resultat = int

# Funcion Suma
#  num1: int represnta el numero 1
#  num2: int represnta el numero 2
#  return: int retorna la suma de num
def suma(num1, num2): 
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacio(num1, num2):
    return num1 * num2

def divisio(num1, num2):
    return num1 / num2

def calculadora(num1, num2, operador):
    if operador == "+":
        return suma(num1, num2)
    elif operador == "-":
        return resta(num1, num2)
    elif operador == "*":
        return multiplicacio(num1, num2)
    elif operador == "/":
        return divisio(num1, num2)
    else:
        return "Operador no vàlid"

print("Benvingut a la calculadora!")   
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
operador = input("Introdueix l'operador (+, -, *, /): ")

resultat = calculadora(num1, num2, operador)
print("El resultat és:", resultat) 

1