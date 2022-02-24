from cmath import pi
import psycopg2
import numpy

archivo=open("Ejercicio11.txt","a")
conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)

print("Que desea realizar")
print("1. Area de un circulo")
print("2. Area de un cuadrado")
print("3. Area de un rectangulo")
print("4. Area de un triangulo")
print("5. Ver el historial")
op=int(input("Opción:"))

if(op==1):
    figura=str("Circulo")
    radio=float(input("Radio del circulo:"))
    resultado=(radio**2)*pi
    print("El circulo de radio",radio,"tiene un area de ", round(resultado,4))
    archivo.write("El circulo de radio:")
    archivo.write(str(radio))
    archivo.write(" tiene un area de ")
    archivo.write(str(round(resultado,4)))
    archivo.write("\n")
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio11(figura,area) VALUES(%s,%s);",(figura,round(resultado,4)))
    conexion.commit()
    Cursor.close()

if(op==2):
    figura=str("Cuadrado")
    arista=float(input("Ingrese el lado del cuadrado:"))
    resultado=arista*arista
    print("El cuadrado de lado",arista,"tiene un area de ",round(resultado,4))
    archivo.write("El cuadrado de lado ")
    archivo.write(str(arista))
    archivo.write(" tiene un area de ")
    archivo.write(str(round(resultado,4)))
    archivo.write("\n")
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio11(figura,area) VALUES(%s,%s);",(figura,round(resultado,4)))
    conexion.commit()
    Cursor.close()

if(op==3):
    figura=str("Rectangulo")
    ancho=float(input("Ingrese en ancho del rectangulo:"))
    largo=float(input("Ingrese el largo del rectangulo:"))
    resultado=ancho*largo
    print("El rectangulo de dimensiones ",ancho,"x",largo,"tiene un area de ",round(resultado,4))
    archivo.write("El rectangulo de dimensiones ")
    archivo.write(str(ancho))
    archivo.write(" x ")
    archivo.write(str(largo))
    archivo.write(" tiene un area de ")
    archivo.write(str(round(resultado,4)))
    archivo.write("\n")
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio11(figura,area) VALUES(%s,%s);",(figura,round(resultado,4)))
    conexion.commit()
    Cursor.close()


if(op==4):
    figura=str("Triangulo")
    base=float(input("Ingrese la base del triangulo:"))
    altura=float(input("Ingrese la altura del triangulo:"))
    resultado1=base*altura
    resultado=resultado1/2
    print("El triangulo de base",base," y altura",altura,"tiene un area de",round(resultado,4))
    archivo.write("El triangulo de base ")
    archivo.write(str(base))
    archivo.write(" y altura ")
    archivo.write(str(altura))
    archivo.write(" tiene un area de ")
    archivo.write(str(round(resultado,4)))
    archivo.write("\n")
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio11(figura,area) VALUES(%s,%s);",(figura,round(resultado,4)))
    conexion.commit()
    Cursor.close()

if(op==5):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio11;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()