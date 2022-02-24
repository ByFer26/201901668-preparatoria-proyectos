import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)



archivo=open("ejercicio14.txt","a")
def estado(a,b):
    if (a<2007 and b>20000):
        estad=str("Debe renovarse")
        print("Debe renovarse")
        archivo.write("El taxi debe renovarse modelo "+str(a)+" kilometraje "+str(b)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio14(modelo,kilometraje,estado) VALUES(%s,%s,%s);",(a,b,estad))
        conexion.commit()
        Cursor.close()
    
    if(2007<a<2013 and b>20000):
        estad=str("Mantenimiento")
        print("Debe recibir mantenimiento")
        archivo.write("El taxi deber recibir mantenimiento "+str(a)+" kilometraje "+str(b)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio14(modelo,kilometraje,estado) VALUES(%s,%s,%s);",(a,b,estad))
        conexion.commit()
        Cursor.close()

    if(a>2013 and b<10000):
        estad=str("Optimo estado")
        print("Esta en optimo estado")
        archivo.write(" El taxi esta en optimo estado "+str(a)+" kilometraje "+str(b)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio14(modelo,kilometraje,estado) VALUES(%s,%s,%s);",(a,b,estad))
        conexion.commit()
        Cursor.close()

    else:
        estad=str("Mecanico")
        print("Mecanico")
        archivo.write("Consulte al mecanico"+str(a)+" kilometraje "+str(b)+"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio14(modelo,kilometraje,estado) VALUES(%s,%s,%s);",(a,b,estad))
        conexion.commit()
        Cursor.close()


        
    

print("Que desea realizar")
print("1.Ingresar datos del taxi")
print("2. Ver estado de los taxis")
op=int(input("Opción:"))

if op==1:
    Modelo=int(input("Ingrese el modelo del taxi:"))
    Kilometraje=float(input("Ingrese los kilometros recorridos:"))
    estado(Modelo,Kilometraje)

if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio14;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()

