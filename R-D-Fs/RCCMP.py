#Packages
#========================================#
import json
import requests
import subprocess
from os.path import exists
import shutil
import os
import urllib.request
from colorama import Fore,Back,init
init(autoreset=True)
import msvcrt
import tempfile
import webbrowser as web
import ctypes
import os
import sys
import time
import importlib.util
#========================================#

# RCC COnfiguration
#===============================#
RCC_version = "4.0.0"
RCC_RD = "04/17/2024"
RCC_cache_id = "RCC81652335434"
#===============================#

def StartRCC():
    #Console configuration
    #============================================================================================#
    def change_console_resolution(rows, columns):
        os.system(f"mode con: cols={columns} lines={rows}")

    def disable_console_resize():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()

        # Retrieve the current window style
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)  # -16 corresponds to GWL_STYLE

        # Disable resizing (WS_THICKFRAME and WS_MAXIMIZEBOX)
        style = style & ~0x00040000  # 0x00040000 corresponds to WS_THICKFRAME
        style = style & ~0x00010000  # 0x00020000 corresponds to WS_MAXIMIZEBOX

        # Set the modified style
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

    disable_console_resize()
    #============================================================================================#

    #logo def function
    #===============================================================================================================#
    def logo():
        print(Fore.LIGHTYELLOW_EX+r''' ____       _     _              ____ _ _            _   
|  _ \ ___ | |__ | | _____  __  / ___| (_) ___ _ __ | |_ 
| |_) / _ \| '_ \| |/ _ \ \/ / | |   | | |/ _ \ '_ \| __|
|  _ < (_) | |_) | | (_) >  <  | |___| | |  __/ | | | |_ 
|_| \_\___/|_.__/|_|\___/_/\_\  \____|_|_|\___|_| |_|\__|
                                                        
  ____          _                  _              
 / ___|   _ ___| |_ ___  _ __ ___ (_)_______ _ __ 
| |  | | | / __| __/ _ \| '_ ` _ \| |_  / _ \ '__|
| |__| |_| \__ \ || (_) | | | | | | |/ /  __/ |   
 \____\__,_|___/\__\___/|_| |_| |_|_/___\___|_|   
                                                    
    ''')

    def PTC():
        msvcrt.getch()
    #===============================================================================================================#
        
    #Json Configuration
    #===========================================================================#
    location_path = os.path.join(tempfile.gettempdir(), f"{RCC_cache_id}.json")
    #===========================================================================#

    #ClientAPI Server connection
    #===========================================================================================================#
    try:
        change_console_resolution(18, 65)
        logo()
        # Make a request to the URL
        response = requests.get(f"https://raw.githubusercontent.com/Eagisa/RCC/main/RCC-Ss/RCC-S.json")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            change_console_resolution(41, 64)
            json_object = response.json()

            # Accessing values for APIs
            C_S_1 = json_object["C-S-1"]["key"]
            C_S_2 = json_object["C-S-2"]["key"]
            C_S_3 = json_object["C-S-3"]["key"]
            R_S_F = json_object["R-S-F"]["key"]
            os.system("cls")
            logo()
        else:
            change_console_resolution(18, 88)
            os.system("cls")
            logo()
            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ", Fore.LIGHTYELLOW_EX+f"> Error couldn't compile RCC-Ss\n")
            PTC()
            exit()
    except requests.ConnectionError:
        os.system("cls")
        logo()
        PTC()
        exit()
    #===========================================================================================================#
        
    #update def function
    #=================================================================================================================================#
    def Update():
        #Update changes
        print(Fore.LIGHTYELLOW_EX+"<+>------------------------------------------------------<+>\n",
            "  ",Fore.BLACK+Back.LIGHTGREEN_EX+" UPDATE ",Fore.LIGHTYELLOW_EX+"> Added New Options, Optimized, Bugs Fixed!")
        print(Fore.LIGHTYELLOW_EX+"<+>------------------------------------------------------<+>\n")
    Update()
    #=================================================================================================================================#

    #Downloads the latest version of Roblox Client
    #==============================================================================================================================================#
    def download():
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        # Roblox launcher (aka: Roblox installer) downloader link
        # url = 'https://setup.rbxcdn.com/' + a + '-Roblox.exe'  # (if not working)
        url = 'https://www.roblox.com/download/client'  # (If setup.rbxcdn not working, use this link)
        filename = 'RobloxPlayerInstaller.exe'
        destination = os.path.join(downloads_path, filename)  # Replace 'path_to_your_folder' with the desired folder path

        try:
            urllib.request.urlretrieve(url, destination)
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Installing roblox...\n")
            install()  # Assuming you have defined the install function elsewhere
        except urllib.error.URLError as e:
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Error occurred while installing roblox-player:", e)
            PTC()
    #==============================================================================================================================================#

    #Installing the downloaded Roblox Client setup
    #===================================================================================================================================================#
    def install():
        # Assuming Downloads is a subdirectory in the user's home directory
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        Roblox_installer_path = os.path.join(downloads_path, "RobloxPlayerInstaller.exe")

        if os.path.exists(Roblox_installer_path):
            os.startfile(Roblox_installer_path)
        else:
            print("", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> {{Error couldn't install the latest version of Roblox Client}}")
            PTC()
    #===================================================================================================================================================#

    #This function search for roblox player
    #=====================================================================================================================================#
    def SearchForRoblox():
        debug = False

        def Find_Roblox_player(file_name, folder_path):
            for folder_name, _, files in os.walk(folder_path):
                if file_name in files:
                    return folder_name
            return None

        # Replace 'your_file_name.extension' with the actual file name you're looking for
        file_to_find = 'RobloxPlayerBeta.exe'

        # Define the list of possible paths to search
        search_paths = [
            (os.getenv('LOCALAPPDATA'), 'LOCALAPPDATA'),
            (os.getenv('ProgramFiles(x86)'), 'ProgramFiles(x86)'),
            (os.getenv('ProgramFiles'), 'ProgramFiles')
        ]

        result = None

        # Iterate through each path in search_paths until the file is found
        for path, directory_name in search_paths:
            result = Find_Roblox_player(file_to_find, os.path.join(path, 'Roblox', 'Versions'))
            if result:
                break

        if result and not debug:
            # Using os.path.basename to get the folder name without the full path
            directory_name = os.path.basename(directory_name)
            folder_name = os.path.basename(result)

            Default = {
                "Path": directory_name,
                "Client_Ver": folder_name
            }
            json_data_1 = json.dumps(Default, indent=2)
                
            file_name = f"{RCC_cache_id}.json"
            file_path = os.path.join(tempfile.gettempdir(), file_name)

            with open(file_path, 'w') as json_file:
                json_file.write(json_data_1)
        else:
            change_console_resolution(29, 60)
            logo()
            Update()
            print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Roblox player is not installed in this system.\n")

            #Roblox client version API
            print(Fore.LIGHTYELLOW_EX+"\n                  Options\n"
                    "<+>--------------------------------------<+>\n"
                    " | (1) Type 'Y' To Install Roblox-Player  |\n"
                    " |----------------------------------------|\n"
                    " | (2) Type 'N' To Skip                   |\n"
                    "<+>--------------------------------------<+>\n")
            while True:
                entry = input(Fore.LIGHTYELLOW_EX+"Choose an option [Y or N]?: ").lower()
                if entry == 'y':
                    download()
                    print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> After the roblox player installation completed.\n"
                        "            restart the RCC program")
                    PTC()
                    exit()
                elif entry == 'n':
                    print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> If the issue is resolved, Try the program again")
                    PTC()
                    exit()
                else:
                    print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> That was invailed, Try again!")
                    
    SearchForRoblox()
    #=====================================================================================================================================#


    #Always Checks if RobloxPlayerLauncher.exe exists it will delete it after the installation is done
    #====================================================================================#
    def RemoveAlways():
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        filename_to_remove = "RobloxPlayerInstaller.exe"
        file_path = os.path.join(downloads_path, filename_to_remove)

        if os.path.exists(file_path):
            os.remove(file_path)
            main()
        else:
            main()
    #====================================================================================#

    #RCC_cache_id.json To troubleshoot the issue
    #=========================================================#
    with open(location_path, "r") as json_file:
        loaded_data_RCC = json.load(json_file)
    #=========================================================#

    #API Configure of RCC_cache_id.json
    #===============================================#
    Path_Directory = str(loaded_data_RCC["Path"])
    Client_ver = str(loaded_data_RCC["Client_Ver"])
    #===============================================#

    #Roblox Path
    #==================================================================================================================#
    version_path = os.path.join(os.getenv(Path_Directory), 'Roblox', 'Versions', Client_ver)
    Roblox_Player = os.path.join(os.getenv(Path_Directory), 'Roblox', 'Versions', Client_ver, 'RobloxPlayerBeta.exe')
    #==================================================================================================================#

    #roblox installer
    #==========================================================================================================================================#
    def setup():
        change_console_resolution(31, 64)
        logo()
        Update()
        SearchForRoblox()
        print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Unable to connect latest roblox client!\n")
        #Roblox client version API
        print(Fore.LIGHTYELLOW_EX+"\n                  Options\n"
                "<+>--------------------------------------<+>\n"
                " | (1) Type 'Y' To Install Roblox-Player  |\n"
                " |----------------------------------------|\n"
                " | (2) Type 'N' To Skip                   |\n"
                "<+>--------------------------------------<+>\n")
        while True:
            entry = input(Fore.LIGHTYELLOW_EX+"Choose an option [Y or N]?: ").lower()
            if entry == 'y':
                download()
                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> After the roblox player installation completed.\n"
                    "            restart the RCC program")
                PTC()
                exit()
            elif entry == 'n':
                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> If the issue is resolved, Try the program again")
                input()
                exit()
            else:
                print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> That was invailed, Try again!")
    #==========================================================================================================================================#

    #Connectivity checker
    #==========================================================================================================================================#
    debug = False
    def RobloxClientConnectivityChecker():
        if exists(Roblox_Player) and not debug:
            print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Connected to "+Client_ver,"\n")
        else:
            print("",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Unable to connect latest roblox client!\n")
            setup()
            exit(1)
    RobloxClientConnectivityChecker()
    #==========================================================================================================================================#

    #Menu (Options)
    #=========================================================#
    def Options():
        print(Fore.LIGHTYELLOW_EX+"                  Options\n"
            "<+>---------------------------------------<+>\n"
            " | (?) | Help?                             |\n"
            " |-----------------------------------------|\n"
            " | (1) | Check Byfron Status               |\n"
            " |-----------------------------------------|\n"
            " | (2) | Install ClientSettings            |\n"
            " |-----------------------------------------|\n"
            " | (3) | Open Roblox Player Location       |\n"
            " |-----------------------------------------|\n"
            " | (4) | Check Roblox Player Information   |\n"
            " |-----------------------------------------|\n"
            " | (5) | Install OOF Sound                 |\n"
            " |-----------------------------------------|\n"
            " | (6) | Clear Cache                       |\n"
            " |-----------------------------------------|\n"
            " | (7) | Reset Roblox Player Settings      |\n"
            " |-----------------------------------------|\n"
            " | (8) | Delete in-Game Textures           |\n"
            "<+>---------------------------------------<+>\n")
    Options()
    #=========================================================#

    #main program
    #=================================================================================================================================================================================================#
    def main():
        while True:
            command = input(Fore.LIGHTYELLOW_EX+"> ").strip()
            #Byfron-Status
            if command == '1':
                byf = os.path.join(version_path, 'RobloxPlayerBeta.dll')
                if os.path.exists(Roblox_Player):
                    if exists(byf) and not debug:
                        print("        ",Fore.LIGHTYELLOW_EX+" Byfron Status ")
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+" Byfron Service: ",Fore.BLACK+Back.LIGHTGREEN_EX+" Active ",Fore.LIGHTYELLOW_EX+" |")
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------<+>\n")
                    else:
                        print("        ",Fore.LIGHTYELLOW_EX+" Byfron Status ")
                        print(Fore.LIGHTYELLOW_EX+"<+>-----------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+" Byfron Service: ",Fore.BLACK+Back.LIGHTRED_EX+" In-Active ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+"<+>-----------------------------<+>\n")
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")
            
                #Client-App-Settings
            elif command == '2':
                if os.path.exists(Roblox_Player):
                    print("               ",Fore.LIGHTYELLOW_EX+"<+>-----------------------<+>\n"
                    "                "+"    Custom ClientSettings\n"
                    "                "+"<+>-----------------------<+>")

                    response = requests.get(C_S_1)
                    if not response.status_code == 404:
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |(1) ClientAppSettings - (L8X_RCO)     | Status |",Fore.BLACK+Back.LIGHTGREEN_EX+" Online  ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+" |-----------------------------------------------------------|")
                    else:
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |(1) ClientAppSettings - (L8X_RCO)     | Status |",Fore.BLACK+Back.LIGHTRED_EX+" Offline ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+" |-----------------------------------------------------------|")
                    
                    response = requests.get(C_S_2)
                    if not response.status_code == 404:
                        print(Fore.LIGHTYELLOW_EX+" |(2) ClientAppSettings - (RCC)         | Status |",Fore.BLACK+Back.LIGHTGREEN_EX+" Online  ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+" |-----------------------------------------------------------|")
                    else:
                        print(Fore.LIGHTYELLOW_EX+" |(2) ClientAppSettings - (RCC)         | Status |",Fore.BLACK+Back.LIGHTRED_EX+" Offline ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+" |-----------------------------------------------------------|")
                    
                    response = requests.get(C_S_3)
                    if not response.status_code == 404:
                        print(Fore.LIGHTYELLOW_EX+" |(3) ClientAppSettings - (BloxStrap)   | Status |",Fore.BLACK+Back.LIGHTGREEN_EX+" Online  ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------------------------------------<+>")
                    else:
                        print(Fore.LIGHTYELLOW_EX+" |(3) ClientAppSettings - (BloxStrap)   | Status |",Fore.BLACK+Back.LIGHTRED_EX+" Offline ",Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+"<+>---------------------------------------------------------<+>")
                        
                    while True:
                        choice = input(Fore.LIGHTYELLOW_EX+"\nChoose an ClientSettings to install or (exit): ").strip()
                            
                        #ClientSettings Installer 1
                        if choice == '1':
                            response = requests.get(C_S_1)

                            if response.status_code == 404:
                                print("", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> {404: Not Found} ClientSettings - (L8X_RCO) Error!")
                                main()

                            data = response.json()
                            client_settings_path = os.path.join(version_path, 'ClientSettings')

                            # Check if the directory already exists
                            if os.path.exists(client_settings_path):
                                # Overwrite the file if it already exists
                                pass
                            else:
                                os.mkdir(client_settings_path)

                            location = os.path.join(client_settings_path, 'ClientAppSettings.json')
                            file_location = os.path.join(os.path.expanduser("~"), location)

                            # Use "w" mode to overwrite the file
                            with open(file_location, "w") as file:
                                json.dump(data, file, indent=2)

                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> ClientSettings - (L8X_RCO) is installed!\n")
                            main()

                        #ClientSettings Installer 2
                        elif choice == '2':
                            response = requests.get(C_S_2)

                            if response.status_code == 404:
                                print("", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> {404: Not Found} ClientSettings - (RCC) Error!")
                                main()

                            data = response.json()
                            client_settings_path = os.path.join(version_path, 'ClientSettings')

                            # Check if the directory already exists
                            if os.path.exists(client_settings_path):
                                # Overwrite the file if it already exists
                                pass
                            else:
                                os.mkdir(client_settings_path)

                            location = os.path.join(client_settings_path, 'ClientAppSettings.json')
                            file_location = os.path.join(os.path.expanduser("~"), location)

                            # Use "w" mode to overwrite the file
                            with open(file_location, "w") as file:
                                json.dump(data, file, indent=2)

                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> ClientSettings - (RCC) is installed!\n")
                            main()
                        
                        #ClientSettings Installer 3
                        elif choice == '3':
                            response = requests.get(C_S_3)

                            if response.status_code == 404:
                                print("", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> {404: Not Found} ClientSettings - (BloxStrap) Error!")
                                main()

                            data = response.json()
                            client_settings_path = os.path.join(version_path, 'ClientSettings')

                            # Check if the directory already exists
                            if os.path.exists(client_settings_path):
                                # Overwrite the file if it already exists
                                pass
                            else:
                                os.mkdir(client_settings_path)

                            location = os.path.join(client_settings_path, 'ClientAppSettings.json')
                            file_location = os.path.join(os.path.expanduser("~"), location)

                            # Use "w" mode to overwrite the file
                            with open(file_location, "w") as file:
                                json.dump(data, file, indent=2)

                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> ClientSettings - (BloxStrap) is installed!\n")
                            main()
                        
                        elif choice == 'exit':
                            break
                        
                        else:
                            print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> That was invailed")

                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")   
                
                #Open-Client-Path
            elif command == '3':
                if os.path.exists(Roblox_Player):
                    file_location = version_path
                    if os.path.exists(file_location):
                        os.startfile(file_location)
                        print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Roblox Player Location is Open\n")
                    else:
                        print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Couldn't Open the Roblox Player Location\n")
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")   

                #All-Client-Information
            elif command == '4':
                if os.path.exists(Roblox_Player):
                    byf = os.path.join(version_path, 'RobloxPlayerBeta.dll')
                    if exists(byf) and not debug:
                        print("         ",Fore.LIGHTYELLOW_EX+"<+>--------------------------------------<+>")
                        print("                ",Fore.LIGHTYELLOW_EX+"Roblox Game Client Information")
                        print("         ",Fore.LIGHTYELLOW_EX+"<+>--------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+"<+>----------------------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Byfron Service                 ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTGREEN_EX+" Active ",Fore.LIGHTYELLOW_EX+"                |")
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Roblox Game Client Type        ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.YELLOW+" 64-Bit ",Fore.LIGHTYELLOW_EX+"                |")
                    else:
                        print("         ",Fore.LIGHTYELLOW_EX+"<+>--------------------------------------<+>")
                        print("                ",Fore.LIGHTYELLOW_EX+"Roblox Game Client Information")
                        print("         ",Fore.LIGHTYELLOW_EX+"<+>--------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+"<+>----------------------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Byfron Service                 ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTRED_EX+" In-Active ",Fore.LIGHTYELLOW_EX+"             |")
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Roblox Game Client Type        ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.CYAN+" 32-Bit ",Fore.LIGHTYELLOW_EX+"                |")
                    location = os.path.join(version_path, 'ClientSettings', 'ClientAppSettings.json')
                    if exists(location) and not debug:
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"ClientSettings                 ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTGREEN_EX+" Installed ",Fore.LIGHTYELLOW_EX+"             |")
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Roblox Game Client Version     ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTGREEN_EX+ Client_ver ,Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+"<+>----------------------------------------------------------<+>\n")
                    else:
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"ClientSettings                 ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTRED_EX+" Not-Installed ",Fore.LIGHTYELLOW_EX+"         |")
                        print(Fore.LIGHTYELLOW_EX+" |------------------------------------------------------------|")
                        print(Fore.LIGHTYELLOW_EX+" |",Fore.LIGHTYELLOW_EX+"Roblox Game Client Version     ",Fore.LIGHTYELLOW_EX+"|",Fore.BLACK+Back.LIGHTGREEN_EX+ Client_ver ,Fore.LIGHTYELLOW_EX+"|")
                        print(Fore.LIGHTYELLOW_EX+"<+>----------------------------------------------------------<+>\n")
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")
            
            elif command == '5':
                if os.path.exists(Roblox_Player):
                    # Destination directory
                    file_location = os.path.join(version_path, 'content', 'sounds', 'ouch.ogg')
                    # Download the file
                    response = requests.get(R_S_F)
                    if response.status_code == 200:
                        with open(file_location, 'wb') as file:
                            file.write(response.content)

                            if os.path.exists(file_location):
                                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ",
                                    Fore.LIGHTYELLOW_EX + "> Oof sound is installed!\n")
                            else:
                                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ",
                                    Fore.LIGHTYELLOW_EX + "> Couldn't install oof sound\n")
                    else:
                        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ",
                            Fore.LIGHTYELLOW_EX + "> Failed to \n")
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")

            elif command == '6':
                if os.path.exists(Roblox_Player):
                    def Roblox():
                        #Roblox Game Cache
                        #=============================================================================================================================#
                        def clear_roblox_cache(folder_path):
                            try:
                                for root, _, files in os.walk(folder_path, topdown=False):
                                    for file in files:
                                        file_path = os.path.join(root, file)
                                        os.remove(file_path)
                                    for dir_path in os.listdir(root):
                                        dir_path = os.path.join(root, dir_path)
                                        if os.path.isdir(dir_path):
                                            shutil.rmtree(dir_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared Roblox HTTP Cache\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear Roblox HTTP Cache\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        temp_path = os.path.join(localappdata_path, 'Temp')
                        roblox_cache_path = os.path.join(temp_path, 'Roblox')

                        clear_roblox_cache(roblox_cache_path)
                        #=============================================================================================================================#

                        #Roblox Crashpad Caches
                        #=========================================================================================================================#
                        def clear_crashpad_roblox(folder_path):
                            try:
                                for filename in os.listdir(folder_path):
                                    file_path = os.path.join(folder_path, filename)
                                    if os.path.isfile(file_path):
                                        os.remove(file_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared Crashpad_Roblox\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear Crashpad_Roblox\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        temp_path = os.path.join(localappdata_path, 'Temp')
                        crashpad_roblox_path = os.path.join(temp_path, 'crashpad_roblox')

                        clear_crashpad_roblox(crashpad_roblox_path)
                        #=========================================================================================================================#

                        #Roblox RBX-.log Cache
                        #====================================================================================================================#
                        def clear_rbx_logs(folder_path):
                            try:
                                for filename in os.listdir(folder_path):
                                    if filename.startswith('RBX-') and filename.endswith('.log'):
                                        file_path = os.path.join(folder_path, filename)
                                        os.remove(file_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared RBX Logs\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear RBX Logs\n")

                        Roblox_RBX_logs_path = os.environ.get('TEMP')

                        clear_rbx_logs(Roblox_RBX_logs_path)
                        #======================================================================================================================#
                        def clear_rbx_folder(folder_path):
                            try:
                                for filename in os.listdir(folder_path):
                                    if filename.startswith('RBX-') and os.path.isdir(os.path.join(folder_path, filename)):
                                        rbx_folder_path = os.path.join(folder_path, filename)
                                        shutil.rmtree(rbx_folder_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared RBX Files\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear RBX Files\n")

                        Roblox_RBX_logs_path = os.environ.get('TEMP')

                        clear_rbx_folder(Roblox_RBX_logs_path)
                        #====================================================================================================================#

                        #Roblox Logs
                        #==========================================================================================================================#
                        def clear_roblox_logs(folder_path):
                            try:
                                for filename in os.listdir(folder_path):
                                    file_path = os.path.join(folder_path, filename)
                                    if os.path.isfile(file_path):
                                        os.remove(file_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared Roblox Logs\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Could't Clear Roblox Logs\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        roblox_path = os.path.join(localappdata_path, 'Roblox')
                        roblox_logs_path = os.path.join(roblox_path, 'logs')

                        clear_roblox_logs(roblox_logs_path)
                        #==========================================================================================================================#

                        #Roblox Downloads Cache
                        #=============================================================================================================================#
                        def clear_roblox_downloads(folder_path):
                            try:
                                for item in os.listdir(folder_path):
                                    item_path = os.path.join(folder_path, item)
                                    if os.path.isfile(item_path):
                                        os.remove(item_path)
                                    elif os.path.isdir(item_path):
                                        clear_roblox_downloads(item_path)
                                        os.rmdir(item_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared Roblox Downloads\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear Roblox Downloads\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        temp_path = os.path.join(localappdata_path, 'Roblox')
                        roblox_downloads_path = os.path.join(temp_path, 'Downloads')

                        clear_roblox_downloads(roblox_downloads_path)
                        #=============================================================================================================================#

                        #Rbxcsettings.rbx 
                        #=========================================================================================================================#
                        def clear_roblox_EffectPredictor(folder_path):
                            try:
                                for item in os.listdir(folder_path):
                                    item_path = os.path.join(folder_path, item)
                                    if os.path.isfile(item_path):
                                        os.remove(item_path)
                                    elif os.path.isdir(item_path):
                                        clear_roblox_downloads(item_path)
                                        os.rmdir(item_path)
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Successfully Cleared Roblox EffectPredictor\n")
                            except Exception as e:
                                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> Error Couldn't Clear Roblox EffectPredictor\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        temp_path = os.path.join(localappdata_path, 'Roblox')
                        roblox_downloads_path = os.path.join(temp_path, 'EffectPredictor')

                        clear_roblox_EffectPredictor(roblox_downloads_path)
                        #=========================================================================================================================#

                        #Clears Roblox LocalStorage Cache
                        #====================================================================================================================================#
                        def clear_roblox_localStorageCache(folder_path):
                            try:
                                for root, _, files in os.walk(folder_path, topdown=False):
                                    for file in files:
                                        file_path = os.path.join(root, file)
                                        os.remove(file_path)
                                    for dir_path in os.listdir(root):
                                        dir_path = os.path.join(root, dir_path)
                                        if os.path.isdir(dir_path):
                                            shutil.rmtree(dir_path)
                                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Successfully Cleared LocalStorage Cache\n")
                            except Exception as e:
                                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Error Couldn't Clear LocalStorage Cache\n")

                        localappdata_path = os.environ.get(Path_Directory)
                        roblox_path = os.path.join(localappdata_path, 'Roblox')
                        roblox_LocalStorageCache_path = os.path.join(roblox_path, 'LocalStorage')

                        clear_roblox_localStorageCache(roblox_LocalStorageCache_path)
                    #====================================================================================================================================#

                    #Window Command Clears IpConfig DNS cache
                    #================================================#
                        command = ["ipconfig", "/flushdns"]
                        try:
                            subprocess.run(command, check=True)
                            print(Fore.LIGHTYELLOW_EX+"DNS cache flushed successfully.")
                        except subprocess.CalledProcessError as e:
                            print(Fore.LIGHTYELLOW_EX+"Error flushing DNS cache:", e)
                    #================================================#

                    Roblox()
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")
                
            #Reset Roblox Player Settings
            elif command == '7':
                if os.path.exists(Roblox_Player):
                    #Roblox Settings Cache
                    #==================================================================================================================================================#
                    base_path_key = Path_Directory
                    base_path = os.environ.get(base_path_key, '')

                    # Add the 'Roblox' folder to the path
                    roblox_folder = 'Roblox'
                    base_path = os.path.join(base_path, roblox_folder)

                    file_names = [
                        'AnalysticsSettings.xml',
                        'frm.cfg',
                        'GlobalBasicSettings_13.xml'
                    ]

                    file_paths = [os.path.join(base_path, file_name) for file_name in file_names]

                    for file_path in file_paths:
                        if os.path.exists(file_path):
                            try:
                                os.remove(file_path)
                                print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + f"> Successfully Cleared {os.path.relpath(file_path, base_path)}\n")
                            except OSError as e:
                                print(f"Error while deleting '{file_path}': {e}")
                        else:
                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + f"> Error Couldn't Clear {os.path.relpath(file_path, base_path)}\n")
                    #==================================================================================================================================================#

                    #Clears IpConfig Cache
                    #============================================#
                    command = ["ipconfig", "/flushdns"]
                    try:
                        subprocess.run(command, check=True)
                        print(Fore.LIGHTYELLOW_EX+"DNS cache flushed successfully.")
                    except subprocess.CalledProcessError as e:
                        print(Fore.LIGHTYELLOW_EX+"Error flushing DNS cache:", e)
                    #============================================#
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")
            
            elif command == '8':
                if os.path.exists(Roblox_Player):
                    def clear_roblox_texture(folder_path):
                        try:
                            for root, _, files in os.walk(folder_path, topdown=False):
                                for file in files:
                                    file_path = os.path.join(root, file)
                                    os.remove(file_path)
                                for dir_path in os.listdir(root):
                                    dir_path = os.path.join(root, dir_path)
                                    if os.path.isdir(dir_path):
                                        shutil.rmtree(dir_path)
                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Successfully deleted roblox in-game textures\n")
                        except Exception as e:
                            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Error Couldn't deleted roblox in-game textures\n")

                    localappdata_path = os.environ.get(Path_Directory)
                    roblox_textures_path = os.path.join(localappdata_path, version_path, 'PlatformContent', 'pc', 'textures')

                    clear_roblox_texture(roblox_textures_path)
                else:
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> Roblox-Client is disconnected!\n")
            
            elif command == '?':
                os.system("cls")
                change_console_resolution(18, 50)
                def RCC_Logo():
                    print(Fore.LIGHTYELLOW_EX+r''' ____         ____        ____ 
|  _ \       / ___|      / ___|
| |_) |     | |         | |    
|  _ <   _  | |___   _  | |___ 
|_| \_\ (_)  \____| (_)  \____|
    ''')
                RCC_Logo()

                def menu():
                    print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> More options are in-development.\n")

                    print(Fore.LIGHTYELLOW_EX+"\n<+>-----------------------<+>\n"
                        " | (1) About RCC           |\n"
                        " |-------------------------|\n"
                        " | (2) Visit RCC on Github |\n"
                        "<+>-----------------------<+>\n")
                menu()
                
                while True:
                    entry = input(Fore.LIGHTYELLOW_EX+"> ")

                    if entry == '1':
                        os.system("cls")
                        change_console_resolution(23, 84)
                        os.system("cls")
                        RCC_Logo()
                        print(Fore.LIGHTYELLOW_EX+"<+>--------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+"                Welcome to RCC!\n"
                            "<+>--------------------------------------------<+>\n"
                            "    RCC is a program developed for customizing\n"
                            "    your roblox client experience, The options\n"
                            "    are provided at the start menu, So choose\n"
                            "    any option you would like to apply!\n"
                            "    Type '?version' to check RCC Version\n"
                            "<+>--------------------------------------------<+>\n")
                        
                        print("                                   ",Fore.BLACK+Back.LIGHTRED_EX+" IMPORTANT NOTE !",Fore.BLACK+Back.BLACK+".")
                        print(Fore.LIGHTYELLOW_EX+"<+>------------------------------------------------------------------------------<+>")
                        print(Fore.LIGHTYELLOW_EX+"     This program is developed only for making roblox client experience better!\n"
                            "            and it's a virus-free not harmful to your system, Thank you!")
                        print(Fore.LIGHTYELLOW_EX+"<+>------------------------------------------------------------------------------<+>")

                        PTC()
                        change_console_resolution(41, 64)
                        os.system("cls")
                        logo()
                        Update()
                        RobloxClientConnectivityChecker()
                        Options()
                        main()
                    
                    elif entry == '2':
                        RCC_GITHUB = "https://github.com/Eagisa/RCC/releases"
                        try:
                            response = requests.head(RCC_GITHUB)
                            if response.status_code == 200:
                                web.open_new_tab(RCC_GITHUB)
                                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ", Fore.LIGHTYELLOW_EX+"> Thank you for visiting the RCC GitHub.\n")
                            else:
                                os.system("cls")
                                RCC_Logo()
                                print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ", Fore.LIGHTYELLOW_EX+"> Error couldn't visit the RCC GitHub\n")
                                PTC()
                        except requests.ConnectionError:
                            os.system("cls")
                            RCC_Logo()
                            print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ", Fore.LIGHTYELLOW_EX+"> No internet , Please check your internet connection!\n")
                            PTC()
                    
                    elif entry == 'clear':
                        os.system("cls")
                        RCC_Logo()
                        menu()
                    
                    elif entry == 'back':
                        change_console_resolution(41, 64)
                        os.system("cls")                 
                        logo()
                        Update()
                        RobloxClientConnectivityChecker()
                        Options()
                        main()

                    else:
                        print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> That was Invailed\n")

            #Close-Program
            elif command == 'exit':
                exit()
            
            elif command == 'clear':
                change_console_resolution(41, 64)
                os.system("cls")
                logo()
                Update()
                RobloxClientConnectivityChecker()
                Options()
                main()
            
            #Version of RobloxClientOptimizer
            elif command == '?version':
                #print("\n  ",Fore.BLACK+Back.LIGHTGREEN_EX+" SYSTEM ",Fore.LIGHTYELLOW_EX+f"> Version: [{RCC_version}] Released: [{RCC_RD}]\n")
                print(Fore.LIGHTYELLOW_EX+"\n           RCC\n"
                    "<+>---------------------<+>\n"
                    " | Version  | "+RCC_version+"      |\n"
                    " |-----------------------|\n"
                    " | Released | "+RCC_RD+" |\n"
                    "<+>---------------------<+>\n")
            else:
                print("\n",Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ",Fore.LIGHTYELLOW_EX+"> That was invailed!\n")

    RemoveAlways()
    #=================================================================================================================================================================================================#