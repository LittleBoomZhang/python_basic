# 字符串的下标
# msg = 'welcome to atguigu'
# print(msg[3])
# print(msg[-1])

# 字符串中的字符，不可修改
# 字符串不能嵌套

# 常用方法

# index方法：和列表及元组的index方法一致

# split方法：将字符串按照指定字符进行分隔，并返回一个列表。
# msg = '尚硅谷@atguigu@你好'
# result = msg.split('@')
# print(result)

# replace方法：将字符串中的某个字符串片段，替换成目标字符串。
# msg = 'welcome to atguigu'
# result = msg.replace('g', 'G')
# print(result)

# count方法：和列表及元组的count方法一致

# strip方法：从某个字符串中删除指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
# msg1 = '666尚6硅6谷666'
# result1 = msg1.strip('6')
# print(result1)
#
# msg2 = '1234尚12硅34谷4321'
# result2 = msg2.strip('1324')
# print(result2)
#
# msg3 = '34215尚12硅34谷4132'
# result3 = msg3.strip('5432')
# print(result3)
#
# msg4 = '  尚硅谷  '
# result4 = msg4.strip()
# print(msg4)
# print(result4)

# 常用的内置函数 len
# 字符串的循环遍历 与前面的一致