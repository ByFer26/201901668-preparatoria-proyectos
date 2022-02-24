import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio6.txt","a")
print("Que desea realizar:")
print("1.Ordenar numeros:")
print("2.Ver historial:")
op=int(input("Opcion:"))


logico=False
while(not logico):
    if op==1:
        try:
            print("Para salir presione enter")
            num1=int(input("Ingrese el primer número:"))
            num2=int(input("Ingrese el segundo número:"))

            if(num1>num2):
                for i in range(num2,num1+1):
                    dist=num1+num2
                    print(-(i-dist))
                    archivo.write("Los numeros son "+str(num1)+" "+str(num2)+"\n")
                    Cursor=conexion.cursor()
                    Cursor.execute("INSERT INTO ejercicio6(numero1,numero2) VALUES(%s,%s);",(num1,num2))
                    conexion.commit()
                    Cursor.close()

            else:
                for i in range(num1,num2+1):
                    dist=num2+num1
                    print(-(i-dist))
                    archivo.write("Los numeros son "+str(num1)+" "+str(num2)+"\n")
                    Cursor=conexion.cursor()
                    Cursor.execute("INSERT INTO ejercicio6(numero1,numero2) VALUES(%s,%s);",(num1,num2))
                    conexion.commit()
                    Cursor.close()


        except ValueError:
            quit()

    if op==2:
        Cursor=conexion.cursor()
        SQL='SELECT*FROM ejercicio6;'
        Cursor.execute(SQL)
        valores=Cursor.fetchall()
        print(valores)
        Cursor.close()
        quit()
    

