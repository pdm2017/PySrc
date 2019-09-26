import re
r = re.compile("e$")
print(r.search("apple"))
print(r.search("banana"))
print(r.search("bread"))
print(r.search("edu"))