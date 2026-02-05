import os
import locale

class Settings:

    CURRENT_SYSTEM = os.name

    if (CURRENT_SYSTEM == 'nt'):
        User_Path = os.path.join(os.environ['USERPROFILE'])

        #Path to save the encrypted file. File extension can be anything you want, withing reason of couse
        Enc_File_Path = "C:\\My_Folder\\My_File.sef"

        #Path to retrieve the actual file you want to encrypt.
        Dec_File_Path = "C:\\My_Folder\\My_File.txt"

        #Path to your private key. Not the safest, but we only want to keep some info from those pesky kids.
        Internal_Data_Folder = "File_Encrypt_PY"
        Internal_Data_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder)
        Key_Name = "My_Key.usk"
        Key_Path = os.path.join(os.path.join(os.environ['USERPROFILE']), "AppData\\Local\\" + Internal_Data_Folder + "\\" + Key_Name)

        #Get system encoding to prevent w/r problems
        Sys_Encoding = locale.getencoding()
    elif (CURRENT_SYSTEM == 'posix'):
        User_Path = os.path.join(os.environ['HOME'])

        #Path to your private key. Not the safest, but we only want to keep some info from those pesky kids.
        Internal_Data_Folder = "00.jd_data"
        Internal_Data_Path = os.path.join(User_Path, f"{Internal_Data_Folder}")
        Key_Name = "jd_enc.usk"
        Key_Path = os.path.join(Internal_Data_Path, f"{Key_Name}")

        #Path to save the encrypted file. File extension can be anything you want, withing reason of couse
        Enc_File_Path = os.path.join(Internal_Data_Path, "important_info.sef")

        #Path to retrieve the actual file you want to encrypt.
        Dec_File_Path = os.path.join(Internal_Data_Path, "important_info.txt")


        #Get system encoding to prevent w/r problems
        Sys_Encoding = locale.getencoding()
