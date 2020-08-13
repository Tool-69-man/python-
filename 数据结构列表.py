anime = ['灰羽之塔', '神之塔', '神的笔记本', '狼与香辛料']
print('动漫合集', anime)
anime.append('to love')
len(anime)
print('第一个动漫：%s和最后一个%s' % (anime[0], anime[4]))
print('中间动漫：%s' % anime[2])
print('现在的长度为%d' % len(anime))
new_anime = anime                           #对象
copy_anime=anime[:]                         #复制
print('new 集合展示%s' % anime)
del new_anime[3]                            #复制一个列表或者类似的序列或者其他复杂的对象
                                            # （不是如整数那样的简单 对象 ），那么你必须使用切片操作符来取得拷贝。
                                            # 如果你只是想要使用另一个变量名，两个名称都 参考 同一个对象，
                                            # 那么如果你不小心的话，可能会引来各种麻烦。
for i in new_anime:
    print(i)
print()
for i in copy_anime:
    print(i)

anime.sort()
print(anime)
print(new_anime)

