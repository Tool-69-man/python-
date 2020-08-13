import random
result=random.randint(1,10)
print(result)
guess=input("请猜一下我心里的数字\n")
while True:
    num=int(guess)
    if num==result:
        print('猜对了，恭喜！')
        break;
    else:
        if num>result:
            print('猜大了')
        else:
            print('猜小了')
    guess=input('猜错了，重猜吧\n')  
print('游戏结束\n')
