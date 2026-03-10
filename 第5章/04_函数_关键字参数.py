# 关键字参数：调用函数时，通过形参名=值的形式传递实参。
# 混用位置参数和关键字参数时，位置参数必须在关键字参数之前。

def greet(name, gender, age, height):
    print(f'我叫{name},性别{gender},年龄{age},身高{height}cm')


# 调用函数（使用关键字参数）
greet(name='张三', gender='男', height=175, age=35)

# 错误示例
# greet(height=175, age=35, '张三', '男')
