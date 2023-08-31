import sys
from scapy.all import *

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt_pcap_scapy.py <file.pcapng>")
        return

    pcap_file = sys.argv[1]

    packets = rdpcap(pcap_file)
    encrypted_message = ""

    for pkt in packets:
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:  # ICMP Echo Request
            encrypted_message += chr(pkt[ICMP].load[-1])

    print("Encrypted Message:", encrypted_message)

    correct_shift = None

    for shift in range(26):
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        if all(word.isalpha() and (word.islower() or word.isupper()) for word in decrypted_message.split()):
            if correct_shift is None:
                correct_shift = shift
                print(f"Shift {shift:02d}: ", end='')
                print_colored(decrypted_message, '32')  # '32' corresponds to green color code
                print()
            else:
                print(f"Shift {shift:02d}: {decrypted_message}")
        else:
            print(f"Shift {shift:02d}: {decrypted_message}")

if __name__ == "__main__":
    main()
