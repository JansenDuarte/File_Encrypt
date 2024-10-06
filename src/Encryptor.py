import os
from cryptography.fernet import Fernet
from LocalSettings import LocalSettings

class Encryptor:

    key = ''

    def __init__(self):
        self.__Find_Key()
        

    def __Find_Key(self):
        if not os.path.exists(LocalSettings.Internal_Data_Path):
            try:
                os.makedirs(LocalSettings.Internal_Data_Path)
            except OSError:
                pass

        try :
            key_file = open(LocalSettings.Key_Path, 'rb')
            self.key = key_file.read()
        except OSError as _e:
            self.__Create_New_Key()


    def __Create_New_Key(self):
        print('\nGenerating new key...')
        self.key = Fernet.generate_key()
        with open(LocalSettings.Key_Path, 'wb') as key_file:
            key_file.write(self.key)
            key_file.close()
        print('\nKey Saved! Continuing')



    def Encrypt_File(self):
        print('\nEncrypting...')

        try:
            with open(LocalSettings.Dec_File_Path, 'r+') as dec_file:
                data = dec_file.read()
                fernet = Fernet(self.key)
                encoded_data = fernet.encrypt(data.encode())

                dec_file.close()
                os.remove(LocalSettings.Dec_File_Path)

                with open(LocalSettings.Enc_File_Path, 'w+') as enc_file:
                    enc_file.write(encoded_data.decode())

                enc_file.close()

                print('\nEncrypted file place in folder: ' + LocalSettings.Enc_File_Path + '\n')
                
        except OSError:
            print('\nNo file found in the path set in \'LocalSetting.py\'')