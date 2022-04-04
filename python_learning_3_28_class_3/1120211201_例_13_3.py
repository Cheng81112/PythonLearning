'''
用pack()方法不加参数排列标签
方法pack()是一种简单的布局方法，如果用不加参数的默认方式，将按布局语句的先后，以最小占用空间的方式自上而下地排列控件实例，并且保持控件本身的最小尺寸
'''
from tkinter import *
root = Tk()

lbred = Label(root, text= "Red", fg="red",relief=GROOVE)
lbred.pack()
lbgreen = Label(root, text= "绿色", fg="green",relief=GROOVE)
lbgreen.pack()
Ibblue = Label(root, text= "蓝", fg= "blue",relief=GROOVE)
Ibblue.pack()
root.mainloop()