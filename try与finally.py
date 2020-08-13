import time
try:
    f=open('X:\\简明python电子书\\需备份文件.txt')
    while True:
        line=f.readline()
        if line==0:
            break
        time.sleep(2)#请用ctrl+C中止项目跳转结束（时间延迟2秒）
        print(line)
finally:
    f.close()
    print('结束')
