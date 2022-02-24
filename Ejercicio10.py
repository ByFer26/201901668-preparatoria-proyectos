from math import factorial
import psycopg2
import numpy

archivo=open("Ejercicio10.txt","a")
conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
print("1.Realizar factorial")
print("2. Ver historial")
op=int(input("Elija una opción:"))
if(op==1):
    num=int(input("Ingrese un numero:"))
    if(num%7==0):
        resultado=factorial(num)
        if(resultado>10000):
            resultado=numpy.format_float_scientific(resultado,precision=4)
        print("El factorial de",num,"Es",resultado)
        archivo.write("El factorial de  ")
        archivo.write(str(num))
        archivo.write(" Es ")
        archivo.write(str(resultado))
        archivo.write("\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio10(numero,factorial) VALUES(%s,%s);",(num,str(resultado)))
        conexion.commit()
        Cursor.close()

    else:
        print("Error el número no es divisible entre 7")
        archivo.write("Error el numero ")
        archivo.write(str(num))
        archivo.write("  no es divisible entre 7\n")

if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio10;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()
