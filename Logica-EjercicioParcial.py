



contmayor14=0
contmasde9=0
acumayor14=0
acummas9=0
edades=list()
for i in range (0, 3):
    edad=int(input("ingresar edad:"))
    estatura=float(input("ingresar esatura:"))
    if edad>14:
        contmayor14+=1
        acumayor14+=estatura
    if estatura>170:
        edades.append(edad)
    prom=int(input("ingresar promedio:"))
    if prom>9:
        contmasde9+=1
        acummas9+=prom

porcentaje=(acummas9*contmasde9)/100

print(f"la cantidad de alumnos mayores a 14 es {contmayor14}")
print(f"porcentaje: {porcentaje}")
for edad in edades:
    print(f"[{edad}]")
