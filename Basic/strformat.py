#item should be in "" and separated by sales
item = input("Enter the item name: ")
sales = input("Enter the quantity: ")
print('"{0}",{1}'.format(item, sales))
print(item + ',' + sales)
print('"' + item + '",' + sales)
print("{0},{1}".format(item, sales))
print('"%s", %s' % (item, sales))
