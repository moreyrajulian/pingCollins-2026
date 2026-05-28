# Redes de Computadoras 2026  

## Trabajo Práctico N°4

**Integrantes:**  
- Callovi, Lautaro  
- Galoppo, José María  
- Moreyra, Julián  
- Rivera, Luis Mariano  

**Grupo:** pingCollins  
**Centro educativo:** FCEFyN - UNC  
**Asignatura:** Redes de Computadoras  

**Profesores:**  
- Henn, Santiago M.  
- Oliva Cuneo, Facundo N.  

---

### Información de los autores
- `jose.maria.galoppo@mi.unc.edu.ar` (Galoppo, José María)  
- `luismarianorivera.25@mi.unc.edu.ar` (Rivera, Luis Mariano)  
- `julian.moreyra@mi.unc.edu.ar` (Moreyra, Julián)  
- `lautaro.callovi@mi.unc.edu.ar` (Callovi, Lautaro Nicolás)  

---

## Resumen  

---

## Introducción  

--- 

## Actividad 1  

Cuando escribimos o usamos código de algún lenguaje como puede ser Python, usualmente creamos variables, tenemos objetos, listas o estructuras que viven en nuestra memoria RAM y poseen un formato que solo ese proceso entiende. Esto tal como vive en RAM no se puede enviar a través de la red hacia otro usuario o compañero para que lo utilice, en la red solo podemos transportar bytes planos. Para poder realizar este envió necesitamos **serializar** nuestra información, es decir, convertir estas estructuras de datos en una secuencia de bytes que pueda viajar por la red y así el que lo reciba sea capaz de **deserializarlo** para poder reconstruir la información original. El proceso sería como este:

$[Objeto \ en \ memoria]  →  serializar  →  [bytes]  →  red  →  [bytes]  →  deserializar  →  [Objeto \ en \ memoria]$

A la hora de serializar información nos podemos encontrar con dos tipos:

- **Serialización no binaria:** los datos se convierten a texto legible para humanos y los bytes representan caracteres. Un ejemplo de esto es JSON que justamente usaremos más adelante, otros ejemplos pueden ser XML, CSV, YAML, etc.
- **Serialización binaria:** en este caso los datos se convierten directamente a bits, sin pasar por texto. Un ejemplo de esto es **protobuf** utilizado por Google, otros son MessagePack, BSON, pickle, etc.

Cada una de estas formas tiene sus ventajas y desventajas, a continuación haremos una comparación: 

| Característica | Serialización No Binaria | Serialización Binaria |
|---|---|---|
| **Legibilidad** | Legible por humanos | No legible sin herramientas |
| **Tamaño de datos** | Mayor (representación en caracteres) | Menor (representación compacta) |
| **Velocidad de procesamiento** | Más lento de parsear | Más rápido de serializar/deserializar |
| **Interoperabilidad** | Universal, cualquier lenguaje | Requiere esquema compartido entre emisor y receptor |
| **Facilidad de debugging** | Fácil (se puede leer directamente) | Difícil (requiere herramientas especiales) |
| **Tipos de datos soportados** | Limitados (string, número, bool, array, objeto) | Ricos (fechas, binarios, tipos personalizados) |

---

## Actividad 2  

A continuación desplegaremos un servidor TCP multi-hilo, para ello haremos uso de un script en Python para el servidor y serializaremos nuestro mensaje en formato JSON para que luego sea enviado por medio de PacketSender. La morfología para el mensaje será la siguiente:

![mensaje](/TP4/images/mensaje.png)

Primero ejecutaremos el script del servidor para que se quede escuchando a la espera de un cliente: 

![servidorEscuchando](/TP4/images/serverOn.png)

De mientras configuraremos PacketSender con los siguientes valores y enviamos: 

![configPacketSender](/TP4/images/packetSenderClient.png)

Luego de enviar el paquete confirmamos que el servidor lo recibió correctamente y le dio la bienvenida a nuestra máquina: 

![envioPacket](/TP4/images/envioPacketSender.png)
![servidorEscuchó](/TP4/images/mensajeRecibido.png) 

---

## Actividad 3  

Ahora diseñaremos un cliente propio, lo realizaremos en lenguaje Python y realizará las siguientes acciones:

1. Pedir IP y puerto al usuario
2. Pedir el nombre de grupo
3. Conectarse al servidor
4. Loop:
   → pedir mensaje al usuario
   → armar el JSON
   → enviarlo
   → si escribimos "exit", salimos

El código se encuentra en: `/TP4/src/nuestro_cliente.py`

Ahora veremos como funciona nuestro cliente y corroboramos que lleguen los mensajes en el servidor:

![funcionando](/TP4/images/serverClienteOn.png) 
![servidorNuevo](/TP4/images/servidorNuevo.png) 
![nuestroCliente](/TP4/images/nuestroCliente.png) 

---

## Actividad 4

Para añadir seguridad al sistema de mensajería TCP implementado en los puntos anteriores,
se cifra la **payload** del mensaje antes de enviarlo. El campo `group` viaja en texto plano,
mientras que el contenido del mensaje viaja ilegible para cualquier interceptor.
 
```json
// Mensaje SIN cifrado
{"group": "pingCollins", "payload": "Hola server!"}
 
// Mensaje CON cifrado
{"group": "pingCollins", "payload": "gAAAAABqGKfbkS_UIyebzmzPAuvtBzHFLSzCLl1u...=="}
```

Para ello utilizamos la librería `cryptography` de Python con la encriptación Fernet. Se modificó el código en `nuestro_cliente.py` y se agregó la función `cifrar_payload()` que recibe el texto plano, lo cifra con la clave Fernet y devuelve el token resultante como string.

Ahora veremos como el servidor recibe el campo `group` en texto plano y el payload es un token cifrado ilegible:

![encriptado](/TP4/images/encriptacion.png) 

Analicemos ahora la técnica de cifrado **Fernet:**

- Fernet es un esquema de **cifrado simétrico autenticado** incluido en la librería `cryptography` de Python. No es un algoritmo nuevo, combina algoritmos criptográficos probados para garantizar tanto confidencialidad como integridad del mensaje.

- Todo token Fernet comienza con los caracteres `gAAAAA`, que corresponden al byte de versión `0x80` codificado en Base64. Internamente, el token contiene los siguientes campos:
 
| Campo | Tamaño | Descripción |
|---|---|---|
| Version | 1 byte | Identifica el formato Fernet (siempre `0x80`) |
| Timestamp | 8 bytes | Momento en que se cifró el mensaje (Unix time) |
| IV | 16 bytes | Vector de inicialización aleatorio |
| Ciphertext | Variable | Datos cifrados con AES-128-CBC |
| HMAC | 32 bytes | Firma de autenticación SHA-256 |

Los algortimos que utiliza son:


- **AES-128-CBC**:

AES (Advanced Encryption Standard) es el estándar de cifrado simétrico más utilizado en el mundo. La variante CBC (Cipher Block Chaining) encadena cada bloque cifrado con el anterior, de modo que bloques de entrada idénticos producen bloques de salida distintos. Esto evita patrones reconocibles en el texto cifrado.

- **HMAC-SHA256**:

Además de cifrar, Fernet firma cada token con un código HMAC. Si cualquier byte del token es modificado en tránsito, la verificación falla y el receptor rechaza el mensaje. Esto garantiza integridad y confidencialidad.

- **Base64 URL-safe**:

Los bytes resultantes del cifrado se codifican en Base64 para poder ser transmitidos como texto en el campo JSON, que no admite bytes arbitrarios.

Algunos aspectos claves a tener en cuenta son: 

- **Cifrado simétrico**: 
Se usa la misma clave para cifrar y descifrar. Cliente y servidor deben compartir esta clave
de antemano por un canal seguro.
 
- **IV aleatorio por mensaje**: 
Cada vez que se cifra un mensaje se genera un IV (vector de inicialización) distinto. Esto
garantiza que cifrar el mismo texto dos veces produce tokens completamente distintos, lo que
impide a un atacante detectar mensajes repetidos.
 
- **Cifrado autenticado**:
Fernet combina cifrado e integridad en una sola operación. No es posible modificar el
contenido cifrado sin que el receptor lo detecte.

---  

## Actividad 5

Ahora modificaremos el servidor para que sea capaz de descifrar la payload utilizando la misma clave Fernet que el cliente. El código del servidor se encuentra en `/TP4/src/nuestro_servidor.py`, ahora el mismo ademas de imprimir el payload cifrado muestra el mensaje descifrado. También se agregó una función que detecta si alguién envío un payload que no es un token Fernet válido.

Podemos observar la funcionalidad en la siguiente captura:

![descifradoServer](/TP4/images/descifradoServer.png) 

Entonces gracias a que ambos extremos comparten la misma clave Fernet el token es correctamente descifrado y se vuelve a obtener el texto plano que enviamos, esta sería la implementación real de el esquema que presentamos al inicio del trabajo.

Para corroborar la veracidad del cifrado del payload capturamos el tráfico de los paquetes para ver como viajan a través de la red:

![wireshark](/TP4/images/wireshark.png) 

Podemos observar como el campo `group` viaja de manera legible pero el `payload` lo hace de manera cifrada y sin la clave Fernet es imposible recuperar el mensaje original a partir del token.

---

## Conclusión  