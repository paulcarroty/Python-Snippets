#  6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
p1= text.find(" ")
#print "p1=", p1

p2= text.find(" ")
#print "p2=", p2


print float(text[p1:])
