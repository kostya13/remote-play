import requests
import json
import subprocess
from tkinter import *
import urllib

base = 'http://lenovo'
content = []
path = []


def get_content(url):
    content.clear()
    res = requests.get(url)
    text = json.loads(res.text)
    if path:
        content.append({'name': '..', 'type': 'directory'})
    content.extend(text)


def is_directory(item):
    return item['type'] == 'directory'


def full_url():
    return  "{}/{}/".format(base, '/'.join(path))


def fill_listbox():
    for item in content:
        prefix = '+' if is_directory(item) else ''
        listbox.insert(END, prefix + item['name'])


def play(file_name):
    full_path = '{}/{}'.format(full_url(), file_name)
    print(full_path)
    subprocess.call(["mpv", full_path])



def immediately(e):
        index = listbox.curselection()[0]
        item = content[index]
        name = item['name']
        if is_directory(item):
            listbox.delete(0, END)
            if name == '..':
                path.pop()
            else:
                url = urllib.parse.quote(name)
                path.append(url)
            get_content(full_url())
            fill_listbox()
        else:
            if name[-3:].lower() in ('avi', 'mp4', 'mkv'):
                play(name)

master = Tk()
listbox = Listbox(master,height=60,width=500)


def main():
    master.title("Remote play")
    listbox.pack(expand=1)
    listbox.bind('<<ListboxSelect>>', immediately)

    get_content(base)
    fill_listbox()

    mainloop()

if __name__ == '__main__':
    main()
