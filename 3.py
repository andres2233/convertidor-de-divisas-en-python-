#hacer un conversor de diferentes monedas en donde se pueda cambiar de dolar a pesos de cada pais y viseversa de peso a dolar , ingresando/
#la monda y la cantida a cambair 

def app(moneda,cantidad) : 
    valor = 0 
    # moneda colombiana  a dolar 
    if moneda == 1:
        valor = cantidad * 0.00028
        print('tus {} pesos colombianoes quivalen a {} dolares'.format(cantidad, valor) )
    # de dolar a moneda colombiana
    elif moneda == 2: 
        
        valor =  cantidad * 3.622 
        valor = round(valor,4 )
        print('tus {} dolares quivalen a {} pesos colombianos '.format(cantidad, valor ))
    
    # Moneda chilena2
    elif moneda == 3:
        valor = cantidad * 0.0014
        print('Los {} pesos chilenos equivalen a {} dolares'.format(cantidad, valor ))
    elif moneda ==4:
        valor = cantidad * 713
        print('los {} dolares quivalen a {} pesos chilenos'.format(cantidad, valor ) )
    # Moneda Argentina
    elif moneda ==5:
        valor = cantidad * 0.014
        print('Los {} pesos argentinos equivalen a {} dolares'.format(cantidad, valor ))
    elif moneda == 6 : 
        valor = cantidad * 93.14
        print('los {} dolares equivalen a {} pesos argentinos'.format(cantidad, valor ))
    # Moneda mexicana
    elif moneda == 7:
        valor = cantidad * 0.044
        print('Los {} pesos mexicanos equivalen a {} dolares'.format(cantidad, valor ))
    elif moneda ==8 : 
        valor = cantidad * 19.83
        print('los {} dolares equivalen a {} dolares '.format(cantidad, valor))
    # Otro
    else:
        print('Ingresa solo un numero de la lista')


try : 

    moneda = int(input(
    '''Bienvenido A  Convertidor De Moneda.py
      selecioina la moneda que quieres convertir ...
      [1] pesos colombianos a dolar 
      [2] dolar a pesos colombianos 
      [3] moneda chilena a dolar 
      [4] dolar a moneda chilena 
      [5] moneda argentina a dolar 
      [6] dolara moneda argentina 
      [7] moneda mexicana a dolar 
      [8] dolar a moneda mexicana 
    Ingresa Tu Opción :  '''))
    print('***********************************************')
    cantidad = int(input( 'Ingresa la cantidad que deseas convertir ' ) )

    
    app(moneda,cantidad)


except : 
    print('ha ocurrido un error ')

