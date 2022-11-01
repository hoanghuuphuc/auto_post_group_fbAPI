

from dataclasses import field
from email import message
from email.mime import image
from tkinter import PhotoImage
import facebook as fb
import gspread
gc = gspread.service_account(filename='cre.json')
sh = gc.open('ggls').sheet1
token="EAAMJ1NPc1vUBAD3jZCVaa8s1yfLyfZCH6XKzlvCNZBddEruQ7x1XlaSZATpnmLJOME0d9ZBMDzKt1LIwH6BW0eEdGkZBpj2VkqKgxAa66qVcgM15ptdWoZAf4QTPZBDeqV6H1JBW5JStgOb0nRC1CFVaVHT7xXSpbvC2iYAgFxZCPzNM7MWAy6C4WAASirBOgXo43jEQVVX0E4OV9AIV5gXHLpuOskz8MwBVHjac69CpxF4NqILotySre"
API=fb.GraphAPI(token)
# print(API.get_object("me"))
# data=API.get_object("me",fields="groups")
# for i in data["groups"]["data"]:
    # print(i["id"])
data_post=sh.acell('A1').value
API.put_object(parent_object="8375280285877298",connection_name="feed",message=data_post)
print("đã đăng")