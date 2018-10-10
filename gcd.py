# greatest common divisor , André Roche 10-Oct-18. From GMIT course videos.

a = 50  # take a value of 50 and store it in a variable called a

b = 20  # same as above 

# now, write a program that will calculate the gcd of the value a and b

while b > 0:            # so as long as b is greater than 0 
    a, b = b, a % b     # woah - confusing. Python can run than one assignment at a time. This line means. The old value of b goes into the new value of a, new value of b goes into the old value of a % old value of b  

print (a)

