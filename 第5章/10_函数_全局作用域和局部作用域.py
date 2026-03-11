# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200


def test():
    c = '尚硅谷'
    d = '你好啊'
    global a  # 如果不加这句代码，函数中的a将改变的是自己内部的a，不会改变全局的变量a
    a = 300
    print('函数中的打印a', a)
    print('函数中的打印b', b)
    print('函数中的打印c', c)
    print('函数中的打印d', d)


test()
print('*************************')
print('全局的打印a', a)
print('全局的打印b', b)

# 局部作用域和局部变量，会在函数调用时创建，在函数执行结束后销毁
# 全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
n = 100


def test3():
    global n
    n += 1
    print('我是test3函数中打印的n：', n)


test3()
test3()
test3()
print(n)
