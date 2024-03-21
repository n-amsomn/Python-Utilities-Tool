import disk_cleanup 
import program_downloader 
import os

def clear_console():
    clear = lambda: os.system('cls')
    clear()

print("Welcome to my silly utility program! For the moment it just does some basic tasks\nlike clean your folders and download some basic programs\nI wish to expand this and maybe migrate it to Powershell with CHOCOLATEY in the future!")
while True:
    print("[1] DISK CLEANUP\n[2] PROGRAM DOWNLOADER")
    action = input("Choose an action: ")

    try:
        int(action)
    except:
        print("Cancelling...")
        exit()

    if int(action) == 1:
        disk_cleanup.main()
        clear_console()
    elif int(action) == 2:
        program_downloader.main()
        clear_console()
    else:
        break
        clear_console()