import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio7.txt","a")
print("Que desea realizar")
print("1.Calcular las vocales:")
print("2.Ver historial:")
op=int(input("Opcion:"))

logico=False
while(not logico):
    if(op==1):
        palabra=input("Ingrese una palabra:")
        a=0;
        e=0;
        i1=0;
        o=0;
        u=0;
        for i in palabra: 
            if(i=='a' or i=='A' ):
                a=a+1

            if(i=='e' or i=='E'):
                e=e+1

            if(i=='i' or i=='I'):
                i1=i1+1
            
            if(i=='o' or i=='O'):
                o=o+1

            if(i=='u' or i=='U'):
                u=u+1

        print("La palabra:", palabra ,"Tiene las vocales:\n","a=",a," \n","e=",e,"\n","i=",i1,"\n","o=",o,"\n","u=",u)
        archivo.write("La palabra: "+palabra+" Tiene las vocales: \n"+"a="+str(a)+" \n"+"e="+str(e)+"\n"+"i="+str(i1)+"\n"+"o="+str(o)+"\n"+"u="+str(u))
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO ejercicio7(palabra,letraa,letrae,letrai,letrao,letrau) VALUES(%s,%s,%s,%s,%s,%s);",(palabra,a,e,i1,o,u))
        conexion.commit()
        Cursor.close()

    if(op==2):
        Cursor=conexion.cursor()
        SQL='SELECT*FROM ejercicio7;'
        Cursor.execute(SQL)
        valores=Cursor.fetchall()
        print(valores)
        Cursor.close()
        quit()



