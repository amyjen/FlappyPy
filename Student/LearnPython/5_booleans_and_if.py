
early = True
has_coffee = False
tired = True

#happy = not(early and tired) or has_coffee  #has same effect as below line
happy = not early and not tired or has_coffee
print(happy)

if happy:
    print("Today is going to be a good day.")
else:
    print("Today is going to be a long day.")

print('-------------------------------------------------------------------')

time = "8:00 AM"

print("Time for some breakfast")

print("Time for some Lunch")

print("Time for some Dinner")

print("I'm not hungry")
