num1 = int
num2 = int
operador = str
resultat = int

def suma(num1, num2): 
    return num1 + num2

# Funció per a la resta
# Definim la funció resta que rep dos números i retorna la seva resta
# num1: primer número
# num2: segon número

def resta(num1, num2):
    return num1 - num2

def multiplicacio(num1, num2):
    return num1 * num2

def divisio(num1, num2):
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def calculadora(num1, num2, operador):
    if operador == "+":
        return suma(num1, num2)
    elif operador == "-":
        return resta(num1, num2)
    elif operador == "*":
        return multiplicacio(num1, num2)
    elif operador == "/":
        return divisio(num1, num2)
    elif operador == "^":
        return potencia(num1, num2)
    else:
        return "Operador no vàlid"

print("Benvingut a la calculadora!")   
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
operador = input("Introdueix l'operador (+, -, *, /, ^): ")

resultat = calculadora(num1, num2, operador)
print("El resultat és:", resultat) 

