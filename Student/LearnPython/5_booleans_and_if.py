
early = True
has_coffee = False
tired = True

#happy = not(early and tired) or has_coffee  #has same effect as below line
happy = not early and not tired or has_coffee
print(happy)

if happy:
    #do code iniide of
    print("Today is going to be a good day.")
else:
    print("Today is going to be a long day.")

print('-------------------------------------------------------------------')

time = "1:00 PM"

if time == "8:00 AM":
    print("Time for some breakfast")
elif time == '1:00 PM':
    print("Time for some Lunch")
elif time == "6:00 PM":
    print("Time for some Dinner")
else:
    print("I'm not hungry")
