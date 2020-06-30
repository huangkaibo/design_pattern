# 3_get_2.py 微调
import threading
from time import sleep

class A(object):
    instance = None
    instance_lock = threading.Lock()

    def __init__(self):
        self.a = None
        sleep(1)

    @classmethod
    def get_instance(cls, *args, **kargs):
        # 加锁是为了避免多个实例同时生成
        # 实例生成后, 是不需要加锁来判断if的
        # 所以多加一步看似冗余的if, 实际只会在一开始生成实例时冗余, 后续这样能减少很多加锁开销
        if not cls.instance:
            cls.instance_lock.acquire()
            if not cls.instance:
                cls.instance = cls()
            cls.instance_lock.release()
        return cls.instance

    def fun(self, a):
        self.a = a

def f():
    a1 = A.get_instance()
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