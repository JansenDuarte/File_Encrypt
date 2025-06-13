import os
import locale

class LocalSettings:

    #INFO: Remember not so send the changes in file names to git! You can change all the shit you want! But don't send you file location out

    Win_User_Path = os.path.join(os.environ['USERPROFILE'])

    #Path to save the encrypted file. File extension can be anything you want, withing reason of couse
    Enc_File_Path = "C:\\Jansen-PastaDados\\Important Info.sef"

    #Path to retrieve the actual file you want to encrypt.
    Dec_File_Path = "C:\\Jansen-PastaDados\\Important Info.txt"

    #Path to your private key. Not the safest, but we only want to keep some info from those pesky kids.
    Internal_Data_Folder = "File_Encrypt_PY"
    Internal_Data_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder)
    Key_Name = "JD_Enc.usk"
    Key_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder + "\\" + Key_Name)

    #Get system encoding to prevent w/r problems
    Sys_Encoding = locale.getencoding()


EXT_CODE_NORMAL = 0
EXT_CODE_KEY_FAILURE = -1
EXT_CODE_NON_EXISTING_FILE = -2
EXT_CODE_ENCODING_ERROR = -3
EXT_CODE_WINDOWS_ERROR = -99