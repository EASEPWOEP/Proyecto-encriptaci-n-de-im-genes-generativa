
Proyecto-Cerrajero.py
Para la clase (TC1038): Fundamentos de programación 
Tema elegido: 

El presente proyecto apela a la vulnerabilidad de seguridad y privacidad que supone que un programa destinado a guardar datos sensibles los tenga almacenados en la memoria del computador para facilitarlos cuando se le presente cierta clave. Esto es especialmente relevante en el contexto actual del internet con el auge de servicios de nube en línea masivos como Google drive y ICloud que podrían padecer de ataques o de los limitados escrúpulos de algunos desarrolladores en equipos de trabajo grandes. Específicamente ahora que existe más demanda que nunca es que los mercados ilegales de información podrían expandirse, dado el gran interés económico de que existe torno tecnologías de inteligencia artificial que se alimentan de este recurso. Esto sin mencionar el problema fundamental de las contraseñas, que es que tienden a ser reutilizadas. Cerrajero.py es un generador de programas de almacenamiento de datos con contraseña personalizados, recibe dos conjuntos de números e imprime un programa que permite acceder a cierto conjunto al proporcionarle el otro, con la particularidad de que ni él ni los programas que fabrica guardan directamente la información que almacenan en la memoria. Esto es posible porque las artesanías de Cerrajero.py no otorgan acceso en base a coincidencia, o mejor dicho no otorgan acceso en realidad, estas solo contienen un valor matemáticamente relacionado en igual proporción a ambos de los grupos de elementos dados tal que su función es revertir el proceso que hizo ese valor para reconstruir al otro argumento de la operación a partir del input del usuario. Es decir, ambos valores son contraseñas simultáneamente, de forma que ninguno acaba siendo información guardada en memoria. Esto es útil también si se recuerda la información pero no la contraseña cuando resulta que la contraseña se utiliza también para otras cosas, de forma que reutilizar puede ser ventajoso hasta cierto punto.

Abajo se detalla información elemental del funcionamiento del programa tanto para usuarios como para desarrolladores, es deseable leer este apartado antes de adentrarse en el prototipo:

Vista de usuario:
La entrada que el cerrajero acepta son los valores uno por uno de dos listas de números con la misma cantidad de elementos, la salida que tiene es código impreso en la consola al que se le denomina en el presente documento como cerradura.  

Si se pega a la cerradura en una terminal como código la entrada que acepta esta es una lista de números, la salida que tiene es otra lista de números o error si la lista proporcionada no contiene la misma cantidad de elementos que las listas que se le proporcionaron al cerrajero para imprimir a la cerradura en cuestión en primer lugar.


Vista del desarrollador:
Los valores del usuario se guardan como elementos de listas en la memoria mediante las variables llave1 y llave2. El producto de los valores con el mismo índice de llave1 entre llave2 se guardan como una sola lista en la memoria en la variable cerradura en los mismos índices en los que estaban los valores originales, al hacer este proceso se cortan y pegan los valores dados por el usuario de llave1 y llave2 de forma que se borran de la memoria. Se imprime una plantilla que contiene la lista almacenada en cerradura.

Los valores del usuario se guardan como elementos de una lista en la memoria mediante la variable llave. El cociente de los valores con el mismo índice de cerradura entre llave se guarda como una sola lista en la memoria en la variable salida en los mismos índices en los que estaban los valores originales. Se imprime salida.
