import os
import time
from main.evaware.utils.GraphicsData import GraphicsData

class ExitHandler:
    @staticmethod
    def exit_program():
        os.system("cls" if os.name == "nt" else "clear")
        print(GraphicsData.get_ascii_art())
        print("Выход через 3 секунды...")
        time.sleep(3)
