import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio3.txt","a")
try:
    print("Presione enter para salir")
    print("Que desea realizar")
    print("1.Averiguar la cantidad de vocales")
    print("2.Ver el historial")
    op=int(input("Opción:"))
    if op==1:
        palabra=input("Ingrese una palabra:")
        vocales=0
        for i in palabra:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vocales=vocales+1
                    
        print("La palabra:",palabra, "tiene",vocales,"vocales") 
        archivo.write("La palabra "+palabra+" tiene "+str(vocales)+" vocales \n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio3(palabra,vocales) VALUES(%s,%s);",(palabra,vocales))
        conexion.commit()
        Cursor.close()

    if op==2:
        Cursor=conexion.cursor()
        SQL='SELECT*FROM ejercicio3;'
        Cursor.execute(SQL)
        valores=Cursor.fetchall()
        print(valores)
        Cursor.close()


except ValueError:
    quit()

