## TP3

1) 
a) ¿Que es SSH y que problema resuelve?
SSH (Secure Shell) es un protocolo de red que permite establecer una comunicación segura y cifrada entre dos hosts a través de una red. Utiliza un sistema de autenticación basado en pares de claves (clave pública y privada) y, por defecto, funciona sobre el puerto 22.
El problema que resuelve es la transmisión insegura de datos, ya que protege la información contra accesos no autorizados y ataques como la interceptación de datos durante la comunicación.

b) Diferencia entre autenticacion y cifrado
La autenticación es el proceso de verificar la identidad de un usuario o sistema, es decir, comprobar que quien intenta acceder es realmente quien dice ser (identidad).
El cifrado consiste en aplicar un algoritmo que transforma el contenido de un mensaje en un formato ilegible, con el objetivo de ocultar la información y evitar que pueda ser leída por personas no autorizadas (confidencialidad).

c) ¿Qué es una clave pública y una clave privada?
Una clave pública y una clave privada forman un par de claves utilizadas en criptografía. Se pueden entender mediante una analogía entre una cerradura y una llave: la clave pública sería como una cerradura que puede tener cualquiera, mientras que la clave privada sería la llave que solo posee la persona responsable.
Este par de claves está asociado a algoritmos de cifrado y descifrado, que permiten proteger la información y garantizar que solo quien tenga la clave privada pueda acceder a los datos cifrados.

d) ¿Por qué la clave privada no debe compartirse?   
La clave privada no debe compartirse porque es el elemento que permite demostrar la identidad del propietario y descifrar la información protegida. Si otra persona obtiene la clave privada, podría hacerse pasar por el dueño legítimo, acceder a sistemas protegidos o descifrar mensajes confidenciales.

e) ¿Qué ventajas tienen las claves SSH frente a contraseñas?
Son más seguras porque utilizan criptografía, lo que hace muy difícil que puedan ser adivinadas o descifradas mediante ataques de fuerza bruta.
Además, permiten autenticarse sin necesidad de escribir una contraseña cada vez, lo que facilita la automatización de tareas y reduce el riesgo de errores humanos. También son menos vulnerables a ataques como el robo de contraseñas o la reutilización de claves débiles en distintos sistemas.

2) Verificar conexión ssh
![DirectorioEnHome](Imagenes/Prueba.png)

6) Relacionar el problema que aborda el video con los TPs 1), 2) y 3). ¿Qué cosas que hemos aprendido se aplican directamente al problema demostrado?
El video muestra un ataque de retransmisión en pagos NFC, lo que se relaciona con los conceptos vistos en los TP1, TP2 y TP3.

En el TP1 se estudiaron los mecanismos de envío de paquetes entre dispositivos, encapsulación y comunicación entre nodos, lo que se relaciona con el ataque mostrado, ya que el atacante actúa como intermediario retransmitiendo la información entre el teléfono y el terminal de pago.

En el TP2 se trabajó con la capa física, lo cual se relaciona con el uso de tecnología NFC en el ataque, ya que depende de la comunicación inalámbrica de corto alcance entre dispositivos.

En el TP3 se trabajó con acceso remoto mediante SSH y se analizaron comunicaciones cifradas, lo que se relaciona directamente con el video, ya que demuestra que aunque los datos estén cifrados, es posible retransmitirlos sin descifrarlos, permitiendo realizar ataques sin conocer el contenido de la comunicación

b) ¿Qué cosas deberíamos tener en cuenta dado el principio de confidencialidad en las redes de
computadoras y los resultados obtenidos en este laboratorio?
Según el principio de confidencialidad, la información debe ser accesible solo para usuarios autorizados. El video demuestra que el cifrado por sí solo no garantiza la confidencialidad si no se valida correctamente la identidad y el contexto de la comunicación.

Los resultados obtenidos en el laboratorio muestran que el tráfico cifrado protege el contenido de los datos, pero no impide que puedan ser interceptados o retransmitidos. Por lo tanto, además del cifrado, es importante implementar mecanismos de autenticación y control del acceso físico para proteger adecuadamente la información.