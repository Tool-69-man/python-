import random
num=random.randint(1,10)
print(num)

status=True
while status:
    guess=int(input('请输入你猜想的数字:\n'))
    if guess==num:
        print('猜对了')
        status=False
    elif guess>num:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('循环结束')
print('游戏结束')
