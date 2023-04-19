
import os
os.system("clear")

def foo(*a):
    for i in range(len(a)):
        if a[i]== 5:
            a[i]= 3
    print("-----", a)

test = [1,2,3,4,5,5,5]
print(test)

foo(test)
print(test)















































# import os
# os.system("clear")

# def foo(**args):

#     sum = 0
#     for value in args.values():
#         sum += value
    
#     return sum

# res = foo(a=5, b=4)

# print(res)