En un modelo simple y bastante general podemos diferenciar tres capas importantes en las comunicaciones:
* Capa de  **Acceso a la red**
* Capa de **Transporte**
* Capa de **Aplicación**

En respuesta a la **pregunta 1.1** la capa de **Acceso a la Red** tiene como principal función transferir los datos desde el dispositivo hacia la red. 

Esto incluye:
* **Encapsulamiento:** Es responsable de la generación de **tramas** y la preparación de los datos para el nivel físico.
* **Control de acceso:** Gestiona el acceso al medio y define el próximo **destino físico**.
* **Gestión de servicios:** Hace uso de servicios de red avanzados, como la gestión de prioridades de tráfico.

>**Nota:** Aunque normalmente los datos salen hacia un medio físico, existen excepciones como los **Virtual Ethernet (veth)** utilizados en entornos de **Docker**, donde la comunicación es puramente lógica entre interfaces virtuales.     

<br>

La capa de **Transporte** es la encargada de garantizar la fiabilidad en el intercambio de datos entre aplicaciones de extremo a extremo. 

En respuesta a la **pregunta 1.2** sus tareas principales incluyen:
* **Multiplexación:** Permite que múltiples procesos (como el navegador, Spotify o bases de datos) compartan la misma conexión de red de forma simultánea.
* **Segmentación y Reensamblado:** Divide los datos de la capa de aplicación en segmentos manejables y los reconstruye en el destino.
* **Control de Flujo:** Gestiona la velocidad de transmisión para evitar la saturación del receptor.
* **Fiabilidad:** Implementa mecanismos de detección y corrección de errores (siempre que el protocolo utilizado, como TCP, lo requiera).

> **Nota:** El **Puerto** actúa como un **T-SAP** (Transport Service Access Point). Se trata de un identificador de 16 bits definido en la cabecera de transporte que permite direccionar los datos al proceso correcto dentro del host.

<br>

En respuesta a la **pregunta 1.3** un **protocolo** es un conjunto de reglas y convenciones preestablecidas que dictan cómo se debe llevar a cabo el intercambio de datos entre sistemas. Estas reglas aseguran que distintas entidades puedan comunicarse.

<br>

En respuesta a la **pregunta 1.4** la **PDU (Protocol Data Unit)** es la unión de los datos generados en la capa superior junto con la información de control de la capa actual:
* **SDU (Service Data Unit):** Los datos útiles provenientes de la capa superior.
* **PCI (Protocol Control Information):** La cabecera (header) o información de control añadida por la capa actual.
> **Nota:** A este proceso de añadir información de control a los datos de la capa superior se le conoce como **encapsulamiento**.

<br>

En respuesta a la **pregunta 1.5** una **arquitectura de protocolos** es una estructura organizada en capas que combina hardware y software para facilitar el intercambio de datos. 
Sus características principales son:
* **Modularidad:** Cada capa resuelve un problema específico de la comunicación.
* **Independencia:** Los cambios en los protocolos de una capa no afectan necesariamente a las demás.
* **Jerarquía:** Cada nivel hace uso de los servicios proporcionados por la capa inferior y ofrece servicios a la capa superior.

<br>

En respuesta a la **pregunta 1.6** **TCP/IP** es una arquitectura de protocolos estándar para las comunicaciones en red. Financiada por la *Agencia de Proyectos de Investigación Avanzada para la Defensa* (DARPA)
Se organiza comúnmente en cinco capas:
1. **Física**: Interfaz física entre el dispositivo de transmisión de datos
2. **Acceso a la Red:** Responsable del intercambio de datos entre el sistema final y la red a la cual está conectado.
3. **Internet:** Responsable del direccionamiento lógico y el enrutamiento (IP).
4. **Transporte:** Gestión de la comunicación extremo a extremo (TCP/UDP).
5. **Aplicación:** Interfaz con el usuario y procesos finales (HTTP, FTP, DNS).

<br>

En respuesta a la **pregunta 1.7** una arquitectura por capas sigue el principio de *"divide y vencerás"*. Esto trae las siguientes ventajas:
* **Desacoplamiento e Independencia:** Permite separar responsabilidades de modo que los cambios realizados en los protocolos de una capa no afecten a las demás.
* **Estandarización:** Facilita que distintos fabricantes desarrollen hardware y software que sea interoperable bajo reglas comunes.
* **Mantenimiento Simplificado:** Permite depurar errores, actualizar funciones y escalar el sistema de manera aislada y eficiente.

<br>

En respuesta a la **pregunta 1.8** un encaminador es un procesador que conecta dos redes y cuya función principal es retransmitir datos desde una red a otra siguiendo la ruta adecuada para alcanzar al destino.

>**Nota:** A diferencia de un conmutador (switch), que opera dentro de una misma red local, el encaminador actúa en la capa de **Red**, gestionando el tráfico entre redes con diferentes direccionamientos.


# Resolución de Ejercicios (Capítulo 2)

## Ejercicio 2.1

**Procedimiento de pedir la pizza (Arquitectura superior):**
* **Nivel 3 (Invitado/Cocinero):** El Invitado (la aplicación que genera los datos) decide qué quiere comer y le pasa su necesidad al Anfitrión. Del otro lado, el Cocinero recibe el pedido final y prepara la pizza.
* **Nivel 2 (Anfitrión/Encargado):** El Anfitrión toma la necesidad del invitado y establece la comunicación llamando por teléfono. El Encargado de pedidos atiende la llamada, anota la orden y se la pasa al nivel superior (el cocinero).
* **Nivel 1 (Teléfono):** Convierte las palabras en señales electromagnéticas y las transmite por el medio físico (la línea telefónica).

**Procedimiento de enviar la pizza (Arquitectura inferior):**
* **Nivel 3 (Invitado/Cocinero):** El Cocinero entrega el producto terminado (datos) a la capa inferior. Al final, el Invitado recibe la pizza y la consume.
* **Nivel 2 (Anfitrión/Encargado):** El Encargado toma la caja y se la entrega a la Furgoneta para su transporte. Del otro lado, el Anfitrión recibe la caja de la furgoneta y se la da al Invitado.
* **Nivel 1 (Furgoneta):** Es el medio de transporte (capa física) que viaja por la Carretera (el medio) llevando el paquete desde el origen al destino.

<br>

## Ejercicio 2.2

**a) Intermediario simple**
Aquí hay tres niveles:
1. **Nivel 3:** Primer Ministro (crea el mensaje).
2. **Nivel 2:** Traductor al inglés (traduce el mensaje original a un "formato" común).
3. **Nivel 1:** Teléfono (transmite la señal acústica). 

*Interacción:* El PM Chino habla en su idioma. El traductor lo pasa a inglés y lo habla por teléfono. El teléfono transmite las señales. En Francia, el traductor francés lo escucha en inglés, lo traduce al francés y se lo dice a su PM.

**b) Nodo intermedio**
Esta situación ilustra un "nodo intermedio" (funcionando de forma análoga a un router en una red).
* **Lado China:** PM (Chino) $\rightarrow$ Traductor (Japonés) $\rightarrow$ Teléfono.
* **Nodo Alemania (Intermedio):** Teléfono $\rightarrow$ Traductor (recibe en Japonés, traduce al Alemán) $\rightarrow$ Teléfono.
* **Lado Francia:** Teléfono $\rightarrow$ Traductor (recibe en Alemán, traduce al Francés) $\rightarrow$ PM (Francés).

<br>

## Ejercicio 2.3

Las desventajas del diseño en capas incluyen: 
1. **Sobrecarga de datos (Overhead):** Cada capa añade su propia información de control (cabeceras), lo que hace que el mensaje total sea más pesado.
2. **Duplicación de esfuerzos:** Algunas funciones, como el control de errores o el direccionamiento, a veces se realizan de forma redundante en más de una capa.
3. **Procesamiento adicional:** Empaquetar y desempaquetar la información en cada capa toma tiempo de procesamiento y memoria en los equipos, lo que puede añadir latencia.

<br>

## Ejercicio 2.4

**No, no existe tal protocolo.** Este es un problema clásico en informática conocido como el "Problema de los Dos Generales". Como el sistema de comunicación es inherentemente no fiable (el soldado puede ser interceptado), ninguna de las partes puede estar jamás 100% segura de que el último mensaje de confirmación haya llegado. Si el General A envía una confirmación, no atacará hasta estar seguro de que B la recibió. Si B envía una confirmación de la confirmación, B no atacará hasta saber que A la recibió, creando un bucle infinito de incertidumbre.

<br>

## Ejercicio 2.5

En una red de difusión pura (donde el medio es un único cable o el aire y el mensaje le llega físicamente a todos), la función de "encaminamiento" o búsqueda de rutas (que es el trabajo principal de la capa de red) **no es estrictamente necesaria**. Todos los nodos reciben la transmisión, por lo que basta con la capa de Enlace de Datos (capa 2) y sus direcciones físicas (MAC) para que cada computadora decida si el mensaje era para ella o si debe ignorarlo. Solo se necesita la capa de Red si se quiere salir de esa LAN hacia otra red distinta (como Internet).

<br>

## Ejercicio 2.7

* **a) Segmentación:** **No es necesario**. La cabecera original del nivel $N$ no se copia en cada segmento. La cabecera de $N$ junto con sus datos se tratan como un gran bloque de información que simplemente se "corta" en pedazos. El nivel inferior ($N-1$) le agregará su propia cabecera a cada uno de esos pedazos para poder rearmarlos en el destino.
* **b) Agrupamiento:** **Sí, es necesario**. Cada una de las pequeñas PDUs del nivel $N$ que se van a meter dentro de un único paquete grande de nivel $N-1$ debe conservar su propia cabecera original. Si no la conservan, el nivel $N$ de la computadora receptora no tendría forma de saber a qué aplicación o proceso le corresponde cada bloque de información.