'''
多进程中，同一个变量，各自拷贝一份存在于每个进程中，互不影响，
而在多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改。
线程之间最大的危险在于多个线程同时改进一个变量

'''
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

'''
如果没有锁的话，两条线程t1和t2会同时一存一取，会导致余额不对
为确保balance计算正确，给change_it上一把锁，
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，
获得该锁以后才能改。由于锁只有一个，无论多少线程，
同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现：
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
用try···finnally确保锁一定会释放，
'''
 
'''
锁的优劣：
好处
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处
坏处当然也很多，首先是阻止了多线程并发执行，
包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，
并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，
既不能执行，也无法结束，只能靠操作系统强制终止。
'''