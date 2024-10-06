import sys
from Encryptor import Encryptor
from Decryptor import Decryptor






arguments = sys.argv

if ('-e' or '-E' or '--encrypt' or '--Encrypt') in arguments:
    
    enc = Encryptor()
    enc.Encrypt_File()

elif ('-d' or '-D' or '--decrypt' or '--Decrypt') in arguments:
    
    dec = Decryptor()
    dec.Decrypt_File()


else:
    print("""
    Option not present or not supported.
    
    Use <-e>', <-E>', <--encrypt>', <--Encrypt>' for encrypting a file.

    Use <-d>', <-D>', <--decrypt>', <--Decrypt>' fro decrypting a file.
       """)

    exit(0) #exited normaly