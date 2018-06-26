

def asteri():
	x = input("Ingresa numeros y separalos con una (,) para interpretarlos con asteriscos: ")
	y = x.split(",")
	z = list(map(int, y))

	for i in range (0,len(z)):
		print(("*") * z[i])


def esfera():
	r = float(input("Ingrese el radio de la esfera: "))
	v = (4 * 3.1416 * (r**3)) /3
	print (v)

def tria():
	b = int(input("Ingrese la base del triangulo: "))
	a = int(input("Ingrese la altura del triangulo: "))

	area = b * a / 2
	print (area)

def versión():
	import sys
	print(sys.version)




def main ():
	x = int(input("Si quiere que se interprete mediante asteriscos presione 1. \nSi quiere saber cuantos días hay de una fecha a otra presione 2. \nSi quiere saber la extencion de un archivo presione 3. \nSi quiere saber el area de un triangulo presione 4. \nPara saber el angulo de una esfera presione 5. \nPara imprimir la versión de Python presione 6.\n")) 

	if (x==1):
		asteri()

	if (x == 2):
		días()

	if (x == 3):
		ext()
	
	if (x == 4):
		tria()

	if (x == 5):
		esfera()

	if (x == 6):
		versión ()




if __name__ == "__main__":
	main()
