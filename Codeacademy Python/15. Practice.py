#is_even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
        
# is_int
def is_int(x):
    if int(x) - x == 0:
        return True
    else:
        return False
        
        
# digit_sum
def digit_sum(n):
    sum = 0
    st = str(n)
    for i in st:
        sum += int(i)
        
    return sum
    
print digit_sum(434)

# factorial
def factorial(x):
    f = 1
    for i in range(1,x+1):
        f=f*i
    return f
    
# is_prime
def is_prime(x): 
    count = 0
    if x < 2: 
        return False 
    elif x == 2: 
        return True 
    else: 
        for i in range(1, x+1): 
            if x%i == 0: 
                count += 1
        if count < 3: 
            return True 
        else: 
            return False
            
for x in range(100):
    print x, is_prime(x)

# reverse
def reverse(text):
    str1 =''
    print range(len(text), 0, -1)
    for i in range(len(text), -1, -1):
        if i > 0:
            str1 = str1 + text[i-1]
        print str1, i
    return str1
    
# anti_vowel
def anti_vowel(text):
    res = ''
    for l in text:
        if l not in ['a', 'o', 'u', 'e', 'i', 'A', 'E', 'U', 'I', 'O']:
            res+=l
    return res
    
    
# scrabble_score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    res = 0
    for i in word:
        if i.lower() in score:
            res+=score[i.lower()]
    return res
    
# censor
def censor(text, word):
    a = ''
    lst = text.split()
    for w in range(len(lst)):
        if lst[w] == word:
            lst[w] = '*'*len(lst[w])

    for i in range(len(lst)):
        a = a + lst[i]+' '
        if a[-1] == '*':
            a +=' '
    return a[0:-1] 
    
# count
def count(sequence, item):
    ct = 0
    for i in sequence:
        if i == item:
            ct += 1
    return ct
    
# purify
def purify(lst):
    lst2 = []
    for n in lst:
        print n, "in list"
        if n%2 == 0:
            lst2.append(n)
        
    return lst2
    
# product
def product(ls):
    m=1
    for e in ls:
        m *=e
    return m
    
# remove_duplicates
def remove_duplicates(l1):
    l2 = []
    for n in l1:
        if n not in l2:
            l2.append(n)
    return l2
    
    
# median
def median(ls):
    print "list =", ls
    ls2 = sorted(ls)
    lee = len(ls2)
    print " sort list =", ls2
    if lee == 1:
        print "lee =", lee
        return ls2[0]
    elif lee % 2 != 0:
        print "lee =", lee
        return ls2[lee/2]
    else:
        print "lee =", lee
        return (ls2[lee/2] + ls2[lee/2 -1])/2.0
        
        







