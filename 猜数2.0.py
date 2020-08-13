guess=input("请猜一下我心里的数字\n")
num=int(guess)
if num==8:
    print('确实是8')
else:
    if num>8:
        print('猜大了')
    else:
        print('猜小了')
    print('我答案是8')
print('游戏结束')
