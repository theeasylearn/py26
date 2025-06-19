d1 = {
    'name':'D patel',
    'age':26,
    'subject':'python'
}

print(d1)
d2 = {}
d2['ch']= (1,2)
d2['ch_name'] = ['intro','data type']
print(d2)
d2.clear()
print("after clear",d2)# clear() Removes all items from the dictionary.
d2=d1.copy()
print("copy of d1",d2)# copy() Returns a shallow copy of the dictionary.
d2['ch']= (1,2)
d2['ch_name'] = ['intro','data type']
print("before added d2",d1)
d1.update(d2)
print("after d2 is added",d1) # update()[other] update() method adds element(s) to the dictionary from dictionary passed as argument if the key is not in the dictionary then key value will be added . If the key is in the dictionary, it updates the key with the new value.
print(d1.fromkeys('ch_name','value'))
print(d1)# fromkeys(seq[, v]) Returns a new dictionary with keys from seq and value equal to v (defaults to None).
print("get value using key",d1.get('ch_name'))# get(key[,d]) Returns the value of the key. If the key does not exist, returns d (defaults to None).
print("items in dic",d1.items())# items() Return a new object of the dictionary's items in (key, value) format.
print("key of dict",d1.keys())# keys() Returns a new object of the dictionary's keys.

print("values of dict",d1.values())# Values() The values() method returns a view object that displays a list of all the values in the dictionary.
print("remove using key",d1.pop('ch'))
print(d1)# pop(key[,d]) Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
d1.popitem()# popitem() Removes and returns last item (key, value). Raises KeyError if the dictionary is empty.
print(d1)