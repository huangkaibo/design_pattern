# 星巴克, 咖啡分为底料(Espresso/HouseBlend等), 调料(Mocha/Soy/Whip等)
# 需要一个任意搭配和计价的系统

# 底料
# 意式浓咖啡
class Expresso(object):
    def __init__(self):
        self.description = "Expresso"

    def cost(self):
        return 1

# 黑咖啡
class HouseBlend(object):
    def __init__(self):
        self.description = "HouseBlend"

    def cost(self):
        return 2

# 调料
# 摩卡
class Mocha(object):
    # beverage表示饮料
    def __init__(self, beverage):
        self.beverage = beverage
        self.description = self.beverage.description + ", Mocha"
    
    def cost(self):
        return 0.5 + self.beverage.cost()

    # 对于不需要调整的功能, 这样子统一处理, 移交回被装饰者自行处理
    # 当然这里就一个函数cost, 所以这句没用, 如果函数多了, 然而只想修改cost函数, 就有用了
    def __getattr__(self, name):
        return getattr(self.beverage, name)

# 豆浆
class Soy(object):
    def __init__(self, beverage):
        self.beverage = beverage
        self.description = self.beverage.description + ", Soy"
    
    def cost(self):
        return 0.6 + self.beverage.cost()

# 奶泡
class Whip(object):
    def __init__(self, beverage):
        self.beverage = beverage
        self.description = self.beverage.description + ", Whip"
    
    def cost(self):
        return 0.6 + self.beverage.cost()

# 点了杯意式浓咖啡
customer1 = Expresso()
# 加豆浆
customer1 = Soy(customer1)
# 加奶泡
customer1 = Whip(customer1)

# 点了杯黑咖啡
customer2 = HouseBlend()
# 双倍摩卡
customer2 = Mocha(customer2)
customer2 = Mocha(customer2)

print(customer1.description, customer1.cost())
print(customer2.description, customer2.cost())

# 注意所有的底料的对外属性和函数要保持一致, 换成java也就是要继承统一的抽象底料类
# 所有的调料要和底料的对外属性和函数保持一致, 因为装饰器是在不破坏原本功能的基础上拓展功能, 所以爱怎么拓展怎么拓展, 原本的东西不能变
# 所以换成java也就是调料要继承统一的抽象调料类, 抽象调料类要继承自抽象底料类