#read Leer un archivo existente, no modificar ni crear
#write Escribir en un archivo, se puede leer, escribir y crear archivos
#append: Agregar informacion a un archivo
#try: Es una sentencia la cual "intenta" ejecutar una instrucciòn
#except Es una sentencia la cual "atrapara" el error en caso de que "try" falle y ejecutara una serie de instrucciones en respuesta
#else Es una sentencia que ejecutara las instrucciones en caso de que "try" no falle
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
donde preguntes nombre promedio y grupo. '''



import os

class Alumno:


    def __init__(self, Nombre, Promedio, Grupo):
        self.Nombre = Nombre
        self.Promedio = Promedio
        self.Grupo = Grupo

    def str(self):
            return "%s , %s , %s"%(self.Nombre,self.Promedio,self.Grupo)

    def Agregar():
            print ("Agrege un alumno de la siguiente manera:")
            print ("Enrique, 6.7, 2017C")
            x = input("Ingrese al Alumno: ")
            f = open("Estudiantes.txt", "a")
            f.write('\n' + (x))
            f.close
            z = int(input("Presiona 1 si quieres agregar a otro alumno  \nPresiona 2 si quieres volver al menú de inicio "))
            if(z == 1):
                Agregar()
            if(z == 2):
                main()


    def alf():
            Dicci = {}
            list = []
            list2 = []
            doc = "Estudiantes.txt"
            with open(doc,'r') as file:
                for line in file.readlines():
                    list = []
                    list.append(line)
                    list = ' '.join(list)
                    list = list.split(",")
                    Dicci [list[0]] = list [1]
                    list2.append(Alumno(list[0],list[1],list[2]))
                    print (str(list[0]))
                list2.sort(key=lambda Alumno:Alumno.Nombre)
                for i in list2:
                    Texto=open("Orden por alfabeto.txt",'a+')
                    Texto.write(str(i))
                    Texto.close
                print("Archivo creado alfabeticamente")
    

    def promedio():
        Alumnos={}
        list=[]
        listOB =[]
        Archivo = "Estudiantes.txt"
        with open(Archivo,'r') as file:
            print("Opened "+ Archivo)
            for line in file.readlines():
                list=[]
                list.append(line)
                list=' '.join(list)
                list=list.split(",")
                Alumnos[list[0]] = list[1]
                listOB.append(Alumno(list[0],list[1],list[2]))
            print(listOB(Alumno.Grupo[0]))
            listOB.sort(key=lambda Alumno:Alumno.Promedio,reverse=True)
            for i in listOB:
                Texto=open("Oren por promedio.txt",'a+')
                Texto.write(str(i))
                Texto.close
            print("Archivo por promedio creado")



def main():
    a = int(input("¡Hola! elige una de las opciones:\n 1 Para que los alumnos se ordenen alfabeticamente\n 2 Para que los alumnos se ordenen según el promedio\n 3 Para agregar un nuevo Alumno al archivo \nEscribe cualquier otro numero si quieres salir  \nElige una opcion: "))
    if a == 1: 
       Alumno.alf ()
    if a == 2: 
        Alumno.promedio ()
    if a == 3:
        Alumno.Agregar()
    



if __name__=="__main__":
	main()
