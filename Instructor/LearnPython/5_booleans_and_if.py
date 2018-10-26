#leave all of this code to be played around with
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
# so start with time and build the ifs with them
time = "8:00 AM"

if time == "8:00 AM":
    print("Time for some breakfast")
else if time == "1:00 PM":
    print("Time for some Lunch")
elif time == "6:00 PM":                 #elif means else if
    print("Time for some Dinner")
else:
    print("I'm not hungry")
