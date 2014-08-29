#  5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown. 


count = 0
largest = 0
smallest = 10
while True:
    n = raw_input("Enter a number: ")
    count = count +1;
    if n == "done" : break
    if len(n) < 1  : break
        
    try :
         num = int(n)
         if num > largest :
            largest = num
         elif num < smallest :
            smallest = num   
       
    except :
         print 'Invalid input' 
    
      
    

print "Maximum is", largest
print "Minimum is", smallest
