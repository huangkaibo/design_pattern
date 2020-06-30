# 方案3需要依靠用户调用get_instance, 但没能阻止用户自行new
# java里通过将构造器私有化实现, 而python实现如下
import threading
from time import sleep

class A(object):
    instance = None
    instance_lock = threading.Lock()

    def __init__(self):
        self.a = None
        sleep(1)

    # python的构造器是__new__, 不是__init__
    # 覆盖构造器, 返回单例即可
    def __new__(cls, *args, **kargs):
        if not cls.instance:
            cls.instance_lock.acquire()
            if not cls.instance:
                # 生成实例不能这样了, 会造成循环调用__new__
                # cls.instance = cls()
                # 而是通过父类__new__来生成实例, 这里的父类就是object
                cls.instance = super().__new__(cls)
            cls.instance_lock.release()
        return cls.instance

    def fun(self, a):
        self.a = a

def f():
    a1 = A()
    a1.fun(1)
    print(id(a1), flush=True)

threads = []
for i in range(10):
    t = threading.Thread(target=f)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()