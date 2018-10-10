# Functions (write something once, call it anytime )

def gcd (a, b):
    """
    Returns the greatest common divisor
    """
    if a < b:
            a, b = b, a

    while b > 0:            # so as long as b is greater than 0 
        a, b = b, a % b     # woah - confusing. Python can run than one assignment at a time. This line means. The old value of b goes into the new value of a, new value of b goes into the old value of a % old value of b  
        
    return a

print (gcd(50, 20))
print (gcd(22, 143))
