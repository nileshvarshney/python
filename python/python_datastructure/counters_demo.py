from collections import Counter

cntr = Counter({})
print(cntr)

cntr.update({'Sun':1})
cntr.update({'Sun':1}) # This will add 1 to Sun value
cntr.update({'Mon':1})
cntr.update({'Tue':1})
cntr.update({'Sun':1}) # This will add 1 to Sun value
print('Sunday Counter Value is :{}'.format(cntr['Sun']))
print('What is the value of Wed :{}'.format(cntr['Wed']))
print(cntr.pop('Sun'))
print(cntr)