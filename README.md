Encypt and decrypt a file to keep some data safeish
===

Information Layout
===
For information about the execution of the program, look in '00.Execution_Information.txt'.

For setting up the paths of encrypted/decrypted files and location of your prng private key, look in 'LocalSettings.py'

Tools for the Crazy
===
 This small tool can encrypt a file to keep some information 'secure'. Please keep in mind, this is NOT meant to keep your data secure from any cyber atacks, ransomware or anything like that! This is meant to keep your data secure from other people that might be using the same machine as you, maybe that wizz kid of yours that has started to mess around with files on your gaming pc and so on.


How To
===
 When using it for the first time, remember to set up a backup of the file you want to encrypt. Safety people!
 Clone the repo. Set up the paths in 'src/LocalSettings.py'. Run 'main.py' with -e option to encrypt the file and remove the easily modifiable version of it. Done! The file is encrypted. No kid f-ing this up now!
 To view and edit the file, run 'main.py' with -d option. It will generate a .txt and open it with Windows Notepad. Look around, edit the file if you wish. Save the changes, if you made any, then run 'main.py' with -e again and it will be encrypted again!


Special Thanks
===
 Thank you wifey, for keeping up with my shenanigans. And thank you Manolo for helping with the shenanigans!


Cheers! Keep Creating! Love, JD
===