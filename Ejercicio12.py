

import psycopg2

archivo=open("Ejercicio12.txt","a")
conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)


def nota(a,b,c):
    promedio=(a+b+c)/3
    if(promedio>60):
        final=str("Aprobado")
        print("Aprobado nota",round(promedio,2))
        archivo.write(final)
        archivo.write(" nota  ")
        archivo.write(str(round(promedio,2)))
        archivo.write("\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio12(nota1,nota2,nota3,promedio,notafinal) VALUES(%s,%s,%s,%s,%s);",(a,b,c,round(promedio,2),final))
        conexion.commit()
        Cursor.close()
        


    else:
        final=str("Reprobado")
        print("Reprobado nota", round(promedio,2))
        archivo.write(final)
        archivo.write(" nota ")
        archivo.write(str(round(promedio,2)))
        archivo.write("\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio12(nota1,nota2,nota3,promedio,notafinal) VALUES(%s,%s,%s,%s,%s);",(a,b,c,round(promedio,2),final))
        conexion.commit()
        Cursor.close()



print("Que desea realizar")
print("1.Obtener promedio")
print("2.Ver historial")
op=int(input("Opcion:"))

if(op==1):
    nota1=float(input("Ingrese la primera nota:"))
    nota2=float(input("Ingrese la segunda nota:"))
    nota3=float(input("Ingrese la tercera nota:"))
    nota(nota1,nota2,nota3)

if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio12;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()
    


