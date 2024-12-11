import requests
import zipfile
import os
import shutil
import sys

class VersionInstaller:
    @staticmethod
    def install_version(temp_dir, target_dir):
        version_url = "https://download946.mediafire.com/6542bosfoftg0WjBOWAwpe_rtMB8L6qeWsZVtAzlTLnf-dJ7UH2pfK8h3_k1KRyCBnAVKQhnJhRX5qRgzTmoAuMvBpmDhfp_rvcM1H__isuXdzstqkhUoQTtl-Yo6_vjqqon-VsvKnSv1XkQQOsTFHEeL8cS-hOuUGm8ptVYPB4s/bze8gh38s58e38h/Evaware.zip"
        zip_path = os.path.join(temp_dir, "Evaware.zip")

        print(f"Путь для скачивания файла: {zip_path}", end="")
        sys.stdout.flush()

        if not os.path.exists(temp_dir):
            print(f"Ошибка: папка {temp_dir} не существует!", end="")
            sys.stdout.flush()
            return

        try:
            response = requests.get(version_url, stream=True)

            if response.status_code == 200:
                print("\nНачинаю скачивание...", end="")
                sys.stdout.flush()
                total_length = int(response.headers.get('Content-Length'))

                with open(zip_path, "wb") as zip_file:
                    downloaded = 0
                    for chunk in response.iter_content(chunk_size=8192):
                        downloaded += len(chunk)
                        zip_file.write(chunk)

                        percent = downloaded / total_length * 100
                        print(f"\rСкачивание: {percent:.2f}% ", end="")
                        sys.stdout.flush()

                print("\nСкачивание завершено.", end="")
                sys.stdout.flush()
            else:
                print(f"Ошибка: сервер вернул статус {response.status_code}.", end="")
                sys.stdout.flush()
                return

            # Проверка размера скачанного файла
            if os.path.getsize(zip_path) == 0:
                print("Ошибка: файл пустой.", end="")
                sys.stdout.flush()
                return

            print(f"Размер скачанного файла: {os.path.getsize(zip_path)} байт.", end="")
            sys.stdout.flush()

            # Распаковка архива
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
            print("Архив успешно распакован.", end="")
            sys.stdout.flush()

            extracted_folder = os.path.join(temp_dir, "Evaware")
            if os.path.exists(extracted_folder):
                shutil.move(extracted_folder, target_dir)
                print("Файлы успешно перемещены.", end="")
                sys.stdout.flush()
            else:
                print("Ошибка: папка Evaware не найдена после распаковки.", end="")
                sys.stdout.flush()

        except Exception as e:
            print(f"Произошла ошибка: {e}", end="")
            sys.stdout.flush()

        finally:
            if os.path.exists(zip_path):
                os.remove(zip_path)
                print("\nУдаление временного архива завершено.", end="")
                sys.stdout.flush()
