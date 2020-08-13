import sys
try:
    s = input('请输入任意')
except EOFError:
    print('输入错误')
    sys.exit()
except:
    print('什么都没')
print('end')
