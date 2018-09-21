# write a program that can return factirial of a given number

def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num - 1)

print   ("Enter a integer....")
number = int(input())
print (factorial(number))
print ("Test")