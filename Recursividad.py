def fac (f):
    if (f==1):
        return 1
    return f * fac(f-1)
    
def fibo (b):
	if (b == 0):
		return 1
	elif (b == 1):
		return 1
	else:
		return (fibo(b-1) + fibo(b-2))

def tres (t):
    if (t == 1):
        return 1
    a = 1
    while (a < 3):
        a = a + 1
    return t * a 

def pascal(): 
    if n == 0: 
        return [] 
    if n == 1: 
        return [[1]] 
    lista = pascal(n-1)
    list = [1] 
    for i in range(1, n-1): 
        list.append(lista[n-2][i-1] + lista[n-2][i]) 
    list.append(1)
    lista.append(list) 
    return lista 

def main ():
    a = int(input("Ingrese 1 si quiere saber el factorial de un numero. \nIngrese 2 si quiere hacer la secuencia de Fibonacci. \nIngrese 3 si quiere multiplicar un numero por 3. \n"))
    if (a == 1):
     f = int(input("Ingrese el numero del cual quiere saber su factorial: ")) 
     fac (f)
     print (fac(f))			
    if (a == 2):
     b = int(input("Ingresa las vueltas que quieres dar en la serie de Fibonacci: "))
     fibo (b)
     print (fibo(b))
    if (a == 3):
     t = int(input("Ingrese un numero entero para multiplicarlo por 3: "))
     tres (t)
     print (tres(t))
    if (a == 4):
     pascal()
if __name__ == "__main__":
 main ()
