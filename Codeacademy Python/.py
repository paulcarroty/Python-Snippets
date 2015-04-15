# Just a Little BIT
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

# Lesson I0: The Base 2 Number System
print 0b1,    '#1'
print 0b10,   '#2'
print 0b11,   '#3'
print 0b100,  '#4'
print 0b101,  '#5'
print 0b110,  '#6'
print 0b111,   '#7'
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

# I Can Count to 1100!
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine =0b1001
ten  =0b1010
eleven = 0b1011
twelve = 0b1100


# The bin() Function
for i in range(2,6):
    print bin(i)
    
    

# int()'s Second Parameter
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

# Slide to the Left! Slide to the Right!
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >>2
shift_left =shift_left << 2

print bin(shift_right)
print bin(shift_left)

# A BIT of This AND That
print bin(0b1110 & 0b101)

# A BIT of This OR That
print bin( 0b1110 | 0b101)

# This XOR That?
print bin(0b1110 ^ 0b101)

# See? This is NOT That Hard!
print ~1
print ~2
print ~3
print ~42
print ~123

# The Man Behind the Bit Mask
def check_bit4(inp):
    mask = 0b1000
    desired = inp & mask
    if desired > 0:
        return "on"
    else:
        return "off"
        
# Turn It On
a = 0b10111011
print bin(a | 0b100)


# Just Flip Out with XOR
a = 0b11101110
print bin(a ^ 0b11111111)

# Slip and Slide
def flip_bit(number, n):
    mask= (0b1 << n-1)
    result = number ^ mask

    return bin(result)
    

















