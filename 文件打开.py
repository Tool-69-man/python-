f = open(r'X:\简明python电子书\需备份文件.txt')
while True:
    line=f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()
