names = []
names.append('Sally')
names.append('Joe')
names.append('Chris')
names.append('Jill')
names.append('Jack')
names.append('Ryan')
names.append('Lola')
names.append('Charlie')
names.append('James')
names.append('John')
print(names)
for x in names:
  print(names.pop(0))
  print(names.pop(0))
  print(names)
  
print(names.pop(0))

print('\nQueue after removing names')
print(names)
