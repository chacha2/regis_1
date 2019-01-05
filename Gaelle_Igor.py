import os.path
from pathlib import Path
import numpy as np

path_home = Path.home()
lst_fichier = os.listdir(path_home)
lst_size = [] 
def size_file(directory) : 
    lst_fichier = os.listdir(directory)
    for fichier in lst_fichier:
        if os.path.isfile(os.path.join(path_home,fichier)):
            lst_size.append(os.path.getsize(os.path.join(path_home,fichier)))
        try:
            if os.path.isdir(os.path.join(path_home,fichier)):
                size_file(os.path.join(path_home,fichier)) 
        except:
            pass
size_file(path_home)                      
result = np.mean(lst_size) 
print(int(result), "ouf c'est beaucoup tout ça !")