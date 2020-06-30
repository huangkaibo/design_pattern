# 通过get的方式来获取类实例

class A(object):
    # 静态成员, 存类实例
    instance = None

    def __init__(self):
        self.a = None

    # 静态函数获取类实例
    @classmethod
    def get_instance(cls, *args, **kargs):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def fun(self, a):
        self.a = a

a1 = A.get_instance()
a1.fun(1)
print(a1.a)

a2 = A.get_instance()
a2.fun(2)
print(a1.a)
print(a2.a)

print(id(a1))
print(id(a2))