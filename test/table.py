from tkintertable import TableCanvas, TableModel
from tkinter import *
import tkinter
import random
import time
import threading


def update(table):
    while True:
        time.sleep(1)
        # cols = table.model.columnNames  # get the current columns
        data["row1"]["col2"] = random.random()  # use row and column names, not cell coordinates
        # table.model.setValueAt(value, rowindex, colindex)  ##use cell coords
        data["row1"]["col1"] = ""  # use row and column names, not cell coordinates
        table.redrawTable()


def monitor(master, table):
    master.after(100, update(table))


if __name__ == '__main__':
    master = tkinter.Tk()  # 主窗口
    master.geometry('600x400')

    tframe = Frame(master)  # 子窗口
    tframe.pack()  # 布局

    data = {'row1': {'col1': '', 'col2': '状态1', 'col3': '状态2', 'col4': '状态3', 'col5': '状态4'},
            'row2': {'col1': '眉毛', 'col2': 'b1', 'col3': 'b2', 'col4': 'b3', 'col5': '/'},
            'row3': {'col1': '眨眼', 'col2': 'e1', 'col3': 'e2', 'col4': 'e3', 'col5': '/'},
            'row4': {'col1': '嘴巴', 'col2': 'm1', 'col3': 'm2', 'col4': '/', 'col5': '/'},
            'row5': {'col1': '头部姿态', 'col2': 'h1', 'col3': 'h2', 'col4': 'h3', 'col5': 'h4'},
            # 'row5': {'头部姿态': "", 'col2': 108.79, 'label': '2'}
            }

    table = TableCanvas(tframe, data=data)  # table组件挂载到frame子窗口上
    table.show()

    # 主进程运行master，子线程运行更新代码
    t1 = threading.Thread(target=update, args=(table,))  # 更新数据
    t2 = threading.Thread(target=monitor, args=(master, table))  # 监听数据并修改表格
    t1.start()
    t2.start()
    master.mainloop()
