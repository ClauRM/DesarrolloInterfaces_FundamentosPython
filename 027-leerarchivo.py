archivo = open("miarchivo.txt",'r')#flag 'r' read=leer

print(archivo.readline())#lee la linea y deja el cursor al final de la linea
print("========")

print(archivo.read())
print("========")

for i in range(0,10):
    print(archivo.readline())
    if archivo.readline() == 0:
        break

archivo.close()
