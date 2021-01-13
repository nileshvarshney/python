import collections

# ordered dictionaries remember the insertion order
od1 = collections.OrderedDict()
od2 = collections.OrderedDict()

od1['one'] = 1
od1['two'] = 2

od2['two'] = 2
od2['one'] = 1

# they will not be the same as their insert order is different
if od1 == od2:
    print('***ordered Lists are equal')
else:
     print('**** ordered Lists are not equal')

print(type(od1))

kvs = [('three',3), ('four',4), ('five',5)]
od1.update(kvs)
for k , v in od1.items():
    print(k,'\t == >  ' , v)

print("="* 30)
print('K E Y S O R T E D')
print("="* 30)
for k , v in sorted(od1.items()):
    print(k,'\t == >  ' , v)