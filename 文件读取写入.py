f = open(r'X:\简明python电子书\需备份文件.txt')#默认是可读方式
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()
poem = '''
过河拆桥
        顺手牵羊
                万箭齐发
                        南蛮入侵
                                无中生有
                                        ......
'''
f = open(r'X:\简明python电子书\需备份文件.txt','r+')#文件打开方式 w,a 可写不可读   r+可读写
f.write(poem)
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()
# f = open(r'X:\简明python电子书\需备份文件.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line)
# f.close()
