import re
print(re.search("^ap","apple"))
print(re.search("[^ap]","apple"))
print(re.search("[^ab]","bread"))
print(re.search("[^ab]","orange"))
print(re.search("[^ap]","anana"))