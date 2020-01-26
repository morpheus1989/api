import memcache

# 开启debug模式，可以查看详细报错信息
# 连接前先启动memcache
# ['ip1:port','ip2:port',....]如果里面有多个连接就构成了分布式存储
mc=memcache.Client(['127.0.0.1:11211'],debug=True)

# time默认为0，意味着永久存储，不建议使用。及时释放内存
# mc.set('user','李寻欢1',time=120)
print(mc.get('user'))

# 一次存储多个键值对
mc.set_multi(dict(name='哈利波特',age=18),time=60*2)
print(mc.get('age'))
# 自增加/减少【默认为1】阅读数/浏览量
mc.incr('age',delta=10)
print(mc.get('age'))