
import sys

word = sys.argv[1]

my_dict = {}

for letters in word:
    my_dict[letters] = word.count(letters)
    
print(my_dict)