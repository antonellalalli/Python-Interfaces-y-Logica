import customtkinter as Ctk

app = Ctk.CTk()
app.title("Cualquier cosa")
 #Tamaño, utiliza geometry que es otra manera de acomodar las cosas.
app.geometry("600x450+100+200") 
pos_x = app.winfo_x() + 150
pos_y = app.winfo_y() + 80 #c&p, determina las posiciones
posicion_fija = f"+{pos_x}+{pos_y}" #Crea una posicion fija del widget.
frame=Ctk.CTkFrame(app, border_width=2, border_color="#1f538d")
frame.pack(padx=10, pady=10, fill="both", expand=True)

#Crear una funcion, que despues de leer el nombre y apellido de un usuario, le muestre un mensaje cordial de bienvenida.
entryNombre=Ctk.CTkEntry(frame, placeholder_text="Nombre") #Crea un campo de entrada de datos, del nombre del usuario
entryNombre.grid(row=2, column=2) #asigna la posicion fija al campo de entrada del nombre, para que quede centrado
entryApellido=Ctk.CTkEntry(frame, placeholder_text="Apellido")#Crea un campo de entrada del apellido del usuario
entryApellido.grid(row=3, column=2)
def Bienvenidar():
    nombre=entryNombre.get()
    apellido=entryApellido.get()
    etiqueta.configure(frame, text=f"Bienvenido a nuestra app {nombre} {apellido}")
    app.update()


etiqueta=Ctk.CTkLabel(frame, text="bienvenido", font=("Arial", 20, "bold")) #Crea una etiqueta que dice bienvenido
etiqueta.grid(row=1, column=2) #ubicacion de la etiqueta 


botonBienvenida=Ctk.CTkButton(frame, text="Bienvenidar", command=Bienvenidar)

botonBienvenida.grid(row=6, column=2)




app.mainloop() #mantiene la ventana activa.