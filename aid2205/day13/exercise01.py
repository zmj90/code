"""
    架构设计思想练习:
        手雷爆炸,可能伤害玩家、敌人.
            玩家受伤后闪现红屏
            敌人受伤后头顶爆字
            还有可能伤害其他目标...
        要求:增加新目标,手雷代码不变.
        提示：先画出架构设计图
"""


class Grenade:
    def explode(self, target):
        if isinstance(target,AttackTarget):
            print("爆炸")
            # 编码时调用父类AttackTarget
            # 运行时执行子类Player、Enemy
            target.damage()


class AttackTarget:
    def damage(self):
        pass


# -----------------
class Player(AttackTarget):
    def damage(self):
        print("闪现红屏")


class Enemy(AttackTarget):
    def damage(self):
        print("头顶爆字")


# -----------------
grenade = Grenade()
grenade.explode(Player())
grenade.explode(Enemy())
grenade.explode("玩家")
