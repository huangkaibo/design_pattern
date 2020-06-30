# 装饰器, 装饰后类就是单例了
def Singleton(cls):
    # 存已new过的类的实例
    instance = {}

    def singleton(*args, **kargs):
        # 没new过就new, 记录下来
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        # 有就返回实例
        return instance[cls]

    return singleton

# 去掉这句话结果不一样
@Singleton
class A(object):
    def __init__(self):
        self.a = None
    
    def fun(self, a):
        self.a = a

a1 = A()
a1.fun(1)
print(a1.a)

a2 = A()
a2.fun(2)
print(a1.a)
print(a2.a)

print(id(a1))
print(id(a2))