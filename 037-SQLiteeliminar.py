##Librerias para trabajar con DB
import sqlite3 as mibd
import sys #leer y escribir archivos del disco duro

##Conexion a la BD denominada agenda
conexion = mibd.connect("agenda.sqlite")

##Establecer cursor para saber en que punto de BD se trabaja
cursor = conexion.cursor()

##Ejecutar sentencia SQL
cursor.execute("DELETE FROM contactos WHERE identificador = 2;")

#cerrar manualmente la conexion
conexion.commit()
