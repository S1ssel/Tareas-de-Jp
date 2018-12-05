import os
'''Hacer una clase alumno
-nombre
-promedio
-grupo

funcion recursiva de ordenamiento 
A) Promedio ordenado
B) Alfabetico alfabetico


Funcion de almacenamiento de alumnos en archivos 1 archivo por grupo

desde la terminal preguntar por el tipo de ordenamiento

poder agregar un almuno nuevo
donde preguntes nombre promedio y gurpo. '''

class alumno:
    def __init__(self,nombre,promedio,grupo):
        self.nombre = nombre
        self.promedio = promedio
        self.grupo = grupo

def ordenProm(alumnos,x):
    if x == 0:
        return alumnos
    promedio = ordenProm(alumnos,x-1)
    #Este for cambia de lugar el promedio mas bajo por el mas alto.
    for i in range(1,(len(promedio)+1-x)):
        if promedio[i-1].promedio < promedio[i].promedio:
            t = promedio[i]
            promedio[i] = promedio[i-1]
            promedio[i-1] = t
    return promedio

def ordenABC(alumnos,x):
    if x == 0:
        return alumnos
    alfabetico = ordenABC(alumnos,x-1)
    #Este for cambia de lugar el nombre mas bajo por el mas alto.
    for i in range(1,(len(alfabetico)+1-x)):
        if alfabetico[i-1].nombre > alfabetico[i].nombre:
            t = alfabetico[i]
            alfabetico[i] = alfabetico[i-1]
            alfabetico[i-1] = t
    return alfabetico
    
def grupos(x):
    #2016A
    a = []
    #2016B
    b = []
    #2017A
    c = []
    #2017B
    d = []
    #2018A
    e = []
    #2018B
    f = []
    for i in range(len(x)):
        if x[i].grupo == '2016A\n' :
            a.append(x[i])
        if x[i].grupo == '2016B\n' :
            b.append(x[i])
        if x[i].grupo == '2017A\n' :
            c.append(x[i])
        if x[i].grupo == '2017B\n' :
            d.append(x[i])
        if x[i].grupo == '2018A\n' :
            e.append(x[i])
        if x[i].grupo == '2018B\n' :
            f.append(x[i])
        
    File1 = open('2016A.txt','w')
    for i in range(len(a)):
        File1.write(str(a[i].nombre)+', '+str(a[i].promedio)+', '+str(a[i].grupo))
    File1.close
    File1 = open('2016B.txt','w')
    for i in range(len(b)):
        File1.write(str(b[i].nombre)+', '+str(b[i].promedio)+', '+str(b[i].grupo))
    File1.close
    File1 = open('2017A.txt','w')
    for i in range(len(c)):
        File1.write(str(c[i].nombre)+', '+str(c[i].promedio)+', '+str(c[i].grupo))
    File1.close
    File1 = open('2017B.txt','w')
    for i in range(len(d)):
        File1.write(str(d[i].nombre)+', '+str(d[i].promedio)+', '+str(d[i].grupo))
    File1.close
    File1 = open('2018A.txt','w')
    for i in range(len(e)):
        File1.write(str(e[i].nombre)+', '+str(e[i].promedio)+', '+str(e[i].grupo))
    File1.close
    File1 = open('2018B.txt','w')
    for i in range(len(f)):
        File1.write(str(f[i].nombre)+', '+str(f[i].promedio)+', '+str(f[i].grupo))
    File1.close
    print('Sus archivos fueron guardados.\n\n\n')   
    return

def addAlumno(Alumnos):
    c = True
    while c:
        x = str(input('¿cual es el nombre del alumno?: '))
        y = str(input('¿cual es su grupo?: '))
        z = str(input('¿cual es su Promedio?: '))
        estudiantes = open('Estudiantes.txt','a')
        estudiantes.write(str(x) +', '+ str(z)+', '+str(y)+str('\n')) 
        a = alumno(x,z,y)
        Alumnos.append(a)
        estudiantes.close
        print('Alumno agregado')
        d = input(str('Desde agregar otro alumno? y/n : '))
        if d == 'n':
            c = False
    
    return Alumnos

def main():
    Alumnos = []
    c = True
    #Este with hace una lista  de el archivo estudiantes, donde cada objeto es una linea.
    with open('Estudiantes.txt','r') as Estudiantes:
        lines = Estudiantes.readlines()
    #Este for transforma cada linea del archivo en un objeto clase alumno.
    for i in range(len(lines)):
            lista = lines[i].split(', ')
            x = alumno(lista[0],float(lista[1]),lista[2])
            Alumnos.append(x)
    while c:
        opcion = input(str('Si quieres agregar un nuveo alumno, pulsa 1.\nSi quieres crear un archivo de los alumnos ordenado por promedio, pulsa 2.\nSi quieres crear un archivo de de los alumnos ordenado alfabeticamente, pulsa 3.\nSi quieres crear un archivo por cada grupo, pulsa 4.\nSi desea salir de el programa, pulse 5\n'))
        if opcion == '1':
            addAlumno(Alumnos)
        if opcion == '2':
            f = ordenProm(Alumnos,len(Alumnos))
            File1 = open('Promedio.txt','w')
            for i in range(len(f)):
                File1.write(str(f[i].nombre)+', '+str(f[i].promedio)+', '+str(f[i].grupo))
            File1.close
        if opcion == '3':
            f = ordenABC(Alumnos,len(Alumnos))
            File1 = open('Alfabetico.txt','w')
            for i in range(len(f)):
                File1.write(str(f[i].nombre)+', '+str(f[i].promedio)+', '+str(f[i].grupo))
            File1.close
        if opcion == '4':

            Archivo = input(str('Si desea crear los archivos por orden alfabetico precione 1.\nSi desea crear los archivos por promedio, pulse 2.\n'))
            if Archivo == '1':
                f = ordenABC(Alumnos,len(Alumnos))
                grupos(f)
            if Archivo == '2':
                f = ordenProm(Alumnos,len(Alumnos))
                grupos(f)
                
        if opcion == '5':
            c = False
    print('Adios')

if __name__ == "__main__":
    main()
