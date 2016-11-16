Программа для просмотра файлов на удаленном сервере

Программа просматривает файлы и передает ссылку локальному плееру.

HTTP сервер должен одтавать содержимое в формате json.

Для сервера nginx необходимо в файл /etc/nginx/sites-enabled/default
добавить строки в раздел server:
    autoindex on;
    autoindex_format json;


Для установки tkinter запустить:
sudo apt-get install python3-tk
