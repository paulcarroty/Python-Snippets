#  8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. 



fn= raw_input("Enter name of file:")
fh = open('romeo.txt')
lst = list()

for line in fh:
    line = line.strip().split()
    for w in line :
       lst.append(w) 
       

lst2 = sorted(lst)
#print lst2

l3=[]
for i in lst2 :
   if i not in l3:
      l3.append(i)

print l3
