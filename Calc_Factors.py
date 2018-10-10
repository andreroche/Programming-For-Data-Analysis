# quick script to calculate the factors of integers
# André Roche 28-Sept-18 

def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

try:
    a = int(input('enter a number: '))
except ValueError:
    print ('you have entered an invalid number')

try:
    b = int(input('enter a number: '))
except ValueError:
    print ('you have entered an invalid number')

print (is_factor(a,b))

