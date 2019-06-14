import os

def rename_file():
    #(1) get file names from a folder
    dir_path = os.getcwd()
    dir_path += '\\prank'
    os.chdir(dir_path)
    file_list = os.listdir()
    
    #(2) for each file, rename filename
    intab = '123456789'
    outtab = '         '
    trantab = str.maketrans(intab,outtab,intab)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(trantab))


rename_file()