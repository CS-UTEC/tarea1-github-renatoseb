numero = int(input("Ingrese numero que quiere validar: "))
if numero < 1:
    print( "El numero no es primo :(")
elif numero == 2:
    print( "El numero es primo :D")
else:
    for i in range(2,numero):
        if numero % i == 0:
            print( "El numero no es primo :(")
            break
        else:
          print( "El numero es primo :D")
          break