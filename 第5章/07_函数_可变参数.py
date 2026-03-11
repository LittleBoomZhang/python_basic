# 可变位置参数
# 定义函数时，在形参名前加*，可以接收任意数量的位置参数，并打包成一个元组。
def test1(*args):
    print(args)


test1('张三', '男', 35, 175)


# ('张三', '男', 35, 175)--这种数据就叫元组

# 可变关键字参数
# 定义函数时，在形参名前加**，可以接收任意数量的关键字参数，并打包成一个字典。
def test2(**kwargs):
    print(kwargs)


test2(name='张三', gender='男', age=35, height=175)


# {'name': '张三', 'gender': '男', 'height': 175, 'age': 35}--这种数据就叫字典

# 可变位置参数、可变关键字参数，可以同时使用，但必须先写可变位置参数
def test3(*args, **kwargs):
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(args)
    print(kwargs)


test3('张三', '男', age=35, height=175)


# 可变位置参数、可变关键字参数，也能与其他类型的参数一起使用
def test4(a, b, *args, c='尚硅谷', **kwargs):
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


test4('张三', '男', '抽烟', '喝酒', c='亚克西', age=35, height=175)
