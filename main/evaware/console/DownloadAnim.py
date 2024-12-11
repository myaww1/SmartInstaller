import sys
import time

class DownloadAnim:
    def show_progress_bar(self, percentage):
        bar_length = 50
        block = int(round(bar_length * percentage))
        progress = "█" * block + "-" * (bar_length - block)
        sys.stdout.write(f"\r|{progress}| {int(percentage * 100)}% Загрузка...")
        sys.stdout.flush()

    def animate_download(self):
        for i in range(101):
            self.show_progress_bar(i / 100.0)
            time.sleep(0.05)
        print("\nЗагрузка завершена!")
