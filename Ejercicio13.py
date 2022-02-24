

import psycopg2



conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio13.txt","a")
print("Que desea realizar")
print("1.Averiguar si es año biciesto")
print("2.Ver el historial")
op=int(input("Opción:"))

if(op==1):
    Year = int(input("Ingrese el año:"));
    Yearstr=str(Year)
    bisiesto = Year/4;

    if bisiesto == int(bisiesto):
        tipo=str("Bisiesto")
        print(Year,"es bisiesto.")
        archivo.write("El año "+Yearstr+" es biciesto\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio13(anio,tipo) VALUES(%s,%s);",(Year,tipo))
        conexion.commit()
        Cursor.close()


    else:
        print(Year,"no es bisiesto.")
        tipo=str("No es bisiesto")
        archivo.write("El año "+Yearstr+" no es bisiesto \n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio13(anio,tipo) VALUES(%s,%s);",(Year,tipo))
        conexion.commit()
        Cursor.close()

if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio13;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()




