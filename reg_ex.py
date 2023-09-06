import re
txt="the rain in the spain"
x=re.search("^the.*spain$",txt)
if x:
    print("yes match found")
else:
    print("no match found")