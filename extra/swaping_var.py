# thus pass by reference or value doesnt for python as there is another model
# for int, pass by value works
def swap(a,b):
    a+=b
    b=a-b
    a=a-b
    return a,b
a=21
b=34
a1,b1=swap(a,b)#here a1 and b1 are created which is new objects...not in place change can be there
print(a1,b1)