#Renaming multiple files in a folder to find a secret message.
import os

def rename_files():
    file_list = os.listdir(r"C:\Users\pradn\Desktop\Masters\Python_Coding_Challenges\prank")
    current_path = os.getcwd()
    os.chdir(r"C:\Users\pradn\Desktop\Masters\Python_Coding_Challenges\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(file_name.maketrans('', '','0123456789')))
    os.chdir(current_path)
    print("All the file names in the folder have been renamed.")

rename_files()
