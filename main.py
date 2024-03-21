import disk_cleanup 
import program_downloader
import file_sorter
import os

def clear_console():
    clear = lambda: os.system('cls')
    clear()

while True:
    clear_console()
    print("Welcome to my silly utility program! For the moment it just does some basic tasks\nlike clean your folders and download some basic programs\nI wish to expand this and maybe migrate it to Powershell with CHOCOLATEY in the future!")
    print("[1] DISK CLEANUP\n[2] PROGRAM DOWNLOADER\n[3] FILE SORTER")
    action = input("Choose an action: ")
    
    try:
        int(action)
    except:
        print("Cancelling...")
        exit()

    if int(action) == 1:
        clear_console()
        disk_cleanup.main()
    elif int(action) == 2:
        clear_console()
        program_downloader.main()
    elif int(action) == 3:
        clear_console()
        file_sorter.main()
    else:
        break
        clear_console()