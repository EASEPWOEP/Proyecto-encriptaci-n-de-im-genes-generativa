
"""
================================
Funciones atomicas del programa:
================================

# Se emplea uso de cadenas de texto en los condicionales de la
# funcion para mejorar la experiencia del usuario, ahora se pueden
# escribir variedades de SI y NO como SIP,NOP,SIII,NOOO. Se enfatizan
# las mayusculas en las instrucciones para dirijir la atencion 
# del operador. Adicionalmente el programa ahora puede recibir listas
# anidadas, pero como la implementación para que las pueda procesar
# aun no esta totalmente lista para emplearse no se incluyo en esta entrega.

guardar_msg(r_msg): Procedimiento para recibir listas con una arbitraria 
de elementos del usuario, se toman los valores uno
por uno y se le pregunta al usuario si desea continuar
antes de ir al siguiente.
"""
def guardar_msg(r_msg):
  caja = []
  interruptor1 = True
  while interruptor1 is True:
    entrada = input(":>")
    print(entrada)
    consulta = input(print("¿Desea continuar modificando la lista?"
                           " Escriba 'SI' o 'NO' en consola"))
    interruptor2 = True
    while interruptor2 is True:
      if "NO" in consulta:
          entrada = float(entrada) 
          r_msg.append(entrada)
          print(r_msg)
          interruptor2 = False
          interruptor1 = False
      
          
      if  "SI" in consulta:
          if "ANIDAR" in (str(entrada)):
              for i in range(len(r_msg)):
                  caja.append(r_msg.pop(0))
              r_msg.append(caja)
              caja = []
          else:
            r_msg.append(float(entrada))
          print(r_msg)
          interruptor2 = False
          
      else:
          print("RESPUESTA NO VALIDA, intente GRITAR")
          interruptor2 = False
  print(r_msg)


"""
===================================
Funciones moleculares del programa:
===================================


inicializar(): Procedimiento para inicializar el resto del algoritmo
recibiendo los valores del usuario y asegurando 
que estos se puedan procesar.
"""
def inicializar():
  msg1 = []
  msg2 = []
  print("Introduzca uno por uno cada valor (decimal o entero) de su PRIMERA lista, "
        "o utilice el comando 'ANIDAR' para separar los valores que ya ha ingresado en una"
        " nueva lista interna")
  guardar_msg(msg1)
  print("Introduzca uno por uno cada valor (decimal o entero) de su SEGUNDA lista, "
        "o utilice el comando 'ANIDAR' para separar los valores que ya ha"
        " ingresado "
        "en una nueva lista interna")
  guardar_msg(msg2)
  tam1 = len(msg1)
  tam2 = len(msg2)
  interruptor1 = True
  while tam1 != tam2 and interruptor1 is True:
    msg1 = []
    msg2 = []
    print("LAS LISTAS TIENEN QUE TENER LA MISMA CANTIDAD DE ELEMENTOS, "
          "vuelva a intentar >:D")
    print("Introduzca uno por uno cada valor (decimal o entero) de su PRIMERA lista, "
          "o utilice el comando ANIDAR para separar los valores que ya ha ingresado en una"
          "nueva lista interna")
    guardar_msg(msg1)
    print("Introduzca uno por uno cada valor (decimal o entero) de su SEGUNDA lista,"
          "o utilice el comando 'ANIDAR' para separar los valores que ya ha ingresado en una"
          "nueva lista interna")
    guardar_msg(msg2)
    tam1 = len(msg1)
    print(tam1)
    tam2 = len(msg2)
    print(tam2)
    if tam1 == tam2:
      interruptor = False
  print("LAS LISTAS SE PUEDEN PROCESAR :D")
  return [msg1, msg2]
  
  
"""
preparar(mensajes): Procedimiento para obtener la lista cerradura, cuyos valores son
los valores de las dos listas dadas por el usuario multiplicados 
entre si por indice.
"""
def preparar(mensajes):
  cerr = []
  interruptor2 = True
  conteo = len(mensajes[0])
  while interruptor2 is True:
    vec1 = mensajes[0].pop(0)
    vec2 = mensajes[-1].pop(0)
    cerr.append((vec1*vec2))
    if conteo == len(cerr):
      interruptor2 = False
  return cerr
  
  
"""
imprimir(cerradura): Procedimiento para imprimirle al usuario el codigo en python
de la cerradura para que este pueda ejecutarlo en una terminal.
"""
def imprimir(cerradura):
  print("llave = []")
  print("cerradura =",cerradura)
  print("salida = []")
  print("interruptor1 = True ")
  print("while interruptor1 is True:")
  print("  entrada = (float(input('INTRODUZCA LLAVE')))")
  print("  consulta = input('DESEA CONTINUAR? ESCRIBA SI O NO')")
  print("  interruptor2 = True")
  print("  while interruptor2 is True:")
  print("    if consulta == 'NO':")
  print("      llave.append(entrada)")
  print("      interruptor2 = False")
  print("      interruptor1 = False")
  print("    elif consulta == 'SI':")
  print("      llave.append(entrada)")
  print("      interruptor2 = False")
  print("    else:")
  print("      print('RESPUESTA NO VALIDA, intente GRITAR')")
  print("      consulta = input()")
  print("for i in range(len(llave)):")
  print("  x = cerradura.pop(0)")
  print("  y = llave.pop(0)")
  print("  salida.append(x / y)")
  print("print(salida)")
  
  
"""
=============================
Parte principal del programa:
=============================
"""
imprimir(preparar(inicializar()))
