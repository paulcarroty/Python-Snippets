# BeFOR We Begin
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for n in names:
    print "%s" % n

# This is KEY!
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}


for k in webster:
    print webster[k]
    
    
# Control Flow and Looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a :
    if (number%2 == 0):
        print number
    
    

# Lists + Functions
def fizz_count(x):
    count = 0
    for i in x :
        if i == 'fizz' :
            count=count+1
    return count

# String Looping
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter, word.index("i")
        
        
# Owning a Store
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    




# Let's Check Out!
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for f in food:
        if stock[f] > 0:
            total = total + prices[f]
            stock[f] = stock[f] -1
    return total
    
    
    
 
    

