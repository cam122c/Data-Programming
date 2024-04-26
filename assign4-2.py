#Cam Robinson due:3/8/24
import sys
import re

text = sys.argv[1]
pattern = "[;'!*%@#,{}$-]"

number = re.findall(pattern,text)
if re.match(pattern,text):
    print("The string contains all alphanumeric characters")
else:
    print("The string contains some non-alphanumeric characters",number)
 