__author__ = 'Pneumatic'

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b        # 12 = 0000 1100. AND Operator copies a bit to the result if it exists in both operands
print("Line 1 - Value of c is ", c)

c = a | b        # 61 = 0011 1101. OR Operator copies a bit if it exists in either operand
print("Line 2 - Value of c is ", c)

c = a ^ b        # 49 = 0011 0001. XOR Operator copies the bit if it is set in one operand but not both
print("Line 3 - Value of c is ", c)

c = ~a         # -61 = 1100 0011. Binary Ones Complement Operator is unary and has the effect of 'flipping' bits
print("Line 4 - Value of c is ", c)

c = a << 2       # 240 = 1111 0000.
print("Line 5 - Value of c is ", c)
# Binary Left Shift Operator. The left operands value is moved left by the number of bits specified by the right operand
c = a >> 2       # 15 = 0000 1111.
print("Line 6 - Value of c is ", c)
# Binary Right Shift Operator. The left operands value is moved right by number of bits specified by the right operand