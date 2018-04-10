# 猜拳游戏

# 导入random模块
import random

while True:
    num = int(input("请输入： 剪刀(0)  石头（1）  布(2) : "))
    random_num = random.choice(range(3))
    print(f"机器数{random_num}")
    if (num == 0 and random_num == 2) or (num == 1 and random_num == 0) or (num == 2 and random_num == 1):
        print("获胜，您太厉害了！神一般的存在啊！")
        break
    elif (num == 0 and random_num == 1) or (num == 1 and random_num == 2) or (num == 2 and random_num == 0):
        print("哈哈！你输了！")
        break
    else:
        print("平局！")
        break
