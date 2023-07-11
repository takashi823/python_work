import PySimpleGUI as sg
from goods import *

sg.theme("Dark Blue 3")

layout = [
    [sg.Text("1~7の好きな数字を入力してください"), sg.Text(size=(12, 1), key="-OUTPUT-")],
    [sg.Input(key="-IN-")],
    [sg.Button("Show"), sg.Button("Exit")],
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

window.close()
