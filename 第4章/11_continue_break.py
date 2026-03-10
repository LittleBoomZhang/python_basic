# continue:跳过本次循环剩余语句,随后进入下一次循环
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     continue
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         continue
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         continue
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# break:立即终止循环,不再执行后续循环
for day in range(1, 5):
    print(f'********第{day}天********')
    print('吃饭')
    break
    print('睡觉')

# 注意:continue和break只在自己所在的循环生效
