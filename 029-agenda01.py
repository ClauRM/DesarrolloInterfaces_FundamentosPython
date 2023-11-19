##Programa Agenda por Claudia Rubio

##from tkinter import *
##
##f = Frame(width=300,height=300) #tamanio de la ventana
##f.pack(padx=30,pady=30)#padding en horizontal y vertical
##
##titulo = Label(f,text = "Hola Mundo")
##titulo.pack(side=TOP)

agenda =[["Nombre","Telefono","Email"]]
agenda.append(["Nombre2","Telefono2","Email2"])

print(agenda)

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
    #ejecucion repetida
    miAgenda()

miAgenda()
