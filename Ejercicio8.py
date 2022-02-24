
from asyncore import write
from sqlite3 import Cursor
import psycopg2
op=0;
conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)

print("Bienvenido que desea realizar")
print("1. Averiguar la cantidad de numeros primos")
print("2. Ver el historial")

op=int(input("Eliga una opcion:"))
archivo=open("Ejercicio8.txt","a")
if(op==1):
    num=int(input("Elija un numero:"))
    pares=0
    for i in range(1,num+1):
        if(i%2==1):
            pares=pares+1
    print("La cantidad de pares es:",pares)
    
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio8(numero,impares) VALUES(%s,%s);",(num,pares))
    conexion.commit()
    Cursor.close()
    archivo.write("Hasta el numero  ")
    archivo.write(str(num))
    archivo.write("  Hay  ")
    archivo.write(str(pares))
    archivo.write("  impares  \n")
    




if(op==2):
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio8;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()


    
        
   
                  

    
           


    
        
         

   
   
    
       
    

    
    

