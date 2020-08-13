import re
import requests
url='http://h5.hunlipic.com/web.php?id=q6YyYKL'
req=requests.get(url)
find_text=re.findall( "<script[\s>][\s\S]+?</script>", req.text )
print(find_text)
