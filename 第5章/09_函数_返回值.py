# 定义一个add函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是{n1 + n2}')


result = add(1, 2)  # 此时返回值是None，因为函数中没有设置返回值


# return关键字：return会结束函数的执行，并把return后的值，作为函数的返回值
def add1(n1, n2):
    return n1 + n2


result1 = add1(1, 2)  # 此时返回值是None，因为函数中没有设置返回值
print(result1)
