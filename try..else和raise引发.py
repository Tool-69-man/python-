class InputPro(Exception):
    def __init__(self, length, least):
        Exception.__init__(self)
        self.length = length
        self.least = least
try:
    s = input('输入')
    if len(s) < 3:
        raise InputPro(len(s), 3)

except EOFError:
    print('输入错误')
except InputPro:
    # print('len=%d 最少应该%d') % (InputPro.lenght, InputPro.least )
    print(InputPro.length, InputPro.least)
else:
    print('正常运行')


