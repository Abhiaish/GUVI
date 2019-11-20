#clear()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

stud.clear()

print(stud)

#copy()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.copy()

print(stud)

#fromkeys()
x = ('a', 'zen', '2019')

dict = dict.fromkeys(x)

print(dict)

#get()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.get("year")

print(x)

#item()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.items()

print(x)

#keys()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.keys()

print(x)

#pop()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

stud.pop("name")

print(stud)

#pop_item()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

stud.pop_item("name")

print(stud)

#setdefault()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.setdefault("name","b")

print(x)


#update()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

stud.update({"age":"25"})
print(stud)

#value()
stud = {
  "name": "a",
  "class": "zen",
  "year": 2019
}

x=stud.value()

print(stud)






