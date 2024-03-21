from urllib.request import urlretrieve
import urls
from tqdm import tqdm
import os
from disk_cleanup import getPaths

def get_programs():
    i = 1
    print("Choose the programs: ")
    for program in urls.installers_urls:
        print(str(i) + ". " + (str(program).replace(".exe", "")).upper())
        i += 1

    user_choice = input("Enter your choices, when done press a key that is not a number: ")
    choice_list = [int(i) for i in user_choice.split() if i.isdigit()]
    return choice_list

def main():
    choice_list = get_programs()
    counter = 1
    with tqdm(total = len(choice_list)) as progress:
        for file_name, link in urls.installers_urls.items():
            if counter in choice_list:
                progress.set_description(file_name)
                fullfilename = os.path.join(getPaths()[0], file_name)
                urlretrieve(link, fullfilename)
                progress.update(1)
            counter += 1
