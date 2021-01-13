from array import array

arr_name = array('i',[10, 20, 30, 40, 50])
def print_array():
    for x in arr_name:
        print(x, end=" ")
    print()

print_array()
print('First element of the array :{}'.format(arr_name[0]))
print('No of elements :{}'.format(len(arr_name)))
arr_name.insert(1, 90)
print('Post insert element')
print_array()

arr_name.remove(90)
print('Post remove element')
print_array()