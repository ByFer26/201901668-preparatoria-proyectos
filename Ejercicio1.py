logico=False
while(not logico):
    try: 
        print("Para salir enter")
        numero1=float(input("Ingrese el primer número:"))
        numero2=float(input("Ingrese el segundo número:"))
        numero3=float(input("Ingrese el tercer número:"))
        

        if(numero1>numero2 and numero1>numero3 and not numero2==numero3):
            resultado=numero1+numero2+numero3
            print(resultado)

        if(numero2>numero1 and numero2>numero3 and not numero1==numero3):
            resultado=numero1*numero2*numero3
            print(resultado)

        if(numero3>numero1 and numero3>numero2 and not numero1==numero2):
            print(numero1,numero2,numero3)

        if(numero1==numero2):
            print(numero3)

        if(numero1==numero3):
            print(numero2)

        if(numero2==numero3):
            print(numero1)

        if(numero1==numero2==numero3):
            print("Todos son iguales")
    
    except ValueError:
        quit()