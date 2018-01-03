# a = input("test:")
# if int(a)>50:
#     print(a)
# elif int(a)<50:
#     print(a)
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数

height=1.73
weight=62
bmi=weight/(height*height)
print(bmi)
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
elif bmi>=32:
    print("严重肥胖")