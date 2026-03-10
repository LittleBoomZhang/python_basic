# 前序知识
# 打印默认是换行的
# print('你好', end='\n')
# print('你好', end='')
# print('尚硅谷', end='')

# for循环实现九九乘法表
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={item * row}', end=' ')
    print()
