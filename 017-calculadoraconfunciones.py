'''
Programa Calculadora
(c) 2023 Claudia Rubio
v1.0
'''
#Bienvenida
print("BIENVENIDO A LA CALCULADORA")
print("Indica tu nombre")
nombre=input()
print("Hola",nombre,"bienvenido a la calculadora")

def calculadora():
    #Indica el tipo de operación
    print("Escoge la operación que vas a realizar"+
        "\n1. Suma"+
        "\n2. Resta"+
        "\n3. Multiplicación"+
        "\n4. División")
    opcion=int(input())
    print("La operacion elegida es",opcion)
    #Indica dos numeros
    print("Introduce un número")
    numero1=int(input())
    print("Introduce otro número")
    numero2=int(input())
    #Realiza la operación
    if opcion ==1:
        print("La suma es igual a",numero1+numero2)
    if opcion ==2:
        print("La resta es igual a",numero1-numero2)
    if opcion ==3:
        print("La multiplicación es igual a",numero1*numero2)
    if opcion ==4:
        print("La división es igual a",numero1/numero2)
    calculadora()

calculadora()
