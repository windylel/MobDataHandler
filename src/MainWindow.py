#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'SenTR'

from Tkinter import *           # 导入 Tkinter 库
import tkMessageBox


root = Tk()
root.geometry('600x400')

beginLabel = Label(root, text="开始时间", fg="black")
beginLabel.pack(padx=5, pady=10, side=LEFT)

beginInput = Label(root, text="Green Grass", bg="green", fg="black")
beginInput.pack(fill=X, padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X, padx=10)
mainloop()