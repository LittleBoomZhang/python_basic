# /前边只能用位置参数，*后面只能用关键字参数。/必须写在*前面。
def greet(name, /, gender, *, age, height):
    print(f'我叫{name},性别{gender},年龄{age},身高{height}cm')


# 正确示例
greet('张三', '男', age=35, height=175)
