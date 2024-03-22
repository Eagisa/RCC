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
#RCC_CBS Version
#=========================#
RCC_CBS_Ver = "100.3.3.5"
#=========================#

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

change_console_resolution(20, 64)

#=============================================================================#
RCC_S = "https://raw.githubusercontent.com/Eagisa/RCC/main/RCC-Ss/RCC-S.json"
#=============================================================================#

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

logo()


def PTC():
    msvcrt.getch()

def RCC_Updater():
    # Function to download a file from a URL
    def download_file(url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)

    # Fetching JSON data from the URL
    url = RCC_S
    response = requests.get(url)
    data = response.json()

    # Getting the version of RCC-C from the JSON object
    rcc_c_version = data.get("RCC-C", {}).get("Version")

    local_appdata = os.getenv('LOCALAPPDATA')
    pyc_file_path = os.path.join(local_appdata, 'RCC', 'RCCMP.py')
    spec = importlib.util.spec_from_file_location("RCCMP", pyc_file_path)
    RCCMP = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RCCMP)

    RCC_ver = RCCMP.RCC_version

    debug = False
    # Checking if the version matches
    if not rcc_c_version == RCC_ver and not debug:
        os.system("cls")
        change_console_resolution(20, 64)
        logo()
        print("\n", Fore.BLACK+Back.LIGHTGREEN_EX+" R.C.C ", Fore.LIGHTYELLOW_EX+"> Updating RCC...\n")
        updater_info = data.get("RCC-FS", {}).get("RCCMP")
        if updater_info:
            file_url = updater_info
            filename = os.path.basename(file_url)
            local_app_data_folder = os.path.join(os.environ["LOCALAPPDATA"], "RCC")
            destination_path = os.path.join(local_app_data_folder, filename)
            download_file(file_url, destination_path)
            os.system("cls")
            logo()
            print("\n", Fore.BLACK + Back.LIGHTGREEN_EX + " R.C.C ", Fore.LIGHTYELLOW_EX + "> You're up to date!\n")
            time.sleep(1.5)
            RCCMP.StartRCC()
    else:
        RCCMP.StartRCC()