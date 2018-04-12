# 练习类特性和静态方法

class Pet(object):
    """ 一个虚拟宠物 """
    # 定义一个类特性
    # 这条赋值语句只会被执行一次
    # 在Python发现类定义时，就已经被创建，不管是否定义对象
    # 类特性通过点运算符来访问的
    total = 0

    # 定义一个静态方法，记录创建的宠物总数
    @staticmethod
    def pet_total():
        print(f"\n到目前为止，已经有{Pet.total}个宠物诞生了。") # 在类的内部，通过Pet.total来调用类特性

    # 创建构造器
    def __init__(self, name):
        print("一个宠物诞生了。")
        self.name = name

        # 调用类特性，将宠物总数加一
        Pet.total += 1

# 程序主体
print(f"查看宠物总数： {Pet.total}")   #在外部直接调用类特性

print("现在开始饲养宠物")
cat = Pet("猫熊")
dog = Pet("旺财")
horse = Pet("赤兔马")

# 在外部通过静态方法调用类特性
Pet.pet_total()

# 通过对象调用类特性
print(dog.total)
