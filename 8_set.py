s1 ={'apple','banana','orange'}
print(s1)
s2 = set()
s2.add('abc')
print(s2)
s2.remove('abc')
print("after remove",s2)
s1 ={'apple','banana','orange'}
s2 = {'apple','kiwi','orange'}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.union(s2))
print(s2.union(s1))
print(s1.intersection(s2))
print(s2.intersection(s1))