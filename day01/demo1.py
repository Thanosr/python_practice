"""
## 占位符
尼玛 这个几把玩意我再记不住我就去吃屎！！！！！

%d 整数的占位符
%f 小数的占位符
%% 表示百分号

"""

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

"""
变量中存储的是内存中的地址、地址、地址！！！！！
"""
# a = 10
# b = 20
# a += b
# print(a)
# a *= a+2
# print(a)


"""
比较、逻辑和算身份运算符的使用

"""

# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not (1 != 2)
# print('flag0 =', flag0) # flag0 = True
# print('flag1 =', flag1) # flag1 = True
# print('flag2 =', flag2) # flag2 = False
# print('flag3 =', flag3) # flag3 = False
# print('flag4 =', flag4) # flag4 = True
# print('flag5 =', flag5) # flag5 = False
# print(flag1 is True) # True
# print(flag2 is not False) # False

# year = int(input("请输入你需要查询的月份:"))

# is_leap = (year % 4 == 0 and year % 100 != 0) or \
#           year % 400 == 0
# print(is_leap)



"""
分支结构
（python中的代码是一条一条执行的，这种结构为顺序结构）
用户身份验证
"""
## 用户验证
# username = input("请输入您的用户名")
# password = input("请输入您的密码")
#
# if username == 'lin' and password == '123':
#     print("验证通过！")
# else:
#     print("验证失败！")

## 分段函数求值

x = float(input('您输入的x = '))

if x > 1:
    y = 3 * x - 5
elif x>=-1:
    y = x + 2
else:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))






