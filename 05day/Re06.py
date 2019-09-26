import re
r = re.compile("ck*w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("kkkw"))
print(r.search("ckaw"))