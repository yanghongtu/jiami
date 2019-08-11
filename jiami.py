'''
贪心学院第一个主题项目代码

写一个加密程序，能够加密的内容是英文和汉字。同时加密并且解密
就是说，一段话中既有中文又有英文，标点符号不用处理。
加密规则，获取ascii码数字，中间用|分割
'''


def jiami(char):
    shuzi = ord(char)
    if 64<shuzi<78 or 96< shuzi <110:
        return chr(shuzi+13)
    elif 77<shuzi<91 or 109<shuzi<123:
        return chr(shuzi-13)
    elif 19967<shuzi<30419:
        return chr(shuzi+10451)
    elif 30418<shuzi<40869:
        return chr(shuzi-10451)
    else:
        return chr(shuzi)


#加密过程
msg = '你好,hello'
result=''
for char in msg:
    result+=str(jiami(char))+'|'
result = result[0:len(result)-1]
print(result)

#解密过程
mingwen=''
for mi in result.split('|'):
    mingwen += jiami(mi)
print(mingwen)