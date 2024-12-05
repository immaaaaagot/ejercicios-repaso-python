edad1=int(input("Dime la edad de la primera persona:"))
edad2= int(input("Dime la edad de la primera persona: "))
if edad2<0 or edad1<0:
    print("Una de las edades es negativa")
if edad2==edad1:
    print("Las edades de ambas personas son iguales")
elif edad2<edad1:
    print("La segunda edad es menor que la primera")
elif edad1<edad2:
    print("La primera edad es menor que la segunda")