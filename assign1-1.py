name = input("please enter the customer's name:")
price = float(input("please enter the unit price for the goods:"))
goods = int(input("please enter the number of the good purchased:"))
item = (input("please enter the name of the goods:"))

total = price*goods


print("the customer",name,'paid totally',total,'for',goods,'of',item)

print('the customer %s paid totally $%.2f for %d of %s'%(name,total,goods,item))