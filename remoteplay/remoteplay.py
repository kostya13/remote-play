#!/usr/bin/python3.5
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


def is_video_file(name):
    return name[-3:].lower() in ('avi', 'mp4', 'mkv')


def full_url():
    return "{}/{}/".format(base, '/'.join(path))


def fill_listbox():
    for item in content:
        prefix = '+' if is_directory(item) else ''
        listbox.insert(END, prefix + item['name'])


def play(file_names):
    to_play = []
    for file_name in file_names:
        full_path = '{}/{}'.format(full_url(), file_name)
        to_play.append(full_path)
    print(to_play)
    subprocess.Popen(["mpv", "--fs"] + to_play)


def immediately(e):
        index = listbox.curselection()[0]
        item = content[index]
        name = item['name']
        if is_directory(item):
            button['state'] = 'disabled'
            listbox.delete(0, END)
            if name == '..':
                path.pop()
            else:
                url = urllib.parse.quote(name)
                path.append(url)
            get_content(full_url())
            fill_listbox()
        else:
            if is_video_file(name):
                button['state'] = 'normal'
            else:
                button['state'] = 'disabled'


def send_to_player():
    names = []
    for index in listbox.curselection():
        item = content[index]
        name = item['name']
        if is_video_file(name):
            names.append(name)
    if names:
        play(names)


master = Tk()
listbox = Listbox(master, height=60, width=500, selectmode=EXTENDED)
button = Button(master, text='Посмотреть', command=send_to_player)


def main():
    master.title("Удаленный проигрыватель")
    button.pack(fill='x', expand=1)
    button['state'] = 'disabled'
    listbox.pack(expand=1)
    listbox.bind('<<ListboxSelect>>', immediately)

    get_content(base)
    fill_listbox()

    mainloop()

if __name__ == '__main__':
    main()
