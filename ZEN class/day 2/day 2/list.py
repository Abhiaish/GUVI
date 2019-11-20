#append()
list = ["a","b","c"]
list.append("d")
x=list
print(x)

#clear()
list= ["a","b","c"]
list.clear()
print(list)

#copy
list= ["a","b","c"]
x=list.copy()
print(x)

#count
fruits = ["a", "b", "c","d","c","h"]

x = fruits.count("c")
print(x)

#extend
x = ["a","b","c"]

y = ["d","e","F"]

x.extend(y)

print(x)

#index
list = ['a', 'b', 'c']

x = list.index("c")
print(x)

#insert
x = ['a', 'b', 'c']

x.insert(1, "d")

print(x)

#pop
y = ['a', 'b', 'c']

x = y.pop(1)

print(x)

#remove
x = ['a', 'b', 'c']

x.remove("b")

print(x)

#reverse
x= ['a', 'b', 'c']

x.reverse()

print(x)

#sort
x = ['a','b','c']

x.sort()

print(x)