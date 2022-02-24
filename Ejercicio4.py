import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio4.txt","a")

try:
    print("Para salir presione enter")
    numero=int(input("Ingrese un numero:"))
    resultado=0
    
    for i in range(0,numero+1):
        resultado =resultado+i
    print("El resultado es:",resultado)    
    
except ValueError:
        quit()

