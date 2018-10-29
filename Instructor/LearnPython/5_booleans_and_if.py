
early = True
has_coffee = False
tired = True

#happy = not(early and tired) or has_coffee  #has same effect as below line
happy = not early and not tired or has_coffee
print(happy)

print('-------------------------------------------------------------------')

print('Would you like to make Flappy Bird in Python?')
answer = 'no'

if answer=='yes':
    print("Ok I'll show you.")
elif answer=='no':#elif means 'else if'
    print('Why not?')
else:
    print('I do not understand that.')
