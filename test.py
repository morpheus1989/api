
from threading import  Thread


# number=123
#
# class TestThread(Thread):
#
#     def run(self):
#         global number
#         number='abc'
#         print('子线程：',number)
#
#
# td=TestThread()
# td.start()
# td.join()
# print('主线程：',number)

from  werkzeug.local import Local

# from threading import local

# Local线程隔离:thread local对象
local=Local()
# 绑定在local对象上的属性具有线程隔离的特征
local.number=123

class TestThread(Thread):

    def run(self):
        local.number='abc'
        print('子线程：',local.number)


td=TestThread()
td.start()
td.join()
print('主线程：',local.number)