#global X 声明全局
def fun():
    #print('一开始的x',x)
    global x
    x=212
    print('全局变量x',x)
x=111

fun()
print(x)
x=555

def  fun1(x):
    print('输出fun后x',x)
    x=12
    print('局部变量12',x)


fun1(x)

print('最后显示全局',x)
