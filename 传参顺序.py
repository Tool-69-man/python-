def fun(a,b=10,c=20):
    print('a:',a,'b:',b,'c:',c)
fun(1,5)
fun(25,c=25)
fun(c=30,a=100)
#fun(c=40,a=50,60)#报错
fun(c=40,a=50,b=60)
