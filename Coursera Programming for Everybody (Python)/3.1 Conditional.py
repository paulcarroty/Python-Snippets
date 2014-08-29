#  3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 

hrs = raw_input("Enter Hours:")
h = float(hrs)
basic_rate = 10.50

if h <=40:
   pay = h * basic_rate
elif h > 40:
   pay = 40* basic_rate + (h-40)*1.5*basic_rate
else: 
   print 'wrong parameter'
    
    
print pay
