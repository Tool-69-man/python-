# “ .” 点号匹配任意字符  通配符
import re
# print("3",re.search(r"^.$","a")!=None)
# print("4",re.search(r"^.$","\n")!=None)#但  “ .”不能匹配 \n
# print("5",re.search(r"^[\S\s]$","\n")!=None)  #自制
# print("6",re.search(r"(?s)^.$","\n")!=None)


#贪婪量词  回溯
# print(re.search(r"\".*\"","\"CLANNAD\"").group(0))
# print(re.search(r"\".*\"","\"CLANNAD\"After story\"").group(0))
#无法在第一个引号结束， 会继续匹配，
# 所以为了准确"[^\"]"
print(re.search(r"\"[^\"]*\"", "\"CLANNAD\"After story\"").group(0))

