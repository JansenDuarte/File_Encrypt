import os
import subprocess
from exit_codes import *
from cryptography.fernet import Fernet
from settings import Settings as sett

class Decryptor:

    key = ''

    def __init__(self):
        self.__find_key()
        

    def __find_key(self):
        if not os.path.exists(sett.Internal_Data_Path):
            try:
                os.makedirs(sett.Internal_Data_Path)
            except OSError:
                pass

        try :
            with open(sett.Key_Path) as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            if sett.VERBOSE_MODE:
                print("""
                    Private key not configured.

                    Run with option <-e> to encrypt a file and generate a private key.
                    
                    Aborting...\n""")
            exit(EXT_CODE_NORMAL)



    def decrypt_file(self):
        if sett.VERBOSE_MODE:
            print('\nDecrypting...')

        try:
            with open(sett.Enc_File_Path, 'r', encoding=sett.Sys_Encoding) as enc_file:
                data = enc_file.read()
                fernet = Fernet(self.key)
                decrypted_data = fernet.decrypt(data.encode(encoding=sett.Sys_Encoding))
        except OSError:
            if  sett.VERBOSE_MODE:
                print('\nEncrypted file not found. Try executing with option <-e> to encrypt the file.')
            exit(EXT_CODE_NON_EXISTING_FILE)
        except UnicodeDecodeError as de:
            if sett.VERBOSE_MODE:
                print(f'Decoding error!\nDetails:\n\tError: {de.reason}\n\tChar. position: {de.start}')
            exit(EXT_CODE_ENCODING_ERROR)

        with open(sett.Dec_File_Path, 'w+') as dec_file:
            dec_file.write(decrypted_data.decode(encoding=sett.Sys_Encoding))

        if sett.VERBOSE_MODE:
            print('\nDecrypted file placed in path: ' + sett.Dec_File_Path + '\n')

        if (sett.CURRENT_SYSTEM == 'posix'):
            try:
                subprocess.call(['nvim', sett.Dec_File_Path])
            except Exception as e:

                if sett.VERBOSE_MODE:
                    print(f"Something big went wrong!")
                exit(EXT_CODE_POSIX_ERROR)
        else:
            try:
                os.startfile(sett.Dec_File_Path)
            except NotImplementedError as nie:
                if sett.VERBOSE_MODE:
                    print(f'\nWindows error!\nCould not open decrypted file')
                exit(EXT_CODE_WINDOWS_ERROR)
