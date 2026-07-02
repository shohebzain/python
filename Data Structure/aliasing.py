#aliasing is mutable. if x == y then if any changes in y that changes will be in x
abc = {"a": "hey","b": "hey","c": "hey","d": "hey",}
x = abc
print(x)
x['a'] = "Hi" 
print(x) 
y = abc.copy()  
y['b'] = "Hi" 
print(y) 
