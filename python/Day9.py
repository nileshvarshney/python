# Create an array of five element and display then
from array import  array

array_num = array('i',[1,3,5,7,9])
for arr in array_num:
    print(arr)

# append an element at the end of array
array_num.append(11)
print ('Array num ',array_num)

# reverse the order
print(array_num[::-1])

# insert new value after number 3
array_num.insert(2,4)
print ('Array num ',array_num)

# remove an item from array
array_num.pop(2)
print ('Array num ',array_num)

# remove first occurance
array_num.remove(3)
print ('Array num ',array_num)

print(type(array_num))
x = array_num.tolist()
print(type(x))
