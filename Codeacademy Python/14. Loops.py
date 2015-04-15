# While you're here
count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1
    
# Condition
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False
    
# While you're at it
num = 1

while num <= 10:  # Fill in the condition
    print num**2    # Print num squared
    num+=1        # Increment num (make sure to do this!)
    
# Simple errors

choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")


# Infinite loops
count = 0

while count < 10: # Add a colon
    print count
    count+=1    # Increment count
    
    
# Break
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
        
# While / else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
    
# Your own while / else
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number

guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    guesses_left-=1
    if guess == random_number:
        print "You win!"
        break
    else:
        print "You lose."
else:
    print "Game over"
    
    
# For your health
print "Counting..."

for i in range(20):
    print i
    
    
# For your hobbies
hobbies = []

for i in range(3):
    hobbies.append(raw_input("Please enter your hobby:"))
    
# For your strings
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

for w in word:
    print w


# For your A
phrase = "A bird in the hand..."

# Add your for loop
for w in phrase:
    for l in w:
        if l == 'A':
            print 'X',
        elif l == 'a':
            print 'X',
        else:
            print l,



#Don't delete this print statement!
print 

# For your lists
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for num in numbers:
    print num**2
    
    
    
# Looping over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print key, d[key]
    
# Counting as you go
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item
    
    
# Multiple lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print max(a, b)
    
    
# For / else
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
    
    
# Change it up
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    print 'A', f
else:
    print 'A fine selection of fruits!'
    
    
# Create your own
for x in ["Bayern", "Arsenal", "Inter"]:
    if x == "Arsenal":
        print x, "is great!"
else:
    print "All ok!"
    







 













