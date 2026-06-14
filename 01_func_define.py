# In this code we will write how the functions concept works along with 
#  detail discription of the lines written in the code for better understanding 
# In this code we will understand the average of 3 numbers
a=1
b=2
c=2
# Here we have defined 3 variables a,b,c and assigned them values 1,2,2 respectively
avg=(a+b+c)/3   
# Here we have defined a variable avg and assigned it the value of the average of a,b,c by adding them and dividing by 3
print(avg)      
# Here we are printing the value of avg which is the average of a,b,c
# Now we will write the same code using functions to make it more reusable and organized
def average():
    # Here we have defined a function named average 
    avg=(a+b+c)/3
    # Here we are calculating the average of a,b,c by adding them and dividing by 3 and assigning it to the variable avg
    return avg
    # Here we are returning the value of avg from the function
# Now we will call the function average with the values of a,b,c   
# Here we are calling the function average with the arguments a,b,c and assigning the returned value to the variable result
print(average())
# Here we are printing the value of result which is the average of a,b,c calculated by

# the function average
