#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

inp=raw_input("Enter score: ")
score=float(inp)

if score >=0.8:
    grade = 'B'
elif score >=0.7:
    grade = 'C'
elif score >=0.6:
    grade = 'D'
elif score <0.6:
    grade = 'F'
else :
    print 'incorrect score'


print grade

