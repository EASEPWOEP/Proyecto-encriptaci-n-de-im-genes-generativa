# Proyecto-encriptacion-de-imagenes-generativa-:D
Para la clase (TC1038): Fundamentos de programación 
Tema elegido: “encriptación” de imágenes

Proyecto: un cerrajero.py que pueda configurarse por el usuario para generar el código de distintas cerradura.py que al ingresarles una imagen especifica creen a partir de esta otra imagen particular utilizando la relación que existe entre ambas imágenes. De modo que si se elimina al cerrajero.py original sea difícil acceder a esa información por ejemplo para un malware que ha descargado sus archivos, siempre que se elimine la imagen “encriptada” inmediatamente después de auditarla. Cerrajero.py sería útil para compartir y consultar con mayor seguridad información sensible como contraseñas sin estar a la merced de la seguridad, transparencia y soporte de servicios de almacenamiento y mensajería digital.

Algoritmo: 
(Cerrajero.py(puede recibir dos imágenes como entrada del usuario ->  descompone los valores de los pixeles de las imágenes dadas en matrices que guarda en las listas imgreclusa y imgllave respectivamente -> determina un valor que bajo cierto proceso de multiplicación permita obtener las matrices de imgreclusa a partir de las de imgllave y guarda esos valores en la lista factoresdecerradura (más detalles de este proceso al final) -> imprime al usuario el código de una cerradura.py el cual ya estaba escrito en un print con la lista factoresdecerradura insertada en una sección))

(Cerradura.py(define factoresdecerradura de acuerdo a cerrajero.py -> puede recibir una imagen del usuario como entrada -> descompone los valores de los pixeles de la imagen dada en matrices que guarda en la lista imgllave -> multiplica los valores de imgllave por los de factoresdecerradura dentro del proceso establecido por cerrajero.py y reconstruye el resultado de matrices en una imagen la cual se guarda en la lista imgreclusa -> descarga imgreclusa como archivo en la computadora.))

El proceso bajo el cual se obtienen y manejan los factoresdecerradura está altamente sujeto a cambios. Aquí se especifica una propuesta que podría retirarse o modificarse a conveniencia del rendimiento y seguridad del programa:
n se usa en el siguiente párrafo para representar el número asignado por Python al elemento en una lista.

Para cada valor n de ambas listas img se guarda un flotante que equivalga a: ((valor número n de imgreclusa) / (valor número n de imgllave)). De tal forma que multiplicando cada n de imgllave por su flotante correspondiente se obtengan los valores de imgreclusa. Entonces serían estos float resultantes los factoresdecerradura.

imagen representativa de la propuesta:
<img width="2420" height="1668" alt="IMG_4324" src="https://github.com/user-attachments/assets/0ec9c212-6ab0-48e5-9ce6-14662d0b9209" />


Limitaciones: 
*Es posible que ambas imagenes tengan que estar en la misma resolución para emparejar sus valores adecuadamente
*Es posible que de usar este método el programa solo soporte ciertas resoluciones en específico para tener preparado el número de variables a definir.

Extra:
Muchas de las herramientas que necesito para ejecutar el programa las aprenderé a través del curso, así mismo me comprometo a investigar por mi cuenta sobre aquellas que quizá no contenga el plan de estudios como por ejemplo el uso de las librerías para transformar imágenes a listas de matrices. Además aún necesito averiguar más a detalle qué tan viable es la propuesta que tengo para los factoresdecerradura para el tipo de información numérica que procesa Python para los colores de un píxel. 

Desconozco si el término “encriptar” resulta adecuado para el algoritmo descrito, por ello añado las comillas y esta aclaración. 

