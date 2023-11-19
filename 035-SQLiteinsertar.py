##Librerias para trabajar con DB
import sqlite3 as mibd
import sys #leer y escribir archivos del disco duro

##Conexion a la BD denominada agenda
conexion = mibd.connect("agenda.sqlite")

##Establecer cursor para saber en que punto de BD se trabaja
cursor = conexion.cursor()

##Ejecutar sentencia SQL
cursor.execute("INSERT INTO contactos VALUES(NULL,'Jorge','789012','info@jorge.com');")

#cerrar manualmente la conexion
conexion.commit()
