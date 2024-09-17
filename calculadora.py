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

# Funció per a la resta
# num1: primer número
# num2: segon número
# return: retorna la resta de num1 i num2

def resta(num1, num2):
    return num1 - num2
# Funcion multiplicacio
#  num1: int represnta el numero 1
#  num2: int represnta el numero 2
#  return: int retorna la multiplicacio de num
def multiplicacio(num1, num2):
    return num1 * num2

# Funció per a la divisió
# num1: primer número
# num2: segon número
# return: retorna la divisió de num1 entre num2


def divisio(num1, num2):
    return num1 / num2
<<<<<<< Updated upstream

# Funció per a la potència
# num1: base
# num2: exponent
# return: retorna la potència de num1 elevat a num2

def potencia(num1, num2):
    return num1 ** num2

=======
# Funcion calculadora
#  num1: int represnta el numero 1
#  num2: int represnta el numero 2
#  operador: str represnta l'operador(+, -, *, /)
>>>>>>> Stashed changes
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

1