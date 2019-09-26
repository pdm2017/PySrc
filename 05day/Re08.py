import re
r = re.compile("^c")
print(r.search("cw"))
print(r.search("hsw"))
print(r.search("ckkw"))
print(r.search("kkkw"))