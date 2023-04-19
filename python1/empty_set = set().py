import os
os.system('clear')

empty_set = set()

a = {1, 2}
b = {2, 3}
a.add(6)

diction = {
    "firsen" : {'table', 'chair'}
}
    

print(a & b)
print(a | b)
print(b - a)
print(a ^ b)

# a = frozenset(a) после него нельзя изменять а

c = [3, 3, 3, 2, 2]
print(c.count(3))

