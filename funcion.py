#funcion de saludo.
def saludar():
	print ("Hola, bienvenido a mi primer programa de funciones!")

#Funcion de multiplicacion.
def multi():
	print("Escribe un numero: ")
	numX = int(input())
	print("Escribe un segundo numero: ")
	numY = int(input())
	result = numX * numY
	print ("El resultado de la multiplicacion es: "+str(result))

def division():
	print("Escribe un numero: ")
	numX = int(input())
	print("Escribe un segundo numero: ")
	numY = int(input())
	result = numX / numY
	print ("El resultado de la division es: "+str(result))

def pot():
	print("Escribe un numero: ")
	numX = int(input())
	result = numX * numX
	print ("El cuadrado de tu numero es: "+str(result))

#Funcion principal de mi programa.
def main():
	saludar ()
	print()

	print ("Escribe 1 si quieres multiplicar.")
	print ("Escribe 2 si quieres dividir.")
	print ("Escribe 3 si quieres saber el cuadrado del numero.")
	num1 = int(input())
	if (num1 == 1):
		multi ()
	if (num1 == 2):
		division ()
	if (num1 == 3):
		pot()
if __name__ == "__main__":
	main()