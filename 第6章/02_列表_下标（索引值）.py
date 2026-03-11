nums = [1, 2, 3, 4, 5]
# 正索引，从左到右，起始元素是0，随后是1，依次类推
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
# 负索引，从右到左，起始元素是-1，随后是-2，依次类推
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

# 定义一个嵌套列表
nums2 = [10, 20, ['你好啊', '尚硅谷'], 40, 50]
# 取出“尚硅谷”
print(nums2[2][1])
