# 仿java版本

# abstract base class抽象基类模块
import abc

# 鸭子公共父类
class Duck(object):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    # 游泳作为不变的特征在父类实现了
    def swim(self):
        print('Im swimming!')

    # 有些鸭子不会飞, 有些会飞
    # 有三种方式
    # 1. 父类实现大多数的, 如会飞, 如果子类特殊的话, 就覆盖
    # 2. 父类只设定空函数, 子类实现
    # 3. 将会变化的飞抽出来, 做成接口和具体实现类, 父类依赖接口, 不依赖实现
    # @abc.abstractmethod
    # 这里的@abc.abstractmethod要不要作用一样, @abc.abstractmethod会限制类称为抽象类
    # 不能new, 且继承他的子类必须实现全部抽象方法
    # 如果不加@abc.abstractmethod就不会这样限制, 可以new, 子类可以只实现部分抽象方法
    def fly(self):
        self.fly_behavior.fly()

    # @abc.abstractmethod
    def quack(self):
        self.quack_behavior.quack()

# 这个就类比java的接口, 接口的概念在python不存在, 在java存在, 下面解释一下为啥
# 以java为例, 接口说到底就是, 我想调用A类的x函数, 也想调用B类的x函数
# 因为java是强类型, 函数参数要写明类型的, 所以只能指定A类型变量.x()或者B类型变量.x()
# 接口的出现就解决了这个问题, A类/B类都继承自同一个接口, 参数类型写接口名, 而不是A类或B类
# 这样子无论传A类还是B类变量, 都能正常调用x()函数
# 但是python不用这样子, python是动态类型, 且函数并不限制参数类型, 所以直接传A变量/B变量都可以正常调用x()函数 (这种设计风格也叫做鸭子类型)
# 所以你看, 其实接口并不是什么很高大上的, 只是由于java语言的局限所必须的补丁
# 所以下面的FlyBehavior/QuackBehavior其实是不必要的, 只是为了模拟java的接口
class FlyBehavior(object):
    # @abc.abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print('Im flying with wings!')

class CantFly(FlyBehavior):
    def fly(self):
        print('I cant fly!')

class QuackBehavior(object):
    # @abc.abstractmethod
    def quack(self):
        pass

class QuackGuaGua(QuackBehavior):
    def quack(self):
        print('Gua Gua!')

class QuackZhiZhi(QuackBehavior):
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