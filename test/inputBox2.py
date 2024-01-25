import os
import tkinter
from tkinter import filedialog
from tkinter.messagebox import showwarning, showinfo


def Input_Key():
    # 初始化弹出输入对话框
    child = tkinter.Tk()
    # 弹出对话框的title
    child.title('文件加密和解密的秘钥值')
    child['height'] = 110
    child['width'] = 320
    child.resizable(0, 0)
    # 设置弹出对话的框的标签值
    label = tkinter.Label(child, text='秘钥值:', font=('黑体', 12))
    label.place(x=1, y=17)
    # 弹出输入对话框请获取相应的值
    digit_str = tkinter.StringVar()
    entry = tkinter.Entry(child, font=('黑体', 12), textvariable=digit_str)
    entry.place(x=100, y=17)

    # 绑定回车键
    def Get_key(*args):
        global key
        key = entry.get()
        if not key:
            key = '123'
            showinfo(title='警告', message='系统默认秘钥值')
        child.destroy()

    # 按下回车键返回秘钥
    child.bind('<Return>', Get_key)
    # 点击OK按钮返回秘钥
    btn_OK = tkinter.Button(child, text='OK', font=('黑体', 12), height=1, command=Get_key)
    btn_OK.place(x=150, y=50)
    child.mainloop()
    print('key: ', key)
    return key
