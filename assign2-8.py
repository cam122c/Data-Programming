#cam robinson due: 2/9/24

def removekeys(dictionary,keyremove):
    print('original dictionary:', dictionary)
    
    updated_dict = dictionary.copy()
    
    for key in keyremove:
        updated_dict.pop(key)
    
    return updated_dict
    
my_dict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
keyremove = ['k2', 'k4']

updated_dict = removekeys(my_dict,keyremove)
print('Updated dictionary:', updated_dict)