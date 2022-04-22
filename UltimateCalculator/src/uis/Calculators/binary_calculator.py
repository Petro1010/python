## @file binary_calculator.py
#  @brief Binary algorithms
#  @date March 18, 2022

import struct

## @brief Calculates IEEE 754 representation from decimal
#  @param n Decimal number
#  @return IEEE 754 floating point representation
#  @throws ValueError Throws an exception if n is too large
def toFloatingPoint(n):
    value = struct.unpack('Q', struct.pack('d', n))[0]
    return format(value,"064b")

## @brief Calculates decimal number from IEEE 754 representation
#  @param n IEEE 754 binary number
#  @return Decimal representation
#  @throws ValueError Throws an exception if n is invalid
def toDecimal(n):
     if len(n) != 64:
         raise ValueError
     hx = hex(int(n, 2))
     return format(str(struct.unpack("d", struct.pack("Q", int(hx, 16)))[0]), ".13")

## @brief Calculates sum of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Sum of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def binAdd(n, m):
    return format(n + m, "b")

## @brief Calculates difference of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Difference of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def binSub(n, m):
    return format(n - m, "b")

## @brief Calculates product of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Product of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def binMult(n, m):
    return format(n * m, "b")

## @brief Calculates quotient of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Quotient of n and m
#  @throws ZeroDivisionError Throws an exception if m equals zero
def binDiv(n, m):
    if not m:
        raise ZeroDivisionError
    return format(round(n / m), "b")

## @brief Calculates power of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Power of n to the m
#  @throws ValueError Throws an exception if n or m are invalid or n and m are both zero
def binPow(n, m):
    return format(n ** m, "b")

## @brief Calculates bitwise AND of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Bitwise AND of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def bitwiseAND(n, m):
    return format(n & m, "b")

## @brief Calculates bitwise OR of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Bitwise OR of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def bitwiseOR(n, m):
    return format(n | m, "b")

## @brief Calculates bitwise NOT of binary number
#  @param n Binary number
#  @return Bitwise NOT of n
#  @throws ValueError Throws an exception if n is invalid
def bitwiseNOT(n):
    bit_len = len(format(n, "b"))
    return format(n ^ 18446744073709551615, "b")[-bit_len:]

## @brief Calculates bitwise XOR of two binary numbers
#  @param n Binary number
#  @param m Binary number
#  @return Bitwise XOR of n and m
#  @throws ValueError Throws an exception if n or m are invalid
def bitwiseXOR(n, m):
    return format(n ^ m, "b")

## @brief Calculates rightward bit shift of binary number using given shift number and length
#  @param n Binary number
#  @param shiftNum Number of shifts
#  @param length Length of binary number 
#  @return n bit shifted rightward shiftNum times
#  @throws ValueError Throws an exception if n larger than length or n in invalid
def rshift(n, shiftNum, length):
    if len(format(n, "b")) > length:
        raise ValueError
    return format(n >> shiftNum, "b").zfill(length)
    
    
## @brief Calculates leftward bit shift of binary number using given shift number and length
#  @param n Binary number
#  @param shiftNum Number of shifts
#  @param length Length of binary number 
#  @return n bit shifted leftward shiftNum times
#  @throws ValueError Throws an exception if n larger than length or n in invalid
def lshift(n, shiftNum, length):
    if len(format(n, "b")) > length:
        raise ValueError
    return format(n << shiftNum, "b").zfill(length)[-length:]

