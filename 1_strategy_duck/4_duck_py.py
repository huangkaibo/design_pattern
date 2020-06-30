# 纯python风格版本
import types

# 鸭子公共父类
class Duck:
    def __init__(self, fly_method, quack_method):
        # types.MethodType, 能够将一个外部函数绑定到一个对象或一个类, 成为其内部函数
        # 这样子就可以直接把策略映射进来, 而不用通过一个策略对象来间接调用策略
        # 也就是将变化的函数映射到类外部去动态改变, 很优雅
        self.fly = types.MethodType(fly_method, self)
        self.quack = types.MethodType(quack_method, self)

    def swim(self):
        print('Im swimming!')

    # 这里两个空函数实际可以删了, 无意义了, 上面的就是声明了, 不必再声明
    # def fly(self):
    #     pass

    # def quack(self):
    #     pass

# 策略也不用再是一个类了, 类的话感觉挺怪的
# 一个函数表示一个策略, 就挺好理解了
# 不过类也有类的好处, 比如可以存储些装填, 比如飞行时间/飞行抖动翅膀次数
def fly_with_wings(self):
    print('Im flying with wings!')

def cant_fly(self):
    print('I cant fly!')

def quack_gua_gua(self):
    print('Gua Gua!')

def quack_zhi_zhi(self):
    print('Zhi Zhi!')

class NormalDuck(Duck):
    def __init__(self):
        super().__init__(fly_with_wings, quack_gua_gua)

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(cant_fly, quack_zhi_zhi)

normal_duck = NormalDuck()
rubber_duck = RubberDuck()

normal_duck.swim()
rubber_duck.swim()

normal_duck.fly()
rubber_duck.fly()

normal_duck.quack()
rubber_duck.quack()