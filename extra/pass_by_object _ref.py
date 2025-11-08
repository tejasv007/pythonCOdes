# python follow pass by object reference
# for mutable it behaves like pass by reference
# pass by reference
# for mutable
def add(l):
    l.append(5)
a=[1,2,3]
add(a)
# print(a)
# for immutable it behaves like pass by value
# for immutable
def addele(s):
    s=s+"A"
a="ana"
addele(a)
print(a)