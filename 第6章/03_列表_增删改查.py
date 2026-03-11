# 新增
# 1. append(元素)--在列表尾部追加一个元素
# nums1 = [10, 20, 30, 40]
# nums1.append(50)
# print(nums1)

# 2. insert(下标, 元素)--在列表指定下标处添加一个元素
# nums2 = [10, 20, 30, 40]
# nums2.insert(2, 666)
# print(nums2)

# 3. extend(可迭代对象)--将可迭代对象中的内容依次取出，追加到列表尾部
# nums3 = [10, 20, 30, 40]
# nums3.extend('尚硅谷')
# nums3.extend(range(1, 4))
# nums3.extend([70, 80, 90])
# print(nums3)


# 删除
# 1. pop(下标)--删除指定位置的元素，并将删除的元素返回
# nums = [10, 20, 10, 40, 50]
# result = nums.pop(1)
# print(nums)
# print(result)

# 2. remove(值)--删除列表中第一次出现的指定值
# nums = [10, 20, 10, 40, 50]
# nums.remove(10)
# print(nums)

# 3. clear()--删除列表中所有的元素（变成一个空列表）
# nums = [10, 20, 10, 40, 50]
# nums.clear()
# print(nums)

# 4. del 列表[下标]--删除指定位置的元素
# nums = [10, 20, 10, 40, 50]
# del nums[3]
# print(nums)

# 修改
# 列表[下标] = 值

# 查询
# 列表[下标]
