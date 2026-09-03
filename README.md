# AVANCE 2
# Como el programa nececita verificar que la resolucion de las imagenes descompuestas en listas sea la misma, es decir que las listas tengan la misma cantidad de elementos, en este avance me enfoque en hacer esa función en particular.
# La variable "verify" verifica que ambas listas hayan sido definidas por input del usuario antes de que se ejecute el while. 0 sifnifica "no se han definido los valores" y 1 "ya se han definido los valores"
# No se utilizaron muchos operadores aritmeticos en este avance porque la parte de mi proyecto que los nececita emplea temas posteriores del curso. Mi proyecto nececita operadores aritmeticos para manejar con listas anidadas. Por lo anterior decidí avanzar con otras cosas como condicionales, estructuras de decisión y arreglos.
verify=0
print("Introduzca su primer grupo de valores sin espacios en la forma -> 123, el sistema los leerá como una lista así -> [1, 2, 3].")
img1 = list(input())
print("Introduzca su segundo grupo de valores en la misma forma :)")
img2 = list(input())
res1=len(img1)
res2=len(img2)
verify=verify+1
while res1 != res2 and verify==1:
  print("Las listas no se pueden procesar, tienen que tener la misma cantidad de elementos >:D")
  print("Reintroduzca su primer grupo de valores sin espacios en la forma -> 123, el sistema los leerá como una lista así -> [1, 2, 3].")
  img1 = input()
  print("Introduzca su segundo grupo de valores en la misma forma")
  img2 = input()
  res1=len(img1)
  res2=len(img2)
if res1 == res2 and verify==1:
	print("Las listas se pueden procesar :D")
# No incluí un modulo que verifique que los valores de las listas sean estrictamenten númericos asi como uno que permita al usuario meter valores con dos decimales porque en el programa final los valores de las listas no serán dados por el usuario directamente como aquí. El input será una imagen que el programa descompondrá en listas, entonces ya en dicha forma se tendra que verificar que estas tengan la misma cantidad de elementos para proseguir. Lo importante aqui es el conteo de elementos, la entrada del usuario solo se incluye para facilitar el proceso de prueba :D





# AVANCE 1
# Proyecto-encriptacion-de-imagenes-generativa-:D
# Para la clase (TC1038): Fundamentos de programación 
# Tema elegido: “encriptación” de imágenes

# Proyecto: un cerrajero.py que pueda configurarse por el usuario para generar el código de distintas cerradura.py que al ingresarles una imagen especifica creen a partir de esta otra imagen particular utilizando la relación que existe entre ambas imágenes. De modo que si se elimina al cerrajero.py original sea difícil acceder a esa información por ejemplo para un malware que ha descargado sus archivos, siempre que se elimine la imagen “encriptada” inmediatamente después de auditarla. Cerrajero.py sería útil para compartir y consultar con mayor seguridad información sensible como contraseñas sin estar a la merced de la seguridad, transparencia y soporte de servicios de almacenamiento y mensajería digital.

# Algoritmo: 
# (Cerrajero.py(puede recibir dos imágenes como entrada del usuario ->  descompone los valores de los pixeles de las imágenes dadas en matrices que guarda en las listas imgreclusa y imgllave respectivamente -> determina un valor que bajo cierto proceso de multiplicación permita obtener las matrices de imgreclusa a partir de las de imgllave y guarda esos valores en la lista factoresdecerradura (más detalles de este proceso al final) -> imprime al usuario el código de una cerradura.py el cual ya estaba escrito en un print con la lista factoresdecerradura insertada en una sección))

# (Cerradura.py(define factoresdecerradura de acuerdo a cerrajero.py -> puede recibir una imagen del usuario como entrada -> descompone los valores de los pixeles de la imagen dada en matrices que guarda en la lista imgllave -> multiplica los valores de imgllave por los de factoresdecerradura dentro del proceso establecido por cerrajero.py y reconstruye el resultado de matrices en una imagen la cual se guarda en la lista imgreclusa -> descarga imgreclusa como archivo en la computadora.))

# El proceso bajo el cual se obtienen y manejan los factoresdecerradura está altamente sujeto a cambios. Aquí se especifica una propuesta que podría retirarse o modificarse a conveniencia del rendimiento y seguridad del programa:
n se usa en el siguiente párrafo para representar el número asignado por Python al elemento en una lista.

# Para cada valor n de ambas listas img se guarda un flotante que equivalga a: ((valor número n de imgreclusa) / (valor número n de imgllave)). De tal forma que multiplicando cada n de imgllave por su flotante correspondiente se obtengan los valores de imgreclusa. Entonces serían estos float resultantes los factoresdecerradura.

# imagen representativa de la propuesta:
<img width="2420" height="1668" alt="IMG_4324" src="https://github.com/user-attachments/assets/0ec9c212-6ab0-48e5-9ce6-14662d0b9209" />


# Limitaciones: 
# *Es posible que ambas imagenes tengan que estar en la misma resolución para emparejar sus valores adecuadamente 
# *Es posible que de usar este método el programa solo soporte ciertas resoluciones en específico para tener preparado el número de variables a definir.

# Extra:
# Muchas de las herramientas que necesito para ejecutar el programa las aprenderé a través del curso, así mismo me comprometo a investigar por mi cuenta sobre aquellas que quizá no contenga el plan de estudios como por ejemplo el uso de las librerías para transformar imágenes a listas de matrices. Además aún necesito averiguar más a detalle qué tan viable es la propuesta que tengo para los factoresdecerradura para el tipo de información numérica que procesa Python para los colores de un píxel. 

# Desconozco si el término “encriptar” resulta adecuado para el algoritmo descrito, por ello añado las comillas y esta aclaración. 

