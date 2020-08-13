# 实现身份证的匹配 身份证有 15位和18位  18位末尾可能是 x    首位不是0
import re


str1 = r"^[1-9]\d{13,16}[0-9x]$"
print('str1 \n', re.search(str1, "342401200012121315") != None)
print(re.search(str1, "34240120001212131x") != None)  # 18位两种情况都能匹配
print(re.search(str1, "342401200012121") != None)
print(re.search(str1, "34240120001212x") != None)  # 但15位不存在末尾位为x,必需改变表达式
str2 = r"^[1-9]\d{16}[0-9x]$"  # 只能匹配18位可以改写为        r"^[1-9]\d[14]\d[2][0-9x]$"
str3 = r"^[1-9]\d{14}$"  # 只能匹配15位                        \d[2][0-9x]可有可无   用？解决
# \d[2][0-9x]?     是对[0-9x]的限定       这时需要 ()
str4 = r"^[1-9]\d{14}(\d{2}[0-9x])?$"
print('str4 \n', re.search(str4, "342401200012121315") != None)
print(re.search(str4, "34240120001212131x") != None)
print(re.search(str4, "342401200012121") != None)
print(re.search(str4, "34240120001212x") != None)  # 错误 表达式正确
#     子表达式  一个整体      "(\d{2}[0-9x])?"     括号起分组作用

openTag1 = r"^<[^/][^>]*[^/]>$"  # 可以匹配open tag 排除self-closing tag   但是单个字母不行
print('openTag1 \n', re.search(openTag1, "<u>") != None)
print(re.search(openTag1, "<table>") != None)
print(re.search(openTag1, "<u/>") != None)
print(re.search(openTag1, "</table>") != None)
openTag2 = r"^<[^/]([^>]*[^/])?>$"  # 所以必须让后面的[^>]*[^/]可有可无
print('openTag2 \n', re.search(openTag2, "<u>") != None)
print(re.search(openTag2, "<table>") != None)
print(re.search(openTag2, "<u/>") != None)
print(re.search(openTag2, "</table>") != None)

#多选结构   (…… | ……)竖线分隔开多个子表达式
str5=r"^[1-9]\d{14}|[1-9]\d{16}[0-9x]$"
print('str5\n', re.search(str5, "342401200012121315") != None)
print(re.search(str5, "34240120001212131x") != None)
print(re.search(str5, "342401200012121") != None)
print(re.search(str5, "34240120001212x") != None)


