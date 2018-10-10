#is it tuesday? André Roche 1-Oct-2018 from course Video GMIT Data Analytics.

import datetime    # import library.

# The next 2 lines are creating variables. They are today and dayofweek

today = datetime.datetime.today() # data structure inside datetime library called same name, datetime structure has a function call today which returns the date and time.
dayofweek = today.weekday() # weekday is the method associated with datastructure which returns an integer in the range of 0-6 (7). Monday is 0, Tuesday is 1 and so on.

print(" Let's check if it's Tuesday")


if dayofweek == 1:  # This is the condition (not equal, comparitive) Is it true of false? the colon means 'here's what to do if the condition is true'
    print ("it's Tuesday!")
elif dayofweek == 0: # i.e. if day of week is Monday
    print("It's not Tuesday")
    print("Luckily, it will be Tuesday tomorrow!")
else:
    print("unfortunately it's not Tuesday.") 

print ("Thanks for checking if it's Tuesday")
    
       
