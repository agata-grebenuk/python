a = ['optimist', 'pessimist', 'troll']
b = ['stacan napolovinu polon', 'stacan napolovinu pust', 'stacana net']

dict = {}
for cc,dd in zip(a,b):
    dict[cc] = dd
print(dict)
li = "oe"
word = input("Input the word:")
l_in = {letter:word.count(letter) for letter in set (word)if letter in li}
print(l_in)








