#add()
sets={"A","B","C"}
sets.add("D")
print(sets)

#clear()
sets={"A","B","C","D"}
sets.clear()
print(sets)

#copy()

sets={"A","B","C","D"}
x=sets.copy()
print(x)

#difference()
x={"A","B","C"}
y={"D","B","A"}
z=y.difference(x)
print(x)

#difference_update()
x={"A","B","C"}
y={"D","B","A"}
y.difference_update(x)
print(y)

#discard()
sets={"A","B","C","D"}
sets.discard("C")
print(sets)

#intersection()
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)

#intersection_update()
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

#isdisjoint()
x = {"a", "b", "c"}
y = {"a", "d", "f"}

z = x.isdisjoint(y)

print(z)

#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#issuperset()
x={"a","b","c","f","j","k"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)

#pop()
sets={"a","b","c"}
sets.pop()
print(sets)


#remove()
sets = {"a", "b", "c"}

sets.remove("b")

print(sets)



#Symmetric_difference()
x = {"a", "b", "c"}
y = {"g", "m", "a"}

z = x.symmetric_difference(y) 

print(z)

#symmetric_difference_update()
x = {"a", "b", "c"}
y = {"g", "m", "a"}

x.symmetric_difference_update(y)

print(x)

#union
x = {"a", "b", "c"}
y = {"g", "m", "a"}

z = x.union(y)

print(z)

#update
x = {"a", "b", "c"}
y = {"d", "e", "f"}

x.update(y)

print(x)