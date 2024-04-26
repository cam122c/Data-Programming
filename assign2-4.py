
my_dict={'item1':105,'item2':25,'item3':31,"item4":65,'item5':234,'item6':50}

sortV=sorted(my_dict.values(),reverse=True)

sortDict={}
for i in sortV:
    for k in my_dict.keys():
        if my_dict[k]==i:
            sortDict[k]=my_dict[k]
            break
          
for key in sortDict:
    print(key,"=>",sortDict[key])