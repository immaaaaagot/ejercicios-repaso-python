letra=input("Dime una letra:")
if letra>= "A" and letra <= "Z":
    print("La letra" + str(letra) + " es mayúscula")
elif letra>= "a" and letra <= "z":
    print("La letra" + str(letra) + " es minúscula")
else:
    print("No es una letra")

