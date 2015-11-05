import subprocess

def mainMenu():
    print("\n1. Gather User Info")
    print("2. Gather Install Apps Info")
    print("3. Gather Services Info")

    menuSelection = int(input("\nEnter Selection: "))

    return menuSelection

def enumUsers():
    #Run id and output result to user_info.txt
    with open("user_info/user_info.txt", "w") as f:
        f.write("###OUTPUT OF ID###\n")
        f.close()
    with open("user_info/user_info.txt", "ab") as f:
        f.write(subprocess.check_output('id'))
        f.close()
    with open("user_info/user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()

    #Run who and append result to user_info.txt
    with open("user_info/user_info.txt", "a") as f:
        f.write("\n###OUTPUT OF WHO###\n")
        f.close()
    with open("user_info/user_info.txt", "ab") as f:
        f.write(subprocess.check_output('who'))
        f.close()
    with open("user_info/user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()

    #Run w and append result to user_info.txt
    with open("user_info/user_info.txt", "a") as f:
        f.write("\n###OUTPUT OF W###\n")
        f.close()
    with open("user_info/user_info.txt", "ab") as f:
        f.write(subprocess.check_output('w'))
        f.close()
    with open("user_info/user_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()


    print("Output Complete\n")

    main()

def enumApps():

    #Run w and append result to user_info.txt
    with open("app_info/app_info.txt", "a") as f:
        f.write("\n###Contents of /usr/bin###\n")
        f.close()
    with open("app_info/app_info.txt", "ab") as f:
        f.write(subprocess.check_output(["ls", "-alh", "/usr/bin/"]))
        f.close()
    with open("app_info/app_info.txt", "a") as f:
        f.write("\n============BREAK===============\n\n")
        f.close()


    main()

def enumServices():
    print("Place Holder")
    main()

def main():
    menuSelection = mainMenu()

    if menuSelection < 1 or menuSelection > 3:
        print("\nInvalid selection")
        mainMenu()
    elif menuSelection == 1:
        enumUsers()
    elif menuSelection == 2:
        enumApps()
    elif menuSelection == 3:
        enumServices()


main()
