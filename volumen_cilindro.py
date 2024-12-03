from math import*
radio= int(input("Dime el radio:"))
altura=int(input("Dime la altura:"))
volumen=round((pi*radio**2*altura), 2) 
print("El volumen del cilindro:" + str(volumen))