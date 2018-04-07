from tkinter import *
import psutil
from time import sleep
import threading

master = Tk()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()


def data():
    while True:
        cpu_p = psutil.cpu_percent(interval=1, percpu=True)  # 读取CPU使用率
        mem_t = psutil.virtual_memory().total/1024/1024/1024  # 全部内存
        mem_t = round(mem_t, 2)  # 取两位小数
        mem_u = psutil.virtual_memory().used/1024/1024/1024  # 已使用内存
        mem_u = round(mem_u, 2)
        mem_p = psutil.virtual_memory().percent  # 读取内存使用率
        t3.set(cpu_p)
        tt = str(mem_u)+"GB / "+str(mem_t)+"GB("+str(mem_p)+"%)"
        t4.set(tt)
        net_in = psutil.net_io_counters().bytes_recv/1024/1024
        net_in = round(net_in, 2)
        net_out = psutil.net_io_counters().bytes_sent/1024/1024
        net_out = round(net_out, 2)
        net = str(net_in)+"MB / "+str(net_out)+"MB"
        t5.set(net)
        disk_u = psutil.disk_usage("/").percent
        disk_u = str(disk_u)+"%"
        t6.set(disk_u)
        sleep(0.5)


master.title("资源监控")  # 窗口标题
master.geometry("300x150+100+100")  # 窗口呈现大小和位置
cpu_logical = psutil.cpu_count()  # 读取CPU线程数
cpu_physical = psutil.cpu_count(logical=False)  # 读取CPU核心数
Label(master, textvariable=t1).grid(row=0, column=0)
t1.set(cpu_physical)
Label(master, text="核").grid(row=0, column=1)
Label(master, textvariable=t2).grid(row=0, column=2)
t2.set(cpu_logical)
Label(master, text="线程").grid(row=0, column=3)
Label(master, text="CPU使用率：").grid(row=1, column=0, columnspan=4)
Label(master, textvariable=t3).grid(row=1, column=4)
Label(master, text="内存使用率：").grid(row=2, column=0, columnspan=4)
Label(master, textvariable=t4).grid(row=2, column=4)
Label(master, text="网络(下/上)：").grid(row=3, column=0, columnspan=4)
Label(master, textvariable=t5).grid(row=3, column=4)
Label(master, text="硬盘使用率：").grid(row=4, column=0, columnspan=4)
Label(master, textvariable=t6).grid(row=4, column=4)
th1 = threading.Thread(target=data)
th1.setDaemon(True)  # 守护线程
th1.start()
master.mainloop()
print("END!")
