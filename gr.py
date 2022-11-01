

from dataclasses import field
from email import message
from email.mime import image
from tkinter import PhotoImage
import facebook as fb
import gspread
gc = gspread.service_account(filename='cre.json')
sh = gc.open('ggls').sheet1
token=""
# print(API.get_object("me"))
# data=API.get_object("me",fields="groups")
# for i in data["groups"]["data"]:
    # print(i["id"])
data_post=sh.acell('A1').value
API.put_object(parent_object="8375280285877298",connection_name="feed",message=data_post)
print("đã đăng")
