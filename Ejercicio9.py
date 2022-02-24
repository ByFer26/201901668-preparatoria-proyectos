import psycopg2

print("Que desea realizar")
print("1. Determinar tipo de triangulo")
print("2.Ver historial")
op=int(input("Elija la operación:"))
archivo=open("Ejercicio9.txt","a")
conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)


if(op==1):
    print("Ingrese las medidas de sus lados en metros")
    lado1=float(input("Ingrese el primer lado:"))
    lado2=float(input("Ingrese el segundo lado:"))
    lado3=float(input("Ingrese el tercer lado:"))

    if(lado1==lado2==lado3):
        tipo=str("Equilatero")
        print("El tipo de triangulo es",tipo,"sus lados son",lado1,lado2,lado3)
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio9(lado1,lado2,lado3,triangulo) VALUES(%s,%s,%s,%s);",(lado1,lado2,lado3,tipo))
        conexion.commit()
        Cursor.close()
        archivo.write("El triangulo con medidas  ")
        archivo.write(str(lado1))
        archivo.write("  ")
        archivo.write(str(lado2))
        archivo.write("  ")
        archivo.write(str(lado3))
        archivo.write("  ")
        archivo.write(" es de tipo  ")
        archivo.write(str(tipo))
        archivo.write("\n")

    if(lado1==lado2  or lado1==lado3 or lado2==lado3 ):
        tipo=str("Isoceles")
        print("El tipo de triangulo es",tipo,"sus lados son",lado1,lado2,lado3)
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio9(lado1,lado2,lado3,triangulo) VALUES(%s,%s,%s,%s);",(lado1,lado2,lado3,tipo))
        conexion.commit()
        Cursor.close()
        archivo.write("El triangulo con medidas  ")
        archivo.write(str(lado1))
        archivo.write("  ")
        archivo.write(str(lado2))
        archivo.write("  ")
        archivo.write(str(lado3))
        archivo.write("  ")
        archivo.write(" es de tipo  ")
        archivo.write(str(tipo))
        archivo.write("\n")

    else:
        tipo=str("Escaleno")
        print("El tipo de triangulo es",tipo,"sus lados son",lado1,lado2,lado3)
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio9(lado1,lado2,lado3,triangulo) VALUES(%s,%s,%s,%s);",(lado1,lado2,lado3,tipo))
        conexion.commit()
        Cursor.close()
        archivo.write("El triangulo con medidas  ")
        archivo.write(str(lado1))
        archivo.write("  ")
        archivo.write(str(lado2))
        archivo.write("  ")
        archivo.write(str(lado3))
        archivo.write("  ")
        archivo.write(" es de tipo  ")
        archivo.write(str(tipo))
        archivo.write("\n")


if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio9;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()
