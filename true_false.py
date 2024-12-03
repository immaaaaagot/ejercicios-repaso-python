from math import*
nombre= input("Dime tu nombre:")
nombreCompleto= input("Dime tu nombre completo:")
respuesta1= sqrt(20)>5
respuesta2= 4<sqrt(20)<5
respuesta3= (2*pi*5)>30
respuesta4= (2*pi*0)==0
respuesta5= 5<len(nombre) <10
respuesta6= 25<(len(nombreCompleto)-2)<35
print("¿Es la raíz cuadrada de 20 mayor que 5?" + str(respuesta1)
print("¿Es la raíz cuadrada de 20 menor que 5 pero mayor que 4?" + str(respuesta2))   
print("¿Es la longitud de la circunferencia de una esfera de radio 5 mayor que 30?" + str(respuesta3))     
print("¿Es la longitud de la circunferencia de una esfera de radio 0 igual a 0?" + str(respuesta4))  
print("¿Tiene mi nombre más de 5 caracteres y menos de 10?" + str(respuesta5))   
print("¿Tiene mi nombre completo más de 25 caracteres y menos de 35?" + str(respuesta6))   