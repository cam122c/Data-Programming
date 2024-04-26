#Cam Robinson due:3/8/24
import sys
import re

letter = sys.argv[1]
pattern = "^[A-Z]{1}[a-z]+$"

if re.match(pattern,letter):
    print(letter,"matches the pattern")
else:
    print(letter,'is NOT following the pattern')