# INFORME TF_PCD

El proyecto consistio en:
Utilizando programacion distribuida implementar un programa en Go que implementa un juego de salto entre nodos conectados en red. El juego consiste en que los jugadores saltan de un nodo a otro en función de comandos recibidos.

Lo desarollado incluye:

1.Un backend sencillo en Flask que manejará una solicitud POST y GET con la entidad Message

En este código, se agregaron tres funciones para manejar la base de datos SQLite:

create_table() crea la tabla "messages" si no existe.
insert_message() inserta un nuevo mensaje en la base de datos.
get_all_messages() recupera todos los mensajes de la base de datos.
En la función handle_message(), se inserta el mensaje recibido en la base de datos llamando a insert_message().

En la función get_message(), se obtienen todos los mensajes de la base de datos llamando a get_all_messages(). Luego, se crea una lista de diccionarios con los mensajes en el formato esperado y se devuelve como respuesta JSON.


2.Un frontend sencillo utilizando HTML, JavaScript para mostrar los movimientos del juego de salto entre nodos obtenidos a través del endpoint GET en la aplicación Flask

Diseño de la aplicacion:
![image](https://github.com/WilmarTarazona/TF_PCD/assets/64874245/ee0e0161-8194-44b8-8435-9c762bbb13f8)


3.Un programa en Go que implementa un juego de salto entre nodos conectados en red. El juego consiste en que los jugadores saltan de un nodo a otro en función de comandos recibidos.

Aquí hay un resumen del código y su funcionalidad:

Se definen tres estructuras de datos: Player, Message e Info. La estructura Player representa a un jugador y tiene campos como el equipo, el hogar y el origen. La estructura Message representa un mensaje enviado entre nodos y contiene un comando, un nombre de host y un jugador. La estructura Info se utiliza para almacenar información sobre el equipo, el nombre de host, los nodos previo y siguiente, y un posible retador.

La función listen se encarga de establecer un servidor TCP en el host especificado y escuchar las conexiones entrantes. Cuando se acepta una conexión, se llama a la función handle en una goroutine para manejarla de forma concurrente.

La función handle procesa una conexión entrante. Primero, decodifica el mensaje JSON recibido en una estructura Message. Luego, dependiendo del comando recibido, realiza diferentes acciones. Si el comando es "jump", se extrae información del canal chInfo y se lleva a cabo la lógica del juego. Si el comando es "send new", se extrae información del canal chInfo y se envía un nuevo jugador al nodo remoto.

La función send se utiliza para enviar mensajes JSON codificados a un nodo remoto a través de una conexión TCP. Primero, establece una conexión con el nodo remoto y luego codifica y envía el mensaje. También se pasa una función f que se ejecuta después de enviar el mensaje.

La función main es el punto de entrada del programa. Lee las banderas de línea de comandos para obtener la configuración del nodo, como el nombre de host, los nodos previo y siguiente, y una bandera especial para iniciar el juego. Si se especifica la bandera especial, el programa envía mensajes "send new" a los nodos previo y siguiente para iniciar el juego. De lo contrario, inicia el servidor TCP llamando a la función listen.

La funcion sendToEndpoint es una solicitud HTTP al endpoint deseado.
