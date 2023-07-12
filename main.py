import PySimpleGUI as sg
from goods import *

sg.theme("Dark Blue 3")

layout = [
    [sg.Text("1~7の好きな数字を入力してください"), sg.Text(size=(12, 1), key="-OUTPUT-")],
    [sg.Input(key="-IN-")],
    [sg.Button("Show")],
    
### ここから追加
    [sg.Text("追加データを入力してください"), sg.Text(size=(12, 1), key="-OUTPUT-")],
    [sg.Text("商品"),sg.Input(key="-NAME-"),sg.Text("商品コード"),sg.Input(key="-NO-"),],
    [sg.Text(size=(30, 1), key="-COMPLETE-")],
    [sg.Button("Regist"), sg.Button("Exit")],
### ここまで
]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Show":
        goods = Goods()
        goods_info = goods.goods_fetch_id(int(values["-IN-"]))
        id, name, no, created_at = goods_info
        window["-OUTPUT-"].update(name)
### ここから追加
    if event == "Regist":
        goods = Goods()
        goods.goods_insert(values["-NAME-"], values["-NO-"])
        
        window["-COMPLETE-"].update(values["-NAME-"] + 'が追加されました')
### ここまで        
window.close()
