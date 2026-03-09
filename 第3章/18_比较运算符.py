# 注意下述情况，字符串比较时
msg1 = 'abc'
msg2 = 'xyz'
msg3 = '我爱你'
msg4 = '中国'
print(msg3 > msg4)
# Python中字符串之间进行比较时，是依次比较每个字符的Unicode编码。

# 使用ord()查看指定字符的Unicode编码
print(ord('a'))
print(ord('我'))

# 使用chr()将Unicode编码转为字符
print(chr(97))
print(chr(25105))

# 注意下列比较,这种情况相同的abc比较完后，直接比较长度
msg5 = 'abc'
msg6 = 'abcdef'
print(msg5 > msg6)
