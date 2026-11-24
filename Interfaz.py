#Importar la libreria
import customtkinter as Ctk

#--------------------Primer paso: Crear la aplicacion -------------
app = Ctk.CTk()
app.title("Primera Interfaz")
 #Tamaño, utiliza geometry que es otra manera de acomodar las cosas.
app.geometry("600x450+100+200") 
#Ubicacion ya dada por el profesor.
#c&p, determina las posiciones
pos_x = app.winfo_x() + 150
pos_y = app.winfo_y() + 80 
 #Crea una posicion fija del widget.
posicion_fija = f"+{pos_x}+{pos_y}"

#-------------------------------------------------------------------


def IngresoDeDatos():

    suma_general=0 #El sumador/acumulador que va a guardar la suma total de los promedios de los 20 alumnos

    cant_aprobados=0 #Contador que cuenta los alumnos que tienen promedio mayor a 7

    cant_desaprobados=0 #Contador que cuenta los alumnos que tienen promedio menor a 7


    for i in range(2):
        #Aca el usuario va a ingresar los datos de a un alumno, 20 veces- Es decir, ingrea las 5 notas del primer alumno, se calcula su promedio, se muestra, y pasa al siguiente alumno.

        suma_alumno=0 #Es el acumulador/sumador que guarda la suma de las 5 notas del alumno, para despues calcular su promedio.

        contadorCONDICION=0 #Es el contador que va a ir desde 0 a 5, para saber cuando cortar la iteracion durante el while. Cuando el contador llega a 5, frena el while-

        while contadorCONDICION <5: #Se pone solo <, porque la cantidad de notas es 5, si ponemos <= desde 0 a 5 habria 6 notas.

            #El usuario debe ingresar las notas
            ingresoNota = Ctk.CTkInputDialog(text=f"Ingrese la nota {contadorCONDICION+1}", title="Ingreso de notas")

            #Se trae el dato que ingreso el usuario y lo guarda en una variable llamada notaIngresada
            notaIngresada=ingresoNota.get_input()
            contadorCONDICION+=1

            #SINTAXIS QUE HAY QUE ENTENDER
            try:
               #Aca trata de convertir la nota Ingresada en un tipo de dato float.
               notaIngresadaenFLOAT=float(notaIngresada)
               if notaIngresadaenFLOAT > 0 and notaIngresadaenFLOAT <= 10: #Aca valida que cada nota ingrsada sea correcta
                suma_alumno+=notaIngresadaenFLOAT
               else: continue #Le pone el continue para que si el rango de nota no es valido, el programa siga corriendo. 

            except ValueError:
               continue

        promedio = suma_alumno/5 #promedio por alumno
        suma_general+= promedio
        if promedio >= 7:
           cant_aprobados = cant_aprobados+1
        else:
           cant_desaprobados = cant_desaprobados+1   
        etiqueta=Ctk.CTkLabel(app,text=f"promedio del alumno {i}:  {promedio}")
        etiqueta.pack()            

    etiqueta1=Ctk.CTkLabel(app,text=f"Cantidad de aprobados{cant_aprobados}")
    etiqueta1.pack()
    etiqueta2=Ctk.CTkLabel(app,text=f"Cantidad de desaprobados{cant_desaprobados}")
    etiqueta2.pack()
    #Boton para el INGRESO DE ALUMNOS
    def MostraPromedioGeneral():
       promedio_general = suma_general/20
       etiqueta3=Ctk.CTkLabel(app, text=f"promedio general{promedio_general}")
       etiqueta3.pack()
    boton1=Ctk.CTkButton(app, text="Mostrar Promedio General", command=MostraPromedioGeneral)
    boton1.pack()

    #INVESTIGAR PORQUE NO SE VE EN LA INTERFAZ
    def MostrarPorcentajeAprobados():
      PorcentajeAprobados=(cant_aprobados*100)/20
      etiquetaPorcentaje=Ctk.CTkLabel(app, text=f"Porcentaje aprobados {PorcentajeAprobados}")
      etiquetaPorcentaje.pack()

    botonPorcentaje=Ctk.CTkButton(app, text="Mostrar Porcentaje Aprobados", command=MostrarPorcentajeAprobados)
    botonPorcentaje.pack()

boton=Ctk.CTkButton(app,text="Ingresar alumnos", command=IngresoDeDatos)
boton.pack()

















#Importante para que la ventana abra y no se cierre instantaneamente.
app.mainloop()