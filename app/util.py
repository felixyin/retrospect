import random


# 生成六位验证码
def veri_code():
    li = []
    for i in range(6):  # 循环6次,生成6个字符
        r = random.randrange(0, 5)  # 随机生成0-4之间的数字
        # if r == 1 or r == 4:  # 如果随机数字是1或者4时,生成0-9的数字
        num = random.randrange(0, 9)
        li.append(str(num))
        # else:  # 如果不是1或者4时,生成65-90之间的数字
        #     temp = random.randrange(65, 91)
        #     char = chr(temp)  # 将数字转化为ascii列表中对应的字母
        #     li.append(char)
    r_code = ''.join(li)  # 6个字符拼接为字符串
    #  print('\033[31;1m%s\033[0m' % r_code)
    return r_code  # 返回字符串
