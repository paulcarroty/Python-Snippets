# Input
print 'Welcome to the Pig Latin Translator!'
original = raw_input("Enter a word:")


# Check your name
print 'Welcome to the Pig Latin Translator!'

original = raw_input("Enter a word:")

if len(original) >0 and original.isalpha():
    print original
else:
    print "empty"


# Pop Quiz
print 'Welcome to the Pig Latin Translator!'

original = raw_input("Enter a word:")

if len(original) >0 and original.isalpha():
    print original
else:
    print "empty"
    
    
# Word Up
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'


# Move it on Back
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word +first + pyg
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'


# Ending Up
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word +first + pyg
new_word = new_word[1:len(new_word)]
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
    
    
