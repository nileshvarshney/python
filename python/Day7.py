""" take 2 integer and generate an array of input size """

raw_input = input('Enter two variables:\t ')
dimension = [int(x) for x in raw_input.split(',')]
print(dimension)
rowin_in = dimension[0]
column_in = dimension[1]

# initialize list
list = [[ column for column in range(column_in)] for row in range(rowin_in)]

# populate calcualted value for array
for row in range(rowin_in):
    for column in range(column_in):
        list[row][column] = row * column

print(list)

