# Reverse a string
input_string = input("Enter a string to see its reverse :\t")
reverse_string = ''.join(reversed(input_string))
print(reverse_string)

# simple way
print(input_string[::-1])

# count odd and even from series of numbers
def odd_even_count(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if (i%2 == 0):
            even_count += 1
        else:
            odd_count += 1
    return "Odd count " + str(odd_count) + "\nEven Count " + str(even_count)
        
x = [1,2,3,4,56,6,7,8,9,10,11,12,12,13,14]
print(odd_even_count(x))

