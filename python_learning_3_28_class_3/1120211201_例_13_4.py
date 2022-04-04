'''
用grid()方法排列标签
方法grid()是基于网格的布局。先虚拟一个二维表格，再在该表格中布局控件实例。
由于在虚拟表格的单元格中所布局的控件实例大小不一，单元格也没有固定或均一的大小，
因此其仅用于布局的定位。grid()方法与pack()方法不能混合使用。
column：控件实例的起始列，最左边为第0列。
columnspan：控件实例所跨越的列数，默认为1列。
row：控件实例的起始行，最上面为第0行。
rowspan：控件实例所跨越的行数，默认为1行。
'''

from tkinter import *
root = Tk()
lbred = Label(root, text= "红", fg= "red" ,relief=GROOVE)
lbred.grid(column=2,row=0)
lbgreen = Label(root, text= "绿", fg="green",relief= GROOVE)
lbgreen.grid(column=0,row=1)
lbblcak = Label(root, text= "黑", fg= "black" ,relief= GROOVE)
lbblcak.grid(column=1,row= 1)
lbblue = Label(root, text= "蓝蓝", fg="blue" ,relief=GROOVE)
lbblue.grid(column=1,columnspan=2,row=2)
root.mainloop()
