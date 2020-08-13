class Person:
    def __init__(self,name):
        self.name=name
    def sayhi(self):
        print('来吧展现自我',  self.name)
p1 = Person ('为熊所有')
p1.sayhi()