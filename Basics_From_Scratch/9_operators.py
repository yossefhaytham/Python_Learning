# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division ======> output is integer number floor(3.9)=3.....

print(10 + 30)  # 40
print(60 - 30)  # 30
print(10 * 3)  # 30
print(100 / 20)  # 5.0
print(8 % 2)  # 0
print(2 ** 5)  # 32
print(100 // 20)  # 5

#====================================================================
#Boolean Values Are The Two Constant Objects False + True.
# -- Assignment Operators --
    # a = 5
    # b = 2
# -- Compound assignment --
    # a -= b     # subtract b from a and assign result to a (a = a - b) 
    # a += b     # add b to a and assign result to a (a = a + b)
    # a *= b     # multiply a by b and assign result to a (a = a * b)
    # a /= b     # divide a by b and assign result to a (a = a / b) float number
    # a **= b    # raise a to the power of b and assign result to a (a = a ** b)
    # a %= b     # take remainder of a divided by b and assign result to a (a = a % b)
        #op1 % op2 = op1 - floor(op1 / op2) * op2  ====> floor (3,2)=4 ..........
    # a //= b    # floor divide a by b and assign result to a (a = a // b) integer number
    # a >>= b    # shift bits of a to the right by b and assign result to a (a = a >> b)
    # a <<= b    # shift bits of a to the left by b and assign result to a (a = a << b)
#===========================================================================================================
# -- Boolean Operators (logical) --
    # and all condition must be true to get true
    # or  one of them must be true to get true
    # not Negation of the condition if it True ,it will be false
#===========================================================================================================
# -- Comparison Operators (relational)-- 
    # [ == ] Equal
    # [ != ] Not Equal
    # [ > ] Greater Than
    # [ < ] Less Than
    # [ >= ] Greater Than Or Equal
    # [ <= ] Less Than Or Equal
#===========================================================================================================
# --- Membership Operators ---
a = [1, 2, 3]
print(2 in a)       # True  -> check if 2 is in the list
print(4 not in a)   # True  -> check if 4 is not in the list
#===========================================================================================================
# --- Identity Operators ---
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)       # True  -> x and y refer to the same object in memory
print(x is z)       # False -> x and z have the same values but different objects
print(x is not z)   # True  -> x and z are not the same object
#===========================================================================================================
# --- Bitwise Operators ---
a = 6   # 110 in binary
b = 3   # 011 in binary
print(a & b)   # 2  -> bitwise AND
print(a | b)   # 7  -> bitwise OR
print(a ^ b)   # 5  -> bitwise XOR Bit_a same Bit_b ==> 0 not equl ==> 1 
print(~a)      # -7 -> bitwise NOT (invert bits) computer used U2(2's complement) to represent negative number
print(a >> 1)  # 3  -> shift bits of a right by 1 (110 >> 1 = 011)
print(a << 1)  # 12 -> shift bits of a left by 1  (110 << 1 = 1100)
#===========================================================================================================
# Order of Operations in Math (PEMDAS):
# --- Operators Precedence and Associativity ---
# ()                # Left-to-right
# **                # Right-to-left
# unary +, -, ~     # Right-to-left
# *, /, //, %       # Left-to-right
# +, -              # Left-to-right
# <<, >>            # Left-to-right
# >, >=, <, <=      # Left-to-right
# ==, !=            # Left-to-right
# is, is not        # Left-to-right
# in, not in        # Left-to-right
# &                 # Left-to-right
# ^                 # Left-to-right
# |                 # Left-to-right
# !                 # Right-to-left
# &&                # Left-to-right
# ||                # Left-to-right
# =, +=, -=, *=,
# /=, %=, &=, ^=,
# |=, <<=, >>=      # Right-to-left
# , (comma)         # Left-to-right