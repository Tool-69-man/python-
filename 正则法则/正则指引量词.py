import re
# r1=re.search(r"^\d\d\d\d$","1000")!=None
# r1=re.search(r"^\d\d\d\d$","12345")!=None
# r1=re.search(r"^\d\d\d\d$","123")!=None#只能匹配4位数字  其余不行
# r1=re.search(r"^\d{3}$","123")!=None#量词简化
# r1=re.search(r"^\d{3,5}$","123456")!=None#量词简化  { m,n}m下限n为上限  {m,}m下限，无上限
#常用量词
# *可能出现，无上限，也可以不出现，{0，}
# ？    {0，1} 最多出现1次
# +     {1，}最少出现1次
# r1=re.search(r"^travell?er$","traveler")!=None
# r1=re.search(r"^travell?er$","traveller")!=None
# r1=re.search(r"^https*$","https")!=None
# r1=re.search(r"^https*$","http")!=None
# r1=re.search(r"^<[^>]+>$","</table>")!=None#< ,>匹配标签  [^>]+匹配中间字符  不能解决tag内部出现 >
# r1=re.search(r"^\"[^\"]*\"$","\"some\"")!=None
#<table>open tag   </table>close tag    <br/>self-closing tag
# r1=re.search(r"^<[^/][^>]+>$","<table>")!=None
# r1=re.search(r"^<[^/][^>]+[^/]>$","<img/>")!=None#结尾不匹配self-closing tag
# r1=re.search(r"^</[^>]+>$","</table>")!=None
# r1=re.search(r"^<+[^>]+/>$","<br/>")!=None#匹配self-closing tag
# print(re.search(r"\d{6}","abd778899asw").group(0))
# print(re.search(r"<+[^>]+/>","<table><br/></table>").group(0))#去掉^$
# 因为要使用正则表达式在字符串中寻找匹配
# 而不是验证整个字符串能否由正则表达式匹配
# print(r1)
# print(re.findall(r"\d{6}","zip1:990033,zip2:100186"))
# for zipcode in re.findall(r"\d{8}","zipcode1:20001212,zipcode2:20200710"):
#     print(zipcode)
