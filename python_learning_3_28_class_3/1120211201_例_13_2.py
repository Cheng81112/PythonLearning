'''
标签示例
'''

from tkinter import *



root = Tk()

lb = Label(
    root,text="我是一个标签",
    bg = "red",
    fg = "white",
    font = ("宋体",24),
    width = 30,
    height = 3,
    relief = SUNKEN)

lb.pack
root.mainloop()
