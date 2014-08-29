# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 


# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
 #   print line
    sum = sum + float(line[line.find(' '):])
    count = count + 1

print "Average spam confidence:", sum / count

