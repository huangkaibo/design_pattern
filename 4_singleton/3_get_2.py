# 3_get_1.py 多线程不安全, 改造如下
import threading
from time import sleep

class A(object):
    instance = None
    instance_lock = threading.Lock()

    def __init__(self):
        self.a = None
        # 试试去掉lock和sleep, 结果不一样
        sleep(1)

    @classmethod
    def get_instance(cls, *args, **kargs):
        # 多线程不安全其实就是在单次时长较长时(cls()调用__init__, 进而sleep), 可能发生上下文切换
        # 切换后会造成多个线程都通过了if语句, 都生成了各自的类实例
        # 去掉lock再运行试试, 结果不一样
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