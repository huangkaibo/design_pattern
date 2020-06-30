# 通过python的元类实现, 使用很简单, 原理很复杂, 没看也不解释, 只列出来
from time import sleep

class SingletonType(type):
    instance = None

    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance

# 只需要继承元类, 其他啥也不需要添加, 入侵非常小, 可以忽略不计
class A(metaclass=SingletonType):
    def __init__(self):
        self.a = None
        sleep(1)

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