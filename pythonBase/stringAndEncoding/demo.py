# str变为bytes
a='ABC'.encode('ascii')
print(a)

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
a = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(a)
a= b'ABC'.decode('ascii')
print(a)