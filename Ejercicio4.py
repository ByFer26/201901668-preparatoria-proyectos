import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio4.txt","a")
print("Que desea realizar")
print("1.Encontrar la suma hasta x numero")
print("2.Ver el historial")
op=int(input("Opción:"))

if op==1:
    try:
        print("Para salir presione enter")
        numero=int(input("Ingrese un numero:"))
        resultado=0
        
        for i in range(0,numero+1):
            resultado =resultado+i
        print("El resultado es:",resultado)  
        archivo.write("La suma de los numeros desde 1 hasta "+str(numero)+" es "+str(resultado)+"\n")  
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio4(numero,suma) VALUES(%s,%s);",(numero,resultado))
        conexion.commit()
        Cursor.close()
        
    except ValueError:
            quit()

if op==2:
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio4;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()

