# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
# fruits = ['香蕉', '苹果', '橙子','香蕉']
# result = fruits.index('香蕉')
# print(result)

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
# nums = [10, 20, 10, 30, 10, 40]
# result = nums.count(10)
# print(result)

# 以上二者都是不统计嵌套列表中的元素的

# 3.使用 reverse 方法，对列表进行反转（会改变原列表）。
# nums = [23,11,32,30,17]
# nums.reverse()
# print(nums)

# 4.使用 sort 方法，对列表排序（默认从小到大）（会改变原列表），若想从大到小，可以将 reverse 参数设为True。
# 4.1 若列表中的元素：都是数字，则按照数字的大小顺序进行排序。
# nums = [23, 11, 32, 30, 17]
# nums.sort(reverse=True)
# print(nums)

# 4.2 若列表中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# nums.sort()
# print(nums)

# 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序。
msg_list = ['北京', '尚硅谷', '你好']
msg_list.sort()
print(msg_list)
print(ord('你'), ord('北'), ord('尚'))
