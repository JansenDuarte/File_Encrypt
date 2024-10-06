import os
from cryptography.fernet import Fernet
from LocalSettings import LocalSettings

class Decryptor:

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
            with open(LocalSettings.Key_Path) as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            print("""
                Private key not configured.

                Run with option <-e> to encrypt a file and generate a private key.
                
                Aborting...\n""")
            exit(0) #exited normaly



    def Decrypt_File(self):
        print('\nDecrypting...')

        try:
            with open(LocalSettings.Enc_File_Path, 'r') as file:
                data = file.read()
                fernet = Fernet(self.key)
                decoded_data = fernet.decrypt(data.encode())

        except OSError:
            print('\nEncrypted file not found. Try executing with option <-e> to encrypt the file.')
            exit(-2)

        file.close()

        with open(LocalSettings.Dec_File_Path, 'w+') as destination:
            destination.write(decoded_data.decode())

        destination.close()

        print('\nDecrypted file place in folder: ' + LocalSettings.Dec_File_Path + '\n')
        os.startfile(LocalSettings.Dec_File_Path)