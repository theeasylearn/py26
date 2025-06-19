l1 =['the',123,12.3,True,'EasyLearn']
l2 =['py',26]
t2 = ('at','Easy','Learn')
print(l1,t2)
l1.append(26)
print(l1) # append()  Add an element to the end of the list    
l1.extend(l2) 
print(l1)# extend(list)  Add  set of values(list) at the end of list. 
l1.extend([123,'xyz'])
print(l1)
l1.insert(1,'py26')
print(l1)# insert(position,item)  Insert an item at the defined position    
l1.remove(123)
print(l1)# remove(item)  Removes given item from the list    
print(l1.pop(9))
print(l1)# pop(position)  Removes and returns an element at the given position
print(l2)
print(l2.clear())
print(l2)# clear()  Removes all items from the list    
print(l1.index(12.3))# index()  Returns the index of the first matched item    
print(l1.count('py'))# count(item)  Returns the count of the number of items passed as an argument    
l3=[1,2,3,4,9,8,7,7,6,5,1]
l4 = ['ds','fd','esr','tye','qwe','da']
l3.sort()
l4.sort()
print(l3);print(l4)# sort()  Sort items in a list in ascending order if all items are of same type    
l4.reverse()
print(l4)# reverse()  Reverse the order of items in the list    
l5=l4.copy()
print(l5)# copy()  Returns a shallow copy of the list
