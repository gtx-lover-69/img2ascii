import os
from colorama import *
from colorama.ansi import clear_screen
from tqdm import tqdm
import requests
import time

print("Initializing. Sit tight!")

def count_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
       count += len(files)
    return count

total = count_files('C:/Users/')


def download(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            f.write(response.content)

        print("Download successful. Beaming you to the app.")
        return filename

    except requests.RequestException as e:
        print(f"Failed to download: {e}")
        return None

def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

def find(name, path):
    with tqdm(range(total), desc="Searching...", colour="blue") as pbar:
        for root, dirs, files in os.walk(path):
            pbar.update(len(files))
            if name in files:
                pbar.close()
                return os.path.join(root, name)
        return None

def main():
    print("Welcome to Matteo's Utility Suite!")
    selection = input("""    1. FileTool
    2. Music Tool
    3. Img2ASCII
    0. Exit
    """)

    if selection.strip() == "1":
        result = find('filetool.exe', 'C:\\Users\\')
        if result:
            clear_screen()
            print("Found! " + Style.DIM + result + Style.RESET_ALL)
            time.sleep(0.5)
            os.startfile(result)
            exit()

        else:
            clear_screen()
            getFileChoice = input("File not found. Press any key to download it.")
            if getFileChoice or getFileChoice == '':
                print("Downloading from GitHub...")
                filename = download('https://raw.githubusercontent.com/gtx-lover-69/Matteo-CLI-FileTool/main/filetool.exe')

                if filename:
                    time.sleep(0.5)
                    os.startfile(filename)
                    exit()

    elif selection.strip() == "2":
        result = find('musictool.exe', 'C:\\Users\\')
        if result:
            clear_screen()
            print("Found! " + Style.DIM + result + Style.RESET_ALL)
            time.sleep(0.5)
            os.startfile(result)
            exit()
        else:
            clear_screen()
            getFileChoice = input("File not found. Press any key to download it.")
            if getFileChoice or getFileChoice == '':
                print("Downloading from GitHub...")
                filename = download('https://raw.githubusercontent.com/gtx-lover-69/Matteo-CLI-MusicTool/main/musictool.exe')

                if filename:
                    time.sleep(0.5)
                    os.startfile(filename)
                    exit()

    if selection.strip() == "3":
        result = find('img2ascii.exe', 'C:\\Users\\')
        if result:
            clear_screen()
            print("Found! " + Style.DIM + result + Style.RESET_ALL)
            time.sleep(0.5)
            os.startfile(result)
            exit()

        else:
            clear_screen()
            getFileChoice = input("File not found. Press any key to download it.")
            if getFileChoice or getFileChoice == '':
                print("Downloading from GitHub...")
                filename = download('https://raw.githubusercontent.com/gtx-lover-69/img2ascii/main/dist/img2ascii.exe')

                if filename:
                    time.sleep(0.5)
                    os.startfile(filename)
                    exit()

    elif selection.strip() == "0":
        exit()

    else:
        print("Invalid selection. Please try again.")
        time.sleep(1)
        clear_screen()


while __name__ == '__main__':
    clear_screen()
    main()
