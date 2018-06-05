fibo = int(input("Ingrese un numero que sea mayor a 5 y menor a 15: "))

if (fibo > 15):
	print ("Te has pasado el rango, el numero se cambiara a 15")
	fibo = 15

if (fibo < 5):
	print ("Te has pasado el rango, el numero se cambiara a 5")
	fibo = 5
print ()

x = 1
y = 0

for i in range (fibo):
	x = x + y
	y = x - y
	print (x)