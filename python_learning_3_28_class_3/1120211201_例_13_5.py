'''
使用configure函数

'''
import tkinter
import time
def gettime():
    # 获取当前时间并转化为字符串
    timestr = time.strftime("%H:%M:%S")
    # 重新设置标签文本
    lb.configure(text=timestr)
    # 每隔1秒调用函数gettime自身获取时间
    root.after(1000,gettime)
root = tkinter.Tk()
root.title("时钟")

lb = tkinter.Label(root, text='', fg = 'black', font = ('黑体', 80))
lb.pack()
gettime()
root.mainloop()