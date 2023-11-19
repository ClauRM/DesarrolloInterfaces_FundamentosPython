##Programa Agenda por Claudia Rubio

agenda =[["Nombre","Telefono","Email"]]

def miAgenda():
    print("Introduce el nuevo nombre en la agenda")
    nombre = input()
    print("Introduce el numero de telefono")
    telefono = input()
    print("Introduce el email")
    email = input()
    #antes de hacer nada, lo metemos en la lista y mostramos
    agenda.append([nombre,telefono,email])
    print(agenda)
    #guardar en archivo
    archivo = open("agenda.txt",'a')#flag 'a' appened=añadir, respeta lo q hay y escribe a continuación
    contacto = nombre+','+telefono+','+email+'\n'
    archivo.write(str(contacto))
    archivo.close()
    #ejecucion repetida
    miAgenda()

miAgenda()
