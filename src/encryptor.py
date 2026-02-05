import os
from exit_codes import *
from cryptography.fernet import Fernet
from settings import Settings as sett

class Encryptor:

    key = ''

    def __init__(self):
        self.__Find_Key()
        

    def __Find_Key(self):
        if not os.path.exists(sett.Internal_Data_Path):
            try:
                os.makedirs(sett.Internal_Data_Path)
            except OSError:
                pass

        try :
            with open(sett.Key_Path, 'rb') as key_file:
                self.key = key_file.read()
        except OSError as _e:
            self.__Create_New_Key()


    def __Create_New_Key(self):
        print('\nGenerating new key...')
        self.key = Fernet.generate_key()
        with open(sett.Key_Path, 'wb') as key_file:
            key_file.write(self.key)
        print('\nKey Saved! Continuing')



    def encrypt_file(self):
        print('\nEncrypting...')

        try:
            with open(sett.Dec_File_Path, 'r+', encoding=sett.Sys_Encoding) as dec_file:
                data = dec_file.read()
                fernet = Fernet(self.key)
                encrypted_data = fernet.encrypt(data.encode(encoding=sett.Sys_Encoding))

                dec_file.close()
                os.remove(sett.Dec_File_Path)

                with open(sett.Enc_File_Path, 'w+') as enc_file:
                    enc_file.write(encrypted_data.decode(encoding=sett.Sys_Encoding))

                enc_file.close()

                print('\nEncrypted file place in path: ' + sett.Enc_File_Path + '\n')
                
        except OSError:
            print('\nNo file found in the path set in \'LocalSetting.py\'')
            exit(EXT_CODE_NON_EXISTING_FILE)
        except UnicodeDecodeError as de:
            print(f'Decoding error!\nDetails:\n\tError: {de.reason}\n\tChar. position: {de.start}')
            exit(EXT_CODE_ENCODING_ERROR)
