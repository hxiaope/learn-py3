L = ['Bart', 'Lisa', 'Adam']
for it in L:
    print('hello,%s'%it)
acc = 0
n = 1
while n <= 100:
    n = n + 1
    if n==98:
        continue
    acc = acc + n
print(acc)