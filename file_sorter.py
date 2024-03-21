from disk_cleanup import getPaths
import os
import json
import time
from tqdm import tqdm

try:
    with open('rules.json', 'r') as file:
        rules_file = json.load(file)
except FileNotFoundError:
        rules_file = {}

downloads = getPaths()[0]

def main():
    print("Welcome to rules_file sorting!\nPlease choose an action:\n[1] Sort the DOWNLOADS rules_file\n[2] Make a NEW sorting rule\n[3] DELETE an existing sorting rule\nTo cancel press any other key!")
    while True:
        action = input("\nChoose an action: ")
        try:
            action = int(action)
        except:
            print("Cancelling...")
            exit()

        if action in range(1,4):
            if action == 1:
                sortrules_files(rules_file)
            elif action ==2:
                newSortingRule(rules_file)
            else:
                removeSortingRule(rules_file)
        else:
            print("Cancelling...")
            exit()




def sortrules_files(rules_file):
    ##create folders##
    print("Generating folders locations for the existing rules: ")
    for k in rules_file:
        try:
            os.mkdir(downloads + '/' + k)
            print(k+" done |", end = ' ')
        except:
            print(k+ " already exists |", end = ' ')
    ##begin sorting##
    with tqdm(total = len(os.listdir(downloads))) as progress:
        for f in os.listdir(downloads):
            progress.set_description(f)
            full_path = os.path.join(downloads, f)
            if os.path.isdir(full_path):
                progress.update(1)
                time.sleep(0.1)
                continue
            for k, p in rules_file.items():
                file_extension = f[f.rfind("."):]
                if file_extension in p:
                    try:
                        destination_folder = os.path.join(downloads, k)
                        os.makedirs(destination_folder, exist_ok=True) 
                        os.replace(full_path, os.path.join(destination_folder, f))
                        progress.update(1)
                        time.sleep(0.1)
                    except FileNotFoundError:
                        print("File not found:", full_path)
                        progress.update(1)
                        time.sleep(0.1)
                    except PermissionError:
                        print("Permission denied for file:", full_path)
                        progress.update(1)
                        time.sleep(0.1)
                    except Exception as e:
                        print("Error:", e)
                        progress.update(1)
                        time.sleep(0.1)


def newSortingRule(rules_file):
    name = input("Name the folder: ")
    rules_file[name] = ''
    type_string = input("Enter the file type separated by space: ")
    type = type_string.split()
    rules_file[name] = type
    with open('rules.json', 'w') as file:
        json.dump(rules_file, file)

def removeSortingRule(rules_file):
    print(rules_file)
    print("Please choose the rule folder you want to delete: ", end='')

    choice = input()
    try:
        del rules_file[choice]
        with open('rules.json', 'w') as file:
            json.dump(rules_file, file)
    except:
        print("Not a valid choice")




    
