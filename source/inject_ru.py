import json,re
exec(open("ru.py",encoding="utf-8").read())
exec(open("ru_extra.py",encoding="utf-8").read())
s=open("src.html",encoding="utf-8").read()
d=json.dumps(RU,ensure_ascii=False).replace("</","<\\/")
s2,n=re.subn(r"var RU = \{.*?\};\n  var lang = 'en';",lambda m:"var RU = "+d+";\n  var lang = 'en';",s,count=1,flags=re.S)
assert n==1
open("src.html","w",encoding="utf-8").write(s2)
