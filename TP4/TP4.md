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

---

## Actividad 4

---  

## Actividad 5

---

## Actividad 6  

---

## Conclusión  
