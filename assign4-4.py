#Cam Robinson due:3/8/24
import sys 
import re

text = sys.argv[1]
pattern = ["r'\ba\w*\s(\w+)"]
result = re.findall(r'\ba\w*\s(\w+)',text)
print(result)