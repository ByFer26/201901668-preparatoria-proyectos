logico=False
while(not logico):
    try:
        print("Presione enter para salir")
        palabra=input("Ingrese una palabra:")
        vocales=0
        for i in palabra:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                
                vocales=vocales+1
            
        print("La palabra:",palabra, "tiene",vocales,"vocales") 
    
    except ValueError:
        quit()
