##Programa Agenda por Claudia Rubio

agenda =[["Nombre","Telefono","Email"]]

#Primero: cargar en la lista agenda los registros que hay en el archivo de texto
archivo = open("agenda.txt",'r')#flag 'r' read=leer
for i in range(1,10):
    nuevalinea = archivo.readline().split(",")
    agenda.append(nuevalinea)
#Segundo: imprimir agenda
print(agenda)


#Metodo para aniadir registros en la agenda
def miAgenda():
    #Menu inicial
    print("Escoge una opción")
    print("1.- Introduce nuevo registro")
    print("2.- Listar registros")
    print("3.- Buscar registro")
    opcion = input()
    #Opcion Nuevo registro
    if opcion == "1":
        print("Introduce el nuevo nombre en la agenda")
        nombre = input()
        print("Introduce el numero de telefono")
        telefono = input()
        print("Introduce el email")
        email = input()
        #Aniadir registros a la agenda
        agenda.append([nombre,telefono,email])
        #Guardar en archivo de texto para persistencia de datos
        archivo = open("agenda.txt",'a')
        contacto = nombre+','+telefono+','+email+'\n'
        archivo.write(str(contacto))
        archivo.close()
    #Opcion Listar registros
    if opcion == "2":
        for i in range(1,len(agenda)):
            print(agenda[i])
    #Opcion Buscar registros
    if opcion == "3":
        print("Introduce el nombre, email o numero de telefono que desea buscar")
        buscar = input()
        for i in range(1,len(agenda)):
            if buscar in agenda[i]:
                print(agenda[i])
                break
    #Ejecucion repetida
    miAgenda()

#Tercero: aniadir contactos en la agenda
miAgenda()
