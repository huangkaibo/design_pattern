# 纯python风格版本

# 鸭子公共父类
class Duck:
    def __init__(self):
        # python根本不会限制fly_behavior/quack_behavior的类型
        # 只要他们有fly/quack函数就好了
        self.fly_behavior = None
        self.quack_behavior = None

    def swim(self):
        print('Im swimming!')

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

class FlyWithWings:
    def fly(self):
        print('Im flying with wings!')

class CantFly:
    def fly(self):
        print('I cant fly!')

class QuackGuaGua:
    def quack(self):
        print('Gua Gua!')

class QuackZhiZhi:
    def quack(self):
        print('Zhi Zhi!')

class NormalDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = QuackGuaGua()

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = CantFly()
        self.quack_behavior = QuackZhiZhi()

normal_duck = NormalDuck()
rubber_duck = RubberDuck()

normal_duck.swim()
rubber_duck.swim()

normal_duck.fly()
rubber_duck.fly()

normal_duck.quack()
rubber_duck.quack()