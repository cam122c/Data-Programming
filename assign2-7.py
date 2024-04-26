dict1 = {"a":100, "b":2, "c":25, "d":9}
dict2 = {"a":200, "e":2, "f":25, "d":9}

for item in dict2:
    if item in dict1:
        dict1[item]=dict1[item]+dict2[item]
    else:
        dict1[item]=dict2[item]

print(dict1)
