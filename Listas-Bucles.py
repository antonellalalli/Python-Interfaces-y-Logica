#-Se leen de a uno por vez 25 valores. Calcular y exhibir el cuadrado de cada uno de ellos

#for i in range (0, 2):
    #valor=float(input("Ingresar valor: "))
   # cuadrado=valor**2
   # print(f"el cuadrado de{valor} es {cuadrado}")



#7-Ingresada una lista de 107 números, determinar e informar el valor máximo y mínimo junto con el orden en el que
# fueron ingresados.

#minimo=int()

#maximo=int()
#for i in range (0, 3):
   # valor=float(input("ingresar valor: "))
   # if i == 0:
    #    maximo=valor
    #    minimo=valor
   # else:
    #    if valor>=maximo:
     #       maximo=valor
      #  elif valor<=minimo:
     #       minimo=valor
#print(f"el valor maximo es{maximo},el valor minimo es {minimo}")




#cont=0
#dorsal=int(input("Ingresar dorsal: "))

#while (dorsal!=0) : 
   # cont+=1 
   # dorsal=int(input("Ingresar otra dorsal: "))

#print(cont)



#Se tiene una nomina de alumnos identificados por su legajo. 
# Se desconoce la cantidad de alumnos, la carga finaliza cuando el legajo que ingresa el usuario es 0. 
# Cada alumno tiene una cantidad de materias al año, para cada una de las materias, consultar si esta aprobada, si es asi, 
# informar cuantas aprobadas tiene, y cuantas desaprobadas. 
#Informar cantidad de alumnos

alumnos=list()
alumnos.append(["Juan", 22, 1.34])
alumnos.append(["Anto", 20, 1.67])
for alumno in alumnos:
    print(alumno)
