import os,time
from urllib.parse import ParseResultBytes
from pathlib import Path
from myemail import *

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
    
#joga os textos nos arquivos
def makedata(the_file,new_data):
    make_file = open(the_file,"w")
    make_file.writelines(new_data)
    make_file.close()
    pass

def comparation_of_file(file1,file2):
    if Path(file1).stat().st_size == Path(file2).stat().st_size:
        return True
    else:
        return False

def filescode(name_of_file,data,link_of_page):
    if checkFileExistance(name_of_file)==True:
        #cria novo arquivo
        newstr = name_of_file.replace(".txt", "2.txt")
        creat_file = open(newstr,"w+")
        creat_file.close()
        makedata(newstr,data)
        #compara
        if comparation_of_file(name_of_file,newstr)==True:
        #se igual exluir newstr
            os.remove(newstr)
        else:#se diferente manda e-mail
            os.remove(name_of_file)
            os.rename(newstr,name_of_file)
            send_email(link_of_page,name_of_file.replace(".txt",""))
        
    else:
        creat_file = open(name_of_file,"w+")
        creat_file.close()
        makedata(name_of_file,data)