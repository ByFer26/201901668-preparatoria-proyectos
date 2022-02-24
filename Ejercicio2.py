import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio2.txt","a")
try:
    print("Para salir presione enter")
    print("Que desea realizar")
    print("1. Averiguar la cantidad de divisores")
    print("2.Ver el historial")
    op=int(input("Ingrese una opción:"))
    if op==1:
        num=int(input("Ingrese un número:"))
        divisores=0
        for i in range(1,num+1):
            num//i
            if(num%i==0):
                print(i)
                divisores=divisores+1
                archivo.write("El numero "+str(num)+" tiene como divisor a "+str(i)+"\n")
        print("El numero",num,"tiene",divisores,"divisores")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio2(numero,divisores) VALUES(%s,%s);",(num,divisores))
        conexion.commit()
        Cursor.close()
    
    if op==2:
        Cursor=conexion.cursor()
        SQL='SELECT*FROM ejercicio2;'
        Cursor.execute(SQL)
        valores=Cursor.fetchall()
        print(valores)
        Cursor.close()
        

except ValueError:
        quit()

    


