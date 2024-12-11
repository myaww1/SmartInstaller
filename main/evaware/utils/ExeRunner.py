import subprocess
import os

class ExeRunner:
    @staticmethod
    def run_exe(exe_path):
        if os.path.exists(exe_path):
            subprocess.run([exe_path], check=True)
        else:
            print(f"Ошибка: {exe_path} не найден.")
