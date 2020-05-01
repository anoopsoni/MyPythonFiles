x = 10
print(x)

def example1():
    z = 10
    x = 2
    print('x is :',x ,'z is:',z)

example1()

def example2():
    global x
    x += 1
    print(x)
example2()

print(x)
