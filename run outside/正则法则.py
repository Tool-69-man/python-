import re
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""

res = re.findall('Xi.*?(\d+)\s.*?s;', content, re.S)
print(res)
