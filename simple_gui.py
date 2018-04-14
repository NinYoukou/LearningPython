# 简单GUI程序
# 演示创建窗口

# 导入tkinter模块
from tkinter import *

# 创建根窗体对象，每个Tkinter程序只能有一个根窗体对象
# 如果创建了多个，多个根窗体对象之间会争夺控制权，而使得程序卡住
root = Tk()

# 调用根窗体方法，修改根窗体
root.title("简单的GUI")      # 添加标题
root.geometry("1440x900")    # 设置根窗体大小，单位像素，高度x宽度

# 启动根窗体对象的事件循环，等待处理将要发生的事件
root.mainloop()
