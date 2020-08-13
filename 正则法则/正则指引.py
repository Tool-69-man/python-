import re
import requests

# r1=re.search("[0-9]", "12")!=None         #Ture
# r2=re.search("^[0-9]$", "12")!=None       #False
# r2=re.search("^[^0-9]$", "12")!=None      #False
# r2=re.search("[^0-9]", "12")!=None        #False
# r2=re.search("^\\d$", "9")!=None          #T
# r2=re.search(r"^\d||\D$", "9")!=None          #T
r2=re.search(r"^[\d\D]$", "9")!=None          #F
# r2=re.search(r"^\d|\D$", "9")!=None          #T  \d\D 不能用  要加|  或[\d\D]
# r2=re.search(r"^\w$", "a")!=None          #T
# r2=re.search(r"^[0-9A-Za-z]$", "j")!=None      #T
# r2=re.search(r"^\w\W$", ",")!=None                #\d 数字[0-9]    \w[0-9a-zA-Z  _ ]注意有下滑线  [\s]表示，只要出现空白就匹配
# r2=re.search(r"^[\x00-\x7F]$", ",")!=None
# r2=re.search(r"^[\x00-\x7F]$", "c")!=None


print(r2)
