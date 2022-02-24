logico=False
while(not logico):

    try:
        print("Para salir presione enter")
        num=int(input("Ingrese un número:"))

        for i in range(1,num+1):
            num//i
            if(num%i==0):
                print(i)

    except ValueError:
        quit()

    


