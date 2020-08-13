动漫字典 = { '野兽之战' : 'beas war',#可以用中文的字典
         '翼时代记':'小樱小狼',
         '叛逆的鲁鲁修' : '魔王与C.C.'
    }
print('第一个动漫',动漫字典['野兽之战'])
print('')
print('第二个动漫%s' % 动漫字典['翼时代记'])
print()
for name,master in 动漫字典.items():
    print('动漫%s是%s' % (name,master))
print('\n')
del 动漫字典['叛逆的鲁鲁修']
#增加
动漫字典['妖精森林的小不点']='悠闲治愈'
for name,master in 动漫字典.items():
    print('动漫%s是%s' % (name,master))
print('现在长度是%d' % len(动漫字典))