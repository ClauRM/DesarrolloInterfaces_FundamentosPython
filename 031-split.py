archivo = open("agenda.txt",'r')#flag 'r' read=leer

linea = archivo.read()
print(linea)

partido = linea.split(",")
print(partido[0])

archivo.close()
