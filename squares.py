# For Loops - André Roche 10-Oct-18. From GMIT course videos

# Note  - For loops in python are meant to be used with lists


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in l: # L is the list, i is the element in the list
    print (i, i*i)  # print i and i squared 
    print ()
    print (i-i*i)

print ("That's the whole list")


# another way to use lists is to use the range function

for i in range(10): # range 10 is 0-9
    print (i)
    print(i*i)

print (" That's all Folks")


print ("wait it doesn't look nicely formatted")

# use the formatting F strings 

#it goes like this

for i in range (20):
    print (f" {i:2} {i*i:4}")   # right justified 2 and 4 

print (range (20))

print (list(range(20)))   #this is a range generator

