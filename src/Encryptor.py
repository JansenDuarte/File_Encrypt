import os
from cryptography.fernet import Fernet

import LocalSettings
from LocalSettings import LocalSettings as settings

class Encryptor:

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
            key_file = open(settings.Key_Path, 'rb')
            self.key = key_file.read()
        except OSError as _e:
            self.__Create_New_Key()


    def __Create_New_Key(self):
        print('\nGenerating new key...')
        self.key = Fernet.generate_key()
        with open(settings.Key_Path, 'wb') as key_file:
            key_file.write(self.key)
            key_file.close()
        print('\nKey Saved! Continuing')



    def Encrypt_File(self):
        print('\nEncrypting...')

        try:
            with open(settings.Dec_File_Path, 'r+', encoding=settings.Sys_Encoding) as dec_file:
                data = dec_file.read()
                fernet = Fernet(self.key)
                encoded_data = fernet.encrypt(data.encode(encoding=settings.Sys_Encoding))

                dec_file.close()
                os.remove(settings.Dec_File_Path)

                with open(settings.Enc_File_Path, 'w+') as enc_file:
                    enc_file.write(encoded_data.decode(encoding=settings.Sys_Encoding))

                enc_file.close()

                print('\nEncrypted file place in path: ' + settings.Enc_File_Path + '\n')
                
        except OSError:
            print('\nNo file found in the path set in \'LocalSetting.py\'')
            exit(LocalSettings.EXT_CODE_NON_EXISTING_FILE)
        except UnicodeDecodeError as de:
            print(f'Decoding error!\nDetails:\n\tError: {de.reason}\n\tChar. position: {de.start}')
            exit(LocalSettings.EXT_CODE_ENCODING_ERROR)