#a function call itself is called recursion until the base condition fail.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))