# Find the factors of an integer, André Roche 28-Sept-18

def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print (i)
if __name__ == '__main__':
    b = input ('Input Number Please')
    b = float (b)

    if b > 0 and b.is_integer():
        factors (int(b))
    else:
        print('Please enter a positive integer')


# explanation - the user inputs an integer. This is b+1 e.g it could be anything.|The +1 ensures it uses that number too! 
# we want to print everything in the range of 1 to the user input value if it's evenly divisible
# it accepts floating point calculations and the input value must be bigger than 0 