import customtkinter as Ctk

app = Ctk.CTk()
app.title("Cualquier cosa")
 #Tamaño, utiliza geometry que es otra manera de acomodar las cosas.
app.geometry("600x450+100+200") 
pos_x = app.winfo_x() + 150
pos_y = app.winfo_y() + 80 #c&p, determina las posiciones
posicion_fija = f"+{pos_x}+{pos_y}" #Crea una posicion fija del widget.

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = Ctk.StringVar(value="on")
checkbox = Ctk.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack()
app.mainloop()