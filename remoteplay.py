import requests
import json
from tkinter import *
import urllib

base = 'http://localhost'
content = []


def get_content(url):
    content.clear()
    res = requests.get(url).text
    print(res)
    res = json.loads(res)
    content.extend(res)
    print(url, content)

def is_directory(item):
    return item['type'] == 'directory'

def fill_listbox():
    for item in content:
        prefix = '+' if is_directory(item) else ''
        listbox.insert(END, prefix + item['name'])

def immediately(e):
        index = listbox.curselection()[0]
        item = content[index]
        if is_directory(item):
            listbox.delete(0, END)
            url = urllib.parse.quote(item['name']) 
            full_url = "{}/{}/".format(base, url)
            get_content(full_url)
            fill_listbox()


master = Tk()
listbox = Listbox(master,height=40,width=500)
listbox.pack(expand=1)
listbox.bind('<<ListboxSelect>>', immediately)

get_content(base)
fill_listbox()

mainloop()
