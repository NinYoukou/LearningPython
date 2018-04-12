# 宠物类

class Pet(object):
    """一只虚拟宠物"""

    # 定义构造器
    def __init__(self, name, je = 0, wl = 0):   # 公有特性name(名字)、je(饥饿值)、wl(无聊值)
        self.name = name
        self.je = je
        self.wl = wl

    # 定义摸捏时间流逝的方法，由于增加饥饿值、无聊值
    # 因为只需被类的其他方法调用，所有将其私有化
    def __pass_time(self):
        self.je += 1
        self.wl += 1

    # 定义mood属性
    @property
    def mood(self):
        unhappiness = self.je + self.wl
        if unhappiness < 5:
            m = "开心"
        elif unhappiness >= 5 and unhappiness < 10:
            m = "还行"
        elif unhappiness >= 10 and unhappiness < 15:
            m = "焦虑"
        else:
            m = "发疯"
        return m

    # 定义talk方法，和宠物聊天
    def talk(self):
        print(f"主人您好！我是{self.name}, 我现在心情{self.mood}，我很享受和主人聊天的时光。")
        self.__pass_time()

    # 定义eat方法，调用此方法会降低饥饿值，喂养宠物
    def eat(self, food = 4):
        self.je -= food
        print("嗯嗯，好吃，非常美味！delicious！谢谢主人！")
        if self.je < 0:
            self.je = 0
        self.__pass_time()

    # 定义play方法，和宠物玩耍
    def play(self, fun = 4):
        self.wl -= fun
        print("主人，和您玩耍，可以带给我好心情！")
        if self.wl < 0:
            self.wl = 0
        self.__pass_time()


# 程序主体
# 创建main函数
def main():
    pet_name = input("请输入您的宠物名字： ")
    pet1 = Pet(pet_name)

    # 创建菜单系统
    menu_choice = None
    while menu_choice != "0":
        print(
            """
            \t\t饲养宠物游戏\n
            \t0 - 退出
            \t1 - 聊天
            \t2 - 喂养
            \t3 - 玩耍
            """
        )
        menu_choice = int(input("请输入(0-3): "))
        print()

        if menu_choice == 0:
            print("退出游戏，欢迎再次游戏！")
            break
        elif menu_choice == 1:
            pet1.talk()
        elif menu_choice == 2:
            pet1.eat()
        elif menu_choice == 3:
            pet1.play()
        else:
            print("\n您输入的数字无效，请重新输入(0-3)！\n")


# 启动游戏
main()
