import re
r = re.compile("[abcd]")

print(r.search("apple"))
print(r.search("room"))
print(r.search("nmnc"))
print(r.search("kjhg"))