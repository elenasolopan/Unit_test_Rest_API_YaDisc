import requests


class YaDiscUser:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.put(url, headers=self.headers, params={'path': folder_name})

        if res.status_code == 201:
            print(f'Папка "{folder_name}" успешно создана')
            return res.status_code

        elif res.status_code == 409:
            print(f'Папка {folder_name} уже существует')
            return res.status_code

        elif res.status_code == 401:
            print('Не авторизован')
            return res.status_code


def execute_upload():
    ya_disc_client = YaDiscUser(input("\nВведите токен пользователя YandexDisc: "))
    ya_folder = input('ВВедите название новой папки на ЯндексДиске: ')
    create_folder_status = ya_disc_client.create_folder(ya_folder)
    print(create_folder_status)
    return create_folder_status, True


if __name__ == '__main__':
    execute_upload()
