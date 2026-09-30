print ("1.-Sumar")
print ("2.-Restar")
print ("3.-Multiplicar")
print ("4.-Dividir")
print ("5.-Salir")
opción=0
while (opción!=5):
   opción= float (input("Di que opción quieres ="))
   dato1=int(input("dato1 ="))
   dato2=int(input("dato2 ="))
   if (opción==1):
        print (dato1,"+",dato2,"=",dato1 + dato2)
else:
       if (opción==2):
           print (dato1,"-",dato2,"=",dato1 - dato2)
       else:
           if (opción==3):
               print (dato1,"*",dato2,"=",dato1 * dato2)
           else:
               if (opción==4):
                    print (dato1,"/",dato2,"=", dato1 / dato2)
               else:
                   if (opción==5):
                       print ("Adiós")