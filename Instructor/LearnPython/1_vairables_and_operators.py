x = 5 #make a variable
y = 2 #make a variable

'''
the following are fairly self evident
however / does exact division, // devides and rounds down,
and x ** y takes x to the power of y
'''
print("x + y =",x + y)
print("x - y =",x - y)
print("x * y =",x * y)
print("x / y =",x / y)
print("x // y =",x // y)
print("x ** y =",x ** y)

print('-------------------------------------------------------------------')

'''
the next part of code changes the value of the variable x itself
'''
print("Right now x =", x)
x = x + 3
print("Now we add 3 to x, x now equals =",x)
x += 2
print("Now we add 2 to x, x now equals =",x)
x *= 10
print("Now we muiltply x by 10, x now equals =",x)
