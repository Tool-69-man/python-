class People:
    num1 = 0
    def __init__ (self,name):
        self.name = name
        print('加入了',self.name)
        People.num1 += 1

    def __del__(self):
        print('%s 走了' % self.name)
        People.num1 -= 1
        if People.num1 == 0:
            print('走光了')
        else:
            print('最后还有', People.num1)
    def say(self):
        print('现在有%s' % self.name)
    def many(self):
        print('现在有%d' %  self.num1)
man1 = People('大卫')
man1.say()
man1.many()
man2 = People('摩西')
man2.say()
man2.many()
man1.say()
man1.many()