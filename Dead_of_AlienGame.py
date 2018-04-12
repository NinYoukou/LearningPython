# Alien Blaster
# 练习对象之间的交互

# 定义Player类
class Player(object):
    """ A player in a shooter game. """
    def blast(self, enemy):
        print("玩家攻击入侵者！\n")
        enemy.die()

# 定义Alien类
class Alien(object):
    """ An alien in a shooter game. """
    def die(self):
        print(r'这外星人边逃跑边说："呕，地球人太厉害了，饶恕我的任性吧！再见，宇宙！"')

# 程序主体
print("\t\t外星人之死游戏\n")

hero = Player()
invader = Alien()
# 英雄对外星人进行攻击
hero.blast(invader)

input("\n\nPress the enter key to exit.")
