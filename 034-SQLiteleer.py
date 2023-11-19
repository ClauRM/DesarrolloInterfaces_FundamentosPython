##Librerias para trabajar con DB
import sqlite3 as mibd
import sys #leer y escribir archivos del disco duro

##Conexion a la BD denominada agenda
conexion = mibd.connect("agenda.sqlite")

##Establecer cursor para saber en que punto de BD se trabaja
cursor = conexion.cursor()

##Ejecutar sentencia SQL
cursor.execute("SELECT * FROM contactos;")

##datos contiene lo que devuelve la DB
datos = cursor.fetchall()#fetchone solo muestra el primer registro fetchall muestra todo

for i in datos:
    print("nombre:",i[1],"\t telefono:",i[2],"\t email:",i[3])#empieza en 1 porque el 0 es el id
