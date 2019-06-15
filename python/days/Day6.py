""" create cool calculator """
c = 50
h = 30
# formula  sqrt((2 * c * d)/h)
import math
x = []
y = [i for i in (input('Give me a number :\t').split(','))]
for i in y:
    d = int(i)
    x.append(str(round(math.sqrt(( 2 * c * d)/h))))

print(x)
