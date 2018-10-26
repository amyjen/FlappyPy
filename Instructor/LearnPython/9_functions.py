def fun(x, y = 2): #x value is required, y value defaults to 2 if not provided
    return x + y #returns the value of the two numbers added together

print(fun(2,2)) #show that the method call adds the two numbers
print(fun(2)) #show that the method call adds 2 to the default y value of 2

print('-------------------------------------------------------------------')

country = "USA" #creates a variable outside the scope of the function

def place(state):
    global country #references variable outside the scope of the function using the global keyword
    return state + ", " + country #returns the strings concatinated together with a comma

print(place("Texas"))
