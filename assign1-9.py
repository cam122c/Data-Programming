#Cam robinson due 1/26/24 
list1 = ["clothing (armor)","clothing (formal)","healing potion","shield","sword"]

print("Your items:")

for itr in list1:
    print(itr)

print("You have",len(list1),"items in your inventory.") 

print("You have fallen into a viper pit.")
if "healing potion" in list1:
    print("You use a healing potion and survived the fall.")
    list1.remove("healing potion")
    print("You have",len(list1),"items in your inventory.") 
else:
    print("You die.")
    
chest = ["5 gold pieces","3 gems","mana potion"]

print("You have found a chest which contains:")
print(chest)
list1[0:0]=chest
print("You have",len(list1),"items in your inventory.")
print("You have been robbed.")
list1.clear()
print("You have",len(list1),"items in your inventory.")  