classmates = ['Michael', 'Bob', 'Tracy']
# 可以把元素插入到指定的位置，比如索引号为1的位置
classmates.append('Adam')
classmates.insert(7,"hxiaope1")
# 删除
classmates.pop(1)

print(classmates)
print(len(classmates))

# tuple一旦初始化就不能修改
t =(1,2)
print(t)
# 只有1个元素的tuple
t=(2,)
print(t)
# 加List 就可变了
t = ('a', 'b', ['A', 'B'])
t[2].append("c")
print(t)