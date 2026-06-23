import os
import shutil

####################################################
dir = "./test"
app_dir = os.makedirs(dir , exist_ok=True)
def desinstalador():
    
    if os.path.exists(dir):
        shutil.rmtree (dir)
        print ("Desinstalando la aplicacion...")
    else:
        print ("Programa no encontrado")
        
if __name__ == "__main__":       
    desinstalador()