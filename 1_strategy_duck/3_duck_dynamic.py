# 纯python风格版本

class Duck:
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    def swim(self):
        print('Im swimming!')

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

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
        pass

class RubberDuck(Duck):
    def __init__(self):
        pass

normal_duck = NormalDuck()
# 原来在NormalDuck/RubberDuck的init里初始化fly_behavior和quack_behavior, 不好就是运行时无法变更(当然你硬要说修改self.fly_behavior也行)
# 建立一个setter, 运行时去set, 就能支持运行时调整而不是一开始就固化了
# 这样做的好处是behavior被进一步抽出来, 可以随时调整behavior, 比如这只NormalDuck明天翅膀断了
# 我就可以normal_duck.set_fly_behavior(CantFly()), 调整behavior
# 实际上, 这就是一个设计模式了, 叫做策略模式
# 每一种飞行方式/叫方式, 都是一种策略, 抽出到用户层, 用户运行时可以随时修改策略
# 这就是策略模式的好处
# 举个例子: 一个地图导航应用, 一开始是为了一个小公园做的, 所以就是步行导航
# 后来公园扩建大了一点, 需要自行车导航了, 再后来又扩建成了森林公园, 需要公交和汽车导航了
# 如果一开始能采用这种策略模式, 那么后续可以随意增加交通工具, 只需要定义一个新的类
# setter设置导航方式为这种类导航, 就OK了, 无需任何变更
# 要不然想象会多麻烦, 最low的, 需要把初期的代码加上 if method == '步行', 后续的交通工具, 添加elif method == 'xxx', 然后复制一份代码
# 更麻烦的是, 原先也没有设定交通工具这个变量, 所以还得想想怎么把交通工具作为变量传进下一层
normal_duck.set_fly_behavior(FlyWithWings())
normal_duck.set_quack_behavior(QuackGuaGua())

rubber_duck = RubberDuck()
rubber_duck.set_fly_behavior(CantFly())
rubber_duck.set_quack_behavior(QuackZhiZhi())

normal_duck.swim()
rubber_duck.swim()

normal_duck.fly()
rubber_duck.fly()

normal_duck.quack()
rubber_duck.quack()