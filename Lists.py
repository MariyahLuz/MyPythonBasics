#This program introduces us to lists in python

items=['bread', 'pasta', 'fruits', 'veggies']
print(items)

print("This is the first item of the list:", items[0])
print("This is the last item of the list:", items[3])
print("This is the second last item of the list:", items[-2])


items[0]='sugar'
print(items)

print(items[0:3])

#adding item to a list
items.append('chocolate')
print(items)

items.insert(3, 'candy')
print(items)

#continating lists
items2= ['chicken', 'irish', 'peas']
add_items= items+items2
print(add_items)

#prints length of a list
print("This is the length of list items one:" , len(items))
print("This is the length of list items two:" , len(items2))
print("This is the length of the final list add_items:" , len(add_items))

#checks to see if item is in the list
print('bread' in items)
print('irish' in items2)