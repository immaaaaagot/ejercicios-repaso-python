
list= []
i=0
while i<5:
    try:
        numero=int(input("Dime un número: "))
        list.append(numero)
        i+=1
    except:
        print("No es un número")

valor_mayor=list[0]
for n in list:
    if valor_mayor>n:
        valor_mayor=valor_mayor
    else:
        valor_mayor=n
print("El numero mayor es: " + str(valor_mayor))