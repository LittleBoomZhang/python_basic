# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
# print(int(True))
# print(int(False))

# print(4 + True)
# print(8 - False)

# print(True + True)
# print(True - False)

# print(7 > True)
# print(False <= 0)

# 使用bool()将指定内容转为布尔类型
# print(bool(1))
# print(bool(0))

# Python中除了0以外的任何数,转为布尔值后都为True
# print(bool(300))
# print(bool(25.6))
# print(bool(1.8e3))
# print(bool(12_000))
# print(bool(-10))

# Python中除空字符串以外的任何字符串,转为布尔值都是True
print(bool('hello'))
print(bool('0'))
print(bool('18.5'))
print(bool('-9'))
print(bool(''))
