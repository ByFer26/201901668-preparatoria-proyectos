import psycopg2

conexion=psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="netacad20",
    dbname="Preparatoria"
)
archivo=open("ejercicio1.txt","a")
print("Que desea realizar")
print("1.Ingresar los 3 numeros")
print("2.Ver el historial")
op=int(input("Opción:"))

def operacion(a,b,c):
    archivo.write("Los números son:"+str(a)+str(b)+str(c)+" y el reultado es "+str(resultado)+"\n")
    Cursor=conexion.cursor()
    Cursor.execute("INSERT INTO ejercicio1(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(a,b,c,str(resultado)))
    conexion.commit()
    Cursor.close()

if op==1:
    try: 
        print("Para salir enter")
        numero1=float(input("Ingrese el primer número:"))
        numero2=float(input("Ingrese el segundo número:"))
        numero3=float(input("Ingrese el tercer número:"))
            

        if(numero1>numero2 and numero1>numero3 and not numero2==numero3):
            resultado=numero1+numero2+numero3
            print(resultado)
            operacion(numero1,numero2,numero3)

        if(numero2>numero1 and numero2>numero3 and not numero1==numero3):
            resultado=numero1*numero2*numero3
            print(resultado)
            operacion(numero1,numero2,numero3)

        if(numero3>numero1 and numero3>numero2 and not numero1==numero2):
            resultado=numero1,numero2,numero3
            print(numero1,numero2,numero3)
            operacion(numero1,numero2,numero3)

        if(numero1==numero2):
            resultado=numero3
            print(numero3)
            operacion(numero1,numero2,numero3)
            

        if(numero1==numero3):
            resultado=numero2
            print(numero2)
            operacion(numero1,numero2,numero3)

        if(numero2==numero3):
            resultado=numero1
            print(numero1)
            operacion(numero1,numero2,numero3)

        if(numero1==numero2==numero3):
            resultado=str("Todos son iguales")
            print("Todos son iguales")
        operacion(numero1,numero2,numero3)
        
    except ValueError:
            quit()

if op==2:
    Cursor=conexion.cursor()
    SQL='SELECT*FROM ejercicio1;'
    Cursor.execute(SQL)
    valores=Cursor.fetchall()
    print(valores)
    Cursor.close()