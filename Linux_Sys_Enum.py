#!/usr/bin/env python3

import subprocess


def enumUsers():
    #Run id and output result to user_info.txt
    #subprocess.call(["mkdir", "user_info"])
    with open("user_info.txt", "a") as f:
        f.write("###OUTPUT OF ID###\n")
        f.close()
    with open("user_info.txt", "ab") as f:
        f.write(subprocess.check_output('id'))
        f.close()
    with open("user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()

    #Run who and append result to user_info.txt
    with open("user_info.txt", "a") as f:
        f.write("\n###OUTPUT OF WHO###\n")
        f.close()
    with open("user_info.txt", "ab") as f:
        f.write(subprocess.check_output('who'))
        f.close()
    with open("user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()

    #Run w and append result to user_info.txt
    with open("user_info.txt", "a") as f:
        f.write("\n###OUTPUT OF W###\n")
        f.close()
    with open("user_info.txt", "ab") as f:
        f.write(subprocess.check_output('w'))
        f.close()
    with open("user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()


    print("Output Complete\n")

    main()

def enumApps():

    #Run w and append result to user_info.txt
    with open("app_info.txt", "a") as f:
        f.write("\n###Contents of /usr/bin###\n")
        f.close()
    with open("app_info.txt", "ab") as f:
        f.write(subprocess.check_output(["ls", "-alh", "/usr/bin/"]))
        f.close()
    with open("app_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()


    main()

def enumServices():
    #Run and append result to user_info.txt
    with open("services_info.txt", "a") as f:
        f.write("\n###Result of ps aux###\n")
        f.close()
    with open("services_info.txt", "ab") as f:
        f.write(subprocess.check_output(["ps", "aux"]))
        f.close()
    with open("services_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()

def main():

    menu = {}
    menu['1']="Gather User Info"
    menu['2']="Gather Installed Apps Info"
    menu['3']="Gather Services Info"
    menu['4']='Get Everything'
    menu['5']="Exit"
    while True:
        for entry in sorted(menu, key=int):
            print(entry, menu[entry])

        selection=input("\nPlease Select: ")
        if selection =='1':
            enumUsers()
        elif selection == '2':
            enumApps()
        elif selection == '3':
            enumServices()
        elif selection == '4':
            enumApps()
            enumUsers()
            enumServices()
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")



main()
