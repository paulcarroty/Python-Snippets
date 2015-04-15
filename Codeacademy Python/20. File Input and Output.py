# See It to Believe It
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

# The open() Function
my_file = open("output.txt", "r+")


# Writing
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for v in my_list:
    my_file.write(str(v) + '\n')
    print v
    
my_file.close()



# Reading
my_file = open("output.txt", "r+")
print my_file.read()
my_file.close()

# Reading Between the Lines
my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()



# PSA: Buffering Data
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()

read_file.close()


#The 'with' and 'as' Keywords
 with open("text.txt", "w") as textfile:
	textfile.write("Success!")

# Try It Yourself
with open("text.txt", "w") as my_file:
    my_file.write("Super, success!")



# Case Closed?
with open("text.txt", "w") as my_file:
    my_file.write("Super, success!")
    if my_file is not my_file.closed:
        my_file.close()
    print my_file.closed
    







