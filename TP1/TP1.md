# Redes de Computadoras 2026

## Trabajo práctico N°1 - Simulación de envío de paquetes, ARP y ruteo entre redes.

## Resumen

En este trabajo práctico se desarrolló de manera "física y manual" el transporte de paquetes en una red WAN con el propósito de comprender conceptualmente su funcionamiento.
---
## Introducción

En la primera parte del laboratorio, nos dividimos en grupos que cumplieron la función de nodos, siendo tres grupos los nodos intermedios que funcionaron como routers. Cada grupo contaba con dirección IP, dirección MAC, máscara de subred y puerta de enlace predeterminada.

En la segunda parte, se realizaron técnicas de detección de errores mediante EDAC (Error Detection And Correction).

---
# Desarrollo
## Actividad 1

En este caso, nuestro grupo (PingCollins) cumplió la función de router.

### Configuración NIC - Router Ping Collins

**Datos del dispositivo:**
- Nombre: Router Ping Collins
- Dirección IP: 10.3.0.1
- Dirección MAC: AC:45:92
- Máscara de subred: 255.255.255.0 (/24)
- Gateway por defecto: N/A

## Actividad 2

**Interfaces:**
- eth0: 10.3.0.1 (subred 10.3.0.0/24, hacia nodos)
- eth1: 10.11.0.1 (subred 10.11.0.0/24, hacia router AC:45:10)
- eth2: 10.16.0.1 (subred 10.16.0.0/24, hacia router AC:45:10)
- eth3: 10.5.0.1 (subred 10.5.0.0/24, hacia router AC:45:10)

**Tabla de ruteo:**

| Destino      | Máscara          | Gateway    | Interfaz |
|--------------|------------------|------------|----------|
| 10.3.0.0     | 255.255.255.0    | Directa    | eth0     |
| 10.11.0.0    | 255.255.255.0    | Directa    | eth1     |
| 10.16.0.0    | 255.255.255.0    | Directa    | eth2     |
| 10.5.0.0     | 255.255.255.0    | Directa    | eth3     |
| 10.10.0.0    | 255.255.255.0    | 10.5.0.X   | eth3     |
| 10.6.0.0     | 255.255.255.0    | 10.5.0.X   | eth3     |
| 10.12.0.0    | 255.255.255.0    | 10.5.0.X   | eth3     |
| 10.13.0.0    | 255.255.255.0    | 10.5.0.X   | eth3     | 

## Actividad 3

En este punto recibimos distintos payloads provenientes de otros routers o el gateway conectado a nosotros. La tarea era detectar a donde habia que enviarlo (otro router o al gateway por defecto), cambiar direccion de origen y destino, y reducir el TTL.

![alt text](image.png)

## Actividad 4

En nuestro caso, al ser routers, nos encargabamos de desempaquetar y empaquetar los frames, en medio del caos de la experiencia, tuvimos dificultades reenviandolos, haciendo que nos queden varios a "medio camino"

## Actividad 5


### a) Cambio de dirección MAC en cada salto

Esto es debido a que existe una clara diferencia entre direccionamiento lógico (IP) y direccionamiento físico (MAC):

- **Dirección IP (Nivel 3 - Red):** Identifica de forma única la máquina de destino final en todo el camino. La IP destino permanece igual durante todo el viaje del paquete porque indica el destino último.

- **Dirección MAC (Nivel 2 - Enlace):** Sirve solo para alcanzar el siguiente salto en la red. Cada router o dispositivo que recibe el paquete cambia la MAC destino por la del siguiente dispositivo en la cadena (calculada mediante ARP).

Esta separación permite que los routers intermedios no necesiten conocer la topología completa de la red; solo necesitan saber cómo llegar al siguiente router basándose en la dirección IP destino.

### b) Uso del gateway por defecto

Cuando un host quiere enviar un paquete a un dispositivo en otra red, no intenta descubrir directamente la MAC del host destino, sino la del default gateway. Esto es así por varias razones:

- **Escalabilidad:** El host no necesita conocer las MACs de todos los dispositivos en redes remotas, solo la de su gateway.

- **Abstracción de redes distantes:** El host confía en que el gateway sabrá cómo alcanzar la red destino. Este es el propósito del gateway.

- **Simplicidad:** Si cada host intentara descubrir MACs remotas, necesitaría ejecutar ARP en redes donde no tiene acceso directo, lo cual es ineficiente e imposible en muchos casos.

El gateway resuelve el problema de que el host no puede comunicarse directamente con redes lejanas, actuando como intermediario y responsable de conocer el camino hacia ellas.

### c) Modelo de ruteo hop-by-hop

Cada router toma decisiones basándose únicamente en su tabla de ruteo local y no en el camino completo hacia el destino. Las ventajas de este modelo son:

- **Descentralización:** No requiere que cada router conozca la topología completa de Internet.

- **Escalabilidad:** Internet puede crecer sin necesidad de actualizar todas las tablas en todos los routers simultáneamente.

- **Flexibilidad:** Los cambios de rutas o topología se adaptan localmente sin afectar toda la red.

- **Resistencia:** Si una ruta falla, cada router puede redirigir tráfico através de alternativas sin necesidad de coordinación global mediante cálculos previos del camino completo.

- **Eficiencia:** El procesamiento se distribuye entre routers, permitiendo que cada uno maneje decisiones locales rápidamente.

### d) Desencapsulación y reencapsulación en cada enlace

En el laboratorio observamos que los routers desencapsulan y vuelven a encapsular el paquete en cada enlaces. Esto es necesario porque:

- **Cambio de dirección MAC:** La dirección MAC destino debe cambiar para cada enlace, por lo que es necesario reconstruir el frame con la nueva MAC.

- **Recalculación de CRC/FCS:** Cada frame tiene su propio checksum (Cyclic Redundancy Check o Frame Check Sequence) para detectar errores en ese enlace específico. Al cambiar el contenido del frame (especialmente la MAC destino), el checksum debe recalcularse.

- **TTL decremento:** El campo TTL en la cabecera IP debe decrementarse, lo que requiere recalcular la suma de comprobación de IP.

- **Cambios de interfaz:** Cada interfaz de salida puede tener características específicas (velocidad, MTU, etc.) que pueden requerir ajustes en la encapsulación.

Simplemente reenviar el frame sin cambios causaría que el checksum fuera incorrecto y el dispositivo destino descartaría el paquete como corrupto.

### e) Significado del campo TTL

El campo TTL (Time To Live) se decrementa en cada router. Este mecanismo previene el problema de **bucles en la red**:

- **Problema prevenido:** Si un paquete entra en un ciclo de ruteo (por ejemplo, Router A → Router B → Router A), sin TTL circularía infinitamente, consumiendo ancho de banda indefinidamente.

- **Mecanismo de protección:** Cada router decrementa el TTL en 1. Cuando TTL llega a 0, el router descarta el paquete y envía un mensaje ICMP "Time Exceeded" al origen.

- **Impacto sin TTL:** Sin este mecanismo, los paquetes circulando en bucles nunca serían descartados, saturando la red y consumiendo recursos indefinidamente. Esto es especialmente crítico en redes grandes como Internet donde los errores de configuración de ruteo son inevitables.

El TTL típicamente comienza en 64 o 128, permitiendo que un paquete legitimo atraviese múltiples saltos (generalmente decenas) mientras previene que paquetes "perdidos" afecten la red permanentemente.