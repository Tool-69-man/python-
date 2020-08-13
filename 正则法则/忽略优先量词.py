import re
htmlSource="""
<script type="text/javascript">
alert("1")
</script>
<br/>
秀啊
<script type="text/javascript">
document.write("OP")
</script>
"""
# jsCode=r"<script type=\"text/javascript\">[\s\S]*</script>"#贪婪
jsCode=r"<script type=\"text/javascript\">[\s\S]*?</script>"#懒惰
# print(re.search(jsCode,htmlSource).group(0))
for js in re.findall(jsCode,htmlSource):
    print("秀"+js+"\n")