import os

class LocalSettings:

    Win_User_Path = os.path.join(os.environ['USERPROFILE'])

    #Path to save the encrypted file. File extension can be anything you want, withing reason of couse
    Enc_File_Path = "C:\\My_Folder\\My_File.sef"

    #Path to retrieve the actual file you want to encrypt.
    Dec_File_Path = "C:\\My_Folder\\My_File.txt"

    #Path to your private key. Not the safest, but we only want to keep some info from those pesky kids.
    Internal_Data_Folder = "File_Encrypt_PY"
    Internal_Data_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder)
    Key_Name = "JD_Enc.usk"
    Key_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder + "\\" + Key_Name)