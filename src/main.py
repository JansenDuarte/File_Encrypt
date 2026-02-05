import sys
from exit_codes import *
from LocalSettings import LocalSettings as sett
from Encryptor import Encryptor
from Decryptor import Decryptor






arguments = sys.argv

if ('-e' or '-E' or '--encrypt' or '--Encrypt') in arguments:
    
    enc = Encryptor()
    enc.encrypt_file()

elif ('-d' or '-D' or '--decrypt' or '--Decrypt') in arguments:
    
    dec = Decryptor()
    dec.decrypt_file()


else:
    print("""
    Option not present or not supported.
    
    Use '-e', '-E', '--encrypt', '--Encrypt' for encrypting a file.

    Use '-d', '-D', '--decrypt', '--Decrypt' for decrypting a file.
       """)

    exit(EXT_CODE_NORMAL)
