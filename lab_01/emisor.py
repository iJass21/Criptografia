import sys
from scapy.all import *

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                ascii_inicio = ord('A')
            else:
                ascii_inicio = ord('a')
            
            ascii_original = ord(caracter)
            ascii_cifrado = (ascii_original - ascii_inicio + corrimiento) % 26 + ascii_inicio
            caracter_cifrado = chr(ascii_cifrado)
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter
    
    return texto_cifrado

if len(sys.argv) != 3:
    print("Uso: python programa.py <texto> <corrimiento>")
    sys.exit(1)

texto_original = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_original, corrimiento)

id_identificador = 1234  # Valor del identificador (puede ser cualquier valor)
contenido_ping = b'\x08\x00\xf7\xff'  # Contenido clásico de un ping (8 bytes)
seq_number_be = 1  # Número de secuencia BE inicial
seq_number_le = 256  # Número de secuencia LE inicial

for caracter in texto_cifrado:
    padding = bytes([i for i in range(0x10, 0x38)])[:(42 - len(caracter))]  # Relleno con valores hexadecimales
    extra_bytes = b'\xf0\x12\xd5'  # 2 bytes adicionales
    icmp_payload = contenido_ping + padding + extra_bytes + caracter.encode()  # Concatenar contenido del ping, relleno, bytes extras y caracter cifrado
    pkt_be = IP(dst="8.8.8.8") / ICMP(type=8, code=0, id=id_identificador, seq=seq_number_be) / Raw(load=icmp_payload)
    #pkt_le = IP(dst="8.8.8.8") / ICMP(type=8, code=0, id=id_identificador, seq=seq_number_le) / Raw(load=icmp_payload)
    send(pkt_be)
    #send(pkt_le)
    print(f"Enviado BE - Seq: {seq_number_be}, Caracter: {caracter}")
   # print(f"Enviado LE - Seq: {seq_number_le}, Caracter: {caracter}")
    seq_number_be += 1
    seq_number_le += 256
