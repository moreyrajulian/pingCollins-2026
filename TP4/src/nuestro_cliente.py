import socket
import json
from cryptography.fernet import Fernet

# hardcodeo a proposito
CLAVE = b'ZmDfcTF7_60GrrY167zsiPd81PgrADa740dm34NSK-s='

def cifrar_payload(texto):
    f = Fernet(CLAVE)
    return f.encrypt(texto.encode("utf-8")).decode("utf-8")

def main():
    # 1. Configuración
    host  = input("IP del servidor: ")
    port  = int(input("Puerto: "))
    group = input("Nombre de tu grupo: ")

    # 2. Conexión
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"\n✓ Conectado a {host}:{port}\n")

    # 3. Loop de mensajes
    try:
        while True:
            payload = input("Mensaje ('exit' para salir): ")

            if payload.lower() == "exit":
                break

            # Solo la payload se cifra, el group viaja en claro
            payload_cifrada = cifrar_payload(payload)

            message = {
                "group": group,
                "payload": payload_cifrada
            }

            client.sendall(json.dumps(message).encode("utf-8"))
            print(f"↑ Payload enviada cifrada: {payload_cifrada[:40]}...\n")

    except KeyboardInterrupt:
        print("\nDesconectando...")

    finally:
        client.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()