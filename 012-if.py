print("Dime tu nombre")
nombre=input()#el usuario proporciona una entrada

#para ver si el sistema guarda la informacion
print()

print("Dime tu edad")
edad=input()

print("Hola,",nombre,". Tu edad es de",edad,"años")

#como da un error de tipo de variable, reemplazo para mostrar el ejercicio del if
edad=15

if edad<30:
    print("Eres joven")
else:
    print("Ya no eres tan joven")
    print("Esto está dentro del else")

print("Esto está fuera del if-else, con lo cual, la sangría es importante")

