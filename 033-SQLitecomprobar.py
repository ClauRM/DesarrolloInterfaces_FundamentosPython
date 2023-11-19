##Librerias y modulos que se pueden importar
##https://docs.python.org/3/library/index.html
##https://docs.python.org/3/py-modindex.html

##Librerias para trabajar con DB
import sqlite3 as mibd
import sys #leer y escribir archivos del disco duro

##Conexion a la BD denominada agenda
conexion = mibd.connect("agenda.sqlite")

##Establecer cursor para saber en que punto de BD se trabaja
cursor = conexion.cursor()

##Le pido algo a la BD en lenguaje SQL
cursor.execute("SELECT SQLITE_VERSION()")

##datos contiene lo que devuelve la DB
datos = cursor.fetchone()
print("La version de SQLite es:",datos)
