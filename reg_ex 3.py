import re
txt="the water is not available"
x=re.search("\s",txt)

print("the first white space is located in the position:",x.start())