#Procedimiento para recibir una lista del usuario
#con una cantidad arbitraria de elementos.
# Para este avance (6) se corrigio un bug en el que 
# las listas de los mensajes no se reseteaban cuando 
# se requeria reintroducirlas por no tener la misma 
# cantidad de valores. Asimismo los valores de las 
# listas ahora se procesan como float para aumentar 
# la complejidad que los mensajes pueden tener y 
# para evitar errores por tipo de dato numerico. 
# Finalmente, se subio el codigo en formato python como 
# indican los estandares de repositorio de la industria. 

def guardar_msg(r_msg):
  interruptor1 = True
  while interruptor1 is True:
    entrada = (float(input(':>')))
    consulta = input('DESEA CONTINUAR? ESCRIBA SI O NO')
    interruptor2 = True
    while interruptor2 is True:
      if consulta == 'NO':
        r_msg.append(entrada)
        print(r_msg)
        interruptor2 = False
        interruptor1 = False
      elif consulta == 'SI':
        r_msg.append(entrada)
        interruptor2 = False
      else:
        print('RESPUESTA NO VALIDA, intente GRITAR')
        consulta = input()
  return r_msg


#Procedimiento para inicializar el resto del algoritmo
#recibiendo los valores del usuario y asegurando 
#que estos se puedan procesar.
def inicializar():
  msg1 = []
  msg2 = []
  print("INTRODUZCA CADA VALOR (DECIMAL O ENTERO) DE LA LISTA DEL MENSAJE ENCERRADO UNO POR " \
  "UNO")
  guardar_msg(msg1)
  print("INTRODUZCA CADA VALOR (DECIMAL O ENTERO) DE LA LISTA DEL MENSAJE CERRADURA UNO " \
  "POR UNO")
  guardar_msg(msg2)
  tam1 = len(msg1)
  tam2 = len(msg2)
  interruptor1 = True
  while tam1 != tam2 and interruptor1 is True:
    msg1 = []
    msg2 = []
    print("LAS LISTAS TIENEN QUE TENER LA MISMA CANTIDAD DE ELEMENTOS," \
    " VUELVA A INTENTAR >:D")
    print("INTRODUZCA CADA VALOR DE LA LISTA DEL MENSAJE ENCERRADO " \
    "UNO POR UNO")
    guardar_img(msg1)
    print("INTRODUZCA CADA VALOR DE LA LISTA DEL MENSAJE CERRADURA UNO " \
    "POR UNO")
    guardar_img(msg2)
    tam1 = len(msg1)
    print(tam1)
    tam2 = len(msg2)
    print(tam2)
    if tam1 == tam2:
      interruptor = False
  print("Las listas se pueden procesar :D")
  return [msg1, msg2]

#Procedimiento para obtener la lista cerradura, cuyos valores son
# los valores de las dos listas dadas por el usuario multiplicados
# entre si por indice.
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

#Procedimiento para imprimirle al usuario el codigo en python
#de la cerradura para que este pueda ejecutarlo en una terminal.
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


imprimir(preparar(inicializar()))

#NOTAS 1. la funcion imprimir carece de capacidad de indentacion alguna,
# esta trabaja basicamente con una plantilla de codigo, por tanto cuando 
# la cantidad de caracteres en las listas que proporciona el usuario es 
# lo suficientemente masiva el codigo se imprime incorrectamente
# (la cantidad de caracteres con la que esto pasa es muy grande,
# asi que podria descartarse mejorar esto para futuras versiones
# si consume demasiado tiempo) 