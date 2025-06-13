import os
from cryptography.fernet import Fernet

import LocalSettings
from LocalSettings import LocalSettings as settings

class Decryptor:

    key = ''

    def __init__(self):
        self.__Find_Key()
        

    def __Find_Key(self):
        if not os.path.exists(settings.Internal_Data_Path):
            try:
                os.makedirs(settings.Internal_Data_Path)
            except OSError:
                pass

        try :
            with open(settings.Key_Path) as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            print("""
                Private key not configured.

                Run with option <-e> to encrypt a file and generate a private key.
                
                Aborting...\n""")
            exit(LocalSettings.EXT_CODE_NORMAL)



    def Decrypt_File(self):
        print('\nDecrypting...')

        try:
            with open(settings.Enc_File_Path, 'r', encoding=settings.Sys_Encoding) as enc_file:
                data = enc_file.read()
                fernet = Fernet(self.key)
                decoded_data = fernet.decrypt(data.encode(encoding=settings.Sys_Encoding))

        except OSError:
            print('\nEncrypted file not found. Try executing with option <-e> to encrypt the file.')
            exit(LocalSettings.EXT_CODE_NON_EXISTING_FILE)
        except UnicodeDecodeError as de:
            print(f'Decoding error!\nDetails:\n\tError: {de.reason}\n\tChar. position: {de.start}')
            exit(LocalSettings.EXT_CODE_ENCODING_ERROR)

        enc_file.close()

        with open(settings.Dec_File_Path, 'w+') as dec_file:
            dec_file.write(decoded_data.decode(encoding=settings.Sys_Encoding))

        dec_file.close()

        print('\nDecrypted file placed in path: ' + settings.Dec_File_Path + '\n')

        try:
            os.startfile(settings.Dec_File_Path)
        except NotImplementedError as nie:
            print(f'\nWindows error!\nCould not open decrypted file')
            exit(LocalSettings.EXT_CODE_WINDOWS_ERROR)