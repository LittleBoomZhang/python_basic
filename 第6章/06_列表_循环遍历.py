score_list = [62, 50, 60, 48, 80, 20, 95]
# while循环遍历
# index = 0
# while index < len(score_list):
#     print(score_list[index])
#     index += 1

# for循环遍历
# 写法一
# for item in score_list:
#     print(item)

# 写法二
# for index in range(len(score_list)):
#     print(score_list[index])

# 写法三
# for index, item in enumerate(score_list):
#     print(index, item)

# enumerate的start参数，可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
for index, item in enumerate(score_list, start=5):
    print(index, item, score_list[0])