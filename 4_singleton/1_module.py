# python的模块import是天生的单例, 由python自身实现
# 所以可以取巧利用这一点来实现单例

class A(object):
    def fun(self):
        pass

a = A()

# 其他文件的代码需要的时候import即可得到单例
# from 1_module import a

# https://www.cnblogs.com/huchong/p/8244279.html