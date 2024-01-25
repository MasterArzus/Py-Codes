import tkinter as tk
# from tkinter import filedialog
from tkinter.filedialog import *


def openFile():
    filepath = askopenfilename()  # 选择打开什么文件，返回文件名
    if filepath.strip() != '':
        filename.set(filepath)  # 设置变量filename的值
    else:
        print("do not choose file")


def openDir():
    fileDir = askdirectory()  # 选择目录，返回目录名
    if fileDir.strip() != '':
        dirpath.set(fileDir)  # 设置变量outputpath的值
    else:
        print("do not choose Dir")


def fileSave():
    filenewpath = asksaveasfilename(defaultextension='.txt')  # 设置保存文件，并返回文件名，指定文件名后缀为.txt
    if filenewpath.strip() != '':
        filenewname.set(filenewpath)  # 设置变量filenewname的值
    else:
        print("do not save file")


root = tk.Tk()
root.title("fileDialog示例")
root.geometry("500x300")

filename = tk.StringVar()
dirpath = tk.StringVar()
filenewname = tk.StringVar()

# 打开文件
tk.Label(root, text='选择文件').grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=filename, width=40).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='打开文件', command=openFile).grid(row=1, column=2, padx=5, pady=5)

# 选择目录
tk.Label(root, text='选择目录').grid(row=2, column=0, padx=5, pady=5)  # 创建label 提示这是选择目录
tk.Entry(root, textvariable=dirpath, width=40).grid(row=2, column=1, padx=5, pady=5)  # 创建Entry，显示选择的目录
tk.Button(root, text='打开目录', command=openDir).grid(row=2, column=2, padx=5, pady=5)  # 创建一个Button，点击弹出打开目录窗口

# 保存文件
tk.Label(root, text='保存文件').grid(row=3, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=filenewname, width=30).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text='点击保存', command=fileSave).grid(row=3, column=2, padx=5, pady=5)

root.mainloop()