import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio5.txt","a")
print("Que desea realizar")
print("1.Los números de 2 en 2 ")
print("2. Ver historial")
op=int(input("Opción:"))

if op==1:
    num1=int(input("Ingrese el primer número:"))
    num2=int(input("Ingrese el segundo número:"))

    if(num1>num2 and num2%2==0):
        for i in range(num2,num1+1):
            if(i%2==0):
                print(i)
        archivo.write("Los numeros son "+str(num2)+" a "+str(num1)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio5(num1,num2) VALUES(%s,%s);",(num1,num2))
        conexion.commit()
        Cursor.close()
                

    else:
        for i in range(num1,num2+1):
            if(i%2==0):
                print(i)
        archivo.write("Los numeros son "+str(num1)+" a "+str(num2)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio5(num1,num2) VALUES(%s,%s);",(num2,num1))
        conexion.commit()
        Cursor.close()

if op==2:
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio14;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()






