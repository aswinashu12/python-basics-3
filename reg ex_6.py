import re
txt="the rain in the spain"
x=re.search(r"\bs\w+",txt)
print(x.group())