import os
import sys
from pathlib import Path
from shutil import rmtree
from tqdm import tqdm
from time import sleep

def deleteFiles(path_to_delete):
    count = 0
    with tqdm(total = len(os.listdir(path_to_delete))) as progress:
        for f in os.listdir(path_to_delete):
            progress.set_description(f)
            if os.path.isdir(os.path.join(path_to_delete, f)) == True:
                try:
                    rmtree(os.path.join(path_to_delete, f))
                except:
                    pass
            else:
                try:
                    os.remove(os.path.join(path_to_delete, f))
                except:
                    pass
            count +=1
            progress.update(1)

def getPaths():
    folder= [] 
    folder.append(str(Path.home() / 'Downloads'))
    folder.append(str(Path.home() / 'Appdata' / 'Local' / 'Temp'))
    folder.append(str(Path.home().drive + '/$Recycle.Bin'))
    folder.append(str(Path.home().drive + '/AMD'))
    return folder



print("Welcome to disk-cleanup!\n")
print("\nChoose action: ")
option = ["Full cleanup: DOWNLOADS + TEMP + RECYCLE BIN", "Half cleanup: TEMP + RECYCLE BIN", "DOWNLOADS folder only", "Full cleanup + AMD Installers"]
print("[1] " + option[0] + "\n[2] " +option[1]+ "\n[3] " +option[2]+ "\n[4] " + option[3])
print("\nTo cancel input any other key!")
choice = input("Chosen action: ")


try:
    choice = int(choice)
except ValueError:
    print("Cancelling...")
    sys.exit(0)

if choice in range(1,5):
    print("You are about to perform a ", end = "")
    for i in range(1,5):
        if i == choice:
            print(option[i-1].upper(), end = "")
    print(" are you sure?: ")
else:
    print("Cancelling...")
    sleep(2)
    sys.exit(0)
    
choice = input()
if choice.lower() == 'y' or choice.lower() == 'yes':
    print("Starting cleanup!")
    sleep(2)
else:
    print("Cancelling...")
    sleep(2)
    sys.exit(0)

# downloads_folder = str(Path.home() / 'Downloads')
# temp_folder = str(Path.home() / 'Appdata' / 'Local' / 'Temp')
# recyblebin_folder = str(Path('C:/') / '$Recycle.Bin')

if choice == 1:
    deleteFiles(getPaths()[0])
    deleteFiles(getPaths()[1])
    deleteFiles(getPaths()[2])
elif choice == 2:
    deleteFiles(getPaths()[1])
    deleteFiles(getPaths()[2]) 
elif choice == 3:
    deleteFiles(getPaths()[0])
else:
    deleteFiles(getPaths()[0])
    deleteFiles(getPaths()[1])
    deleteFiles(getPaths()[2])
    deleteFiles(getPaths()[3])

print("DONE")
