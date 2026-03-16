En un modelo simple y bastante general podemos diferenciar tres capas importantes en las comunicaciones:
* Capa de  **Acceso a la red**
* Capa de **Transporte**
* Capa de **Aplicación**

En respuesta a la **pregunta 2.1** la capa de **Acceso a la Red** tiene como principal función transferir los datos desde el dispositivo hacia la red. 

Esto incluye:
* **Encapsulamiento:** Es responsable de la generación de **tramas** y la preparación de los datos para el nivel físico.
* **Control de acceso:** Gestiona el acceso al medio y define el próximo **destino físico**.
* **Gestión de servicios:** Hace uso de servicios de red avanzados, como la gestión de prioridades de tráfico.

>**Nota:** Aunque normalmente los datos salen hacia un medio físico, existen excepciones como los **Virtual Ethernet (veth)** utilizados en entornos de **Docker**, donde la comunicación es puramente lógica entre interfaces virtuales.     

<br>

La capa de **Transporte** es la encargada de garantizar la fiabilidad en el intercambio de datos entre aplicaciones de extremo a extremo. 

En respuesta a la **pregunta 2.2** sus tareas principales incluyen:
* **Multiplexación:** Permite que múltiples procesos (como el navegador, Spotify o bases de datos) compartan la misma conexión de red de forma simultánea.
* **Segmentación y Reensamblado:** Divide los datos de la capa de aplicación en segmentos manejables y los reconstruye en el destino.
* **Control de Flujo:** Gestiona la velocidad de transmisión para evitar la saturación del receptor.
* **Fiabilidad:** Implementa mecanismos de detección y corrección de errores (siempre que el protocolo utilizado, como TCP, lo requiera).

> **Nota:** El **Puerto** actúa como un **T-SAP** (Transport Service Access Point). Se trata de un identificador de 16 bits definido en la cabecera de transporte que permite direccionar los datos al proceso correcto dentro del host.

<br>

En respuesta a la **pregunta 2.3** un **protocolo** es un conjunto de reglas y convenciones preestablecidas que dictan cómo se debe llevar a cabo el intercambio de datos entre sistemas. Estas reglas aseguran que distintas entidades puedan comunicarse.

<br>

En respuesta a la **pregunta 2.4** la **PDU (Protocol Data Unit)** es la unión de los datos generados en la capa superior junto con la información de control de la capa actual:
* **SDU (Service Data Unit):** Los datos útiles provenientes de la capa superior.
* **PCI (Protocol Control Information):** La cabecera (header) o información de control añadida por la capa actual.
> **Nota:** A este proceso de añadir información de control a los datos de la capa superior se le conoce como **encapsulamiento**.

<br>

En respuesta a la **pregunta 2.5** una **arquitectura de protocolos** es una estructura organizada en capas que combina hardware y software para facilitar el intercambio de datos. 
Sus características principales son:
* **Modularidad:** Cada capa resuelve un problema específico de la comunicación.
* **Independencia:** Los cambios en los protocolos de una capa no afectan necesariamente a las demás.
* **Jerarquía:** Cada nivel hace uso de los servicios proporcionados por la capa inferior y ofrece servicios a la capa superior.

<br>

En respuesta a la **pregunta 2.6** **TCP/IP** es una arquitectura de protocolos estándar para las comunicaciones en red. Financiada por la *Agencia de Proyectos de Investigación Avanzada para la Defensa* (DARPA)
Se organiza comúnmente en cinco capas:
1. **Física**: Interfaz física entre el dispositivo de transmisión de datos
2. **Acceso a la Red:** Responsable del intercambio de datos entre el sistema final y la red a la cual está conectado.
3. **Internet:** Responsable del direccionamiento lógico y el enrutamiento (IP).
4. **Transporte:** Gestión de la comunicación extremo a extremo (TCP/UDP).
5. **Aplicación:** Interfaz con el usuario y procesos finales (HTTP, FTP, DNS).

<br>

En respuesta a la **pregunta 2.7** una arquitectura por capas sigue el principio de *"divide y vencerás"*. Esto trae las siguientes ventajas:
* **Desacoplamiento e Independencia:** Permite separar responsabilidades de modo que los cambios realizados en los protocolos de una capa no afecten a las demás.
* **Estandarización:** Facilita que distintos fabricantes desarrollen hardware y software que sea interoperable bajo reglas comunes.
* **Mantenimiento Simplificado:** Permite depurar errores, actualizar funciones y escalar el sistema de manera aislada y eficiente.

<br>

En respuesta a la **pregunta 2.8** un encaminador es un procesador que conecta dos redes y cuya función principal es retransmitir datos desde una red a otra siguiendo la ruta adecuada para alcanzar al destino.

>**Nota:** A diferencia de un conmutador (switch), que opera dentro de una misma red local, el encaminador actúa en la capa de **Red**, gestionando el tráfico entre redes con diferentes direccionamientos.


