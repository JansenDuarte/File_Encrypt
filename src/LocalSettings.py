import os

class LocalSettings:

    Win_User_Path = os.path.join(os.environ['USERPROFILE'])

    Enc_File_Path = "C:\\Jansen-PastaDados\\Important Info.sef"
    Dec_File_Path = "C:\\Jansen-PastaDados\\Important Info.txt"

    Internal_Data_Folder = "File_Encrypt_PY"
    Internal_Data_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder)
    Key_Name = "JD_Enc.usk"
    Key_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder + "\\" + Key_Name)