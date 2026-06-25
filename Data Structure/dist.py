
d = {}
print(type(d))
# alt + shift + A to commment the multiple lines in python
d = {
    "id":123,"name":"shoheb","salary":"123",
}
print(d.keys())
print(d.values())
del d["id"]
print(d.clear()) # remove the all the list elements


#conveting from list or tuples to dist using zip ex :- a = dict(zip(key,values))
keys = ("id","name","salary")
values = (1,"shoheb",123)
emp = dict(zip(keys,values))
print(emp)

keys = ["id","name","salary"]
values = [1,"shoheb",123,123] #ignoring extra values
emp = dict(zip(keys,values))
print(emp)

keys = ["id","name","salary"]
values = [1,"shoheb"] 
emp = dict(zip(keys,values))
print(emp) # only print the key which values is there.
#dict using the for loop
d = {
    "id":123,"name":"shoheb","salary":"123",
}
for x in d.items():
    print(x)