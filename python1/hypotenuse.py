import os
os.system('clear')


def foo(a,myl = []):
    myl.append(a)
    print(myl)

def sum(*args):
    #print(args)
    sum = 0
    for el in args:
        sum += el
    return sum

print(sum(2,3))

foo(3)
foo(4)
def foo_l(**args):
    print(args)

foo_l(n1=2, n2=5)