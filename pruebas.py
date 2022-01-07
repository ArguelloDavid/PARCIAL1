numero = int(input("Ingrese un numero:"))
antecesor=numero-1
residuo=0
contadorDivisibles=0
while antecesor>1:
    residuo=numero%antecesor
    if residuo==0:
        contadorDivisibles=contadorDivisibles+1
    antecesor=antecesor-1
if contadorDivisibles==0:
    print("El número ingresado es primo")

else:
    print("El número no es primo")