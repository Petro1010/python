## @file conversion_calculator.py
#  @brief Conversion Algorithms
#  @date March 18, 2022

currencyCVals = {
    ("US Dollars", "Euros"): 0.91,
    ("US Dollars", "Jap Yen"): 119.45,
    ("US Dollars", "Pounds"): 0.76,
    ("US Dollars", "CA Dollars"): 1.26,

    ("Euros", "US Dollars"): 1.10,
    ("Euros", "Jap Yen"): 131.70,
    ("Euros", "Pounds"): 0.84,
    ("Euros", "CA Dollars"): 1.39,

    ("Jap Yen", "US Dollars"): 0.0084,
    ("Jap Yen", "Euros"): 0.0076,
    ("Jap Yen", "Pounds"): 0.0064,
    ("Jap Yen", "CA Dollars"): 0.011,

    ("Pounds", "US Dollars"): 1.32,
    ("Pounds", "Euros"): 1.19,
    ("Pounds", "Jap Yen"): 157.36,
    ("Pounds", "CA Dollars"): 1.66,

    ("CA Dollars", "US Dollars"): 0.79,
    ("CA Dollars", "Euros"): 0.72,
    ("CA Dollars", "Jap Yen"): 0.60,
    ("CA Dollars", "Pounds"): 94.70,
}

cryptoCVals = {
    ("Bitcoin", "Ethereum"): 14.04,
    ("Bitcoin", "Dogecoin"): 344342.42,
    ("Ethereum", "Bitcoin"): 0.071,
    ("Ethereum", "Dogecoin"): 24483.37,
    ("Dogecoin", "Bitcoin"): 0.0000029,
    ("Dogecoin", "Ethereum"): 0.000041,

}

## @brief Converts from selected currency to another selected currency
#  @param initialVal A real number that represents the currency value
#  @param currFrom A string value that represents the currency of the initialVal
#  @param currTo A string value that represents which currency to convert to
#  @return the final value after conversion
def convertCurrency(initialVal, currFrom, currTo):
    mult = currencyCVals[(currFrom, currTo)]
    finalVal = float(initialVal) * mult
    return finalVal

## @brief Converts from selected cryptocurrency to another selected cryptocurrency
#  @param initialVal A real number that represents the cryptocurrency value
#  @param currFrom A string value that represents the cryptocurrency of the initialVal
#  @param currTo A string value that represents which cryptocurrency to convert to
#  @return the final value after conversion
def convertCrypto(initialVal, currFrom, currTo):
    mult = cryptoCVals[(currFrom, currTo)]
    finalVal = float(initialVal) * mult
    return finalVal

## @brief Converts from a selected numerical value of a base to another base value
#  @param initialVal A real number that represents the initial numerical value
#  @param baseFrom A string value that represents the base of the initialVal
#  @param baseTo A string value that represents which base to convert to
#  @return the final value after conversion
def convertBase(initialVal, baseFrom, baseTo):
    arr = []
    if(baseFrom == "10" and baseTo == "2"):
        decToBin(int(initialVal), arr)
        finalVal = "".join(str(x) for x in arr[:-1])
        return finalVal
    elif (baseFrom == "10" and baseTo == "8"):
        decToOct(int(initialVal), arr)
        finalVal = "".join(str(x) for x in arr[1:])
        return finalVal
    elif (baseFrom == "10" and baseTo == "16"):
        decToHex(int(initialVal), arr)
        finalVal = "".join(str(x) for x in arr[1:])
        return finalVal
    else:
        finalVal = 0
    
    return finalVal

def decToBin(x, arr):
    if x >= 1:
        decToBin(x // 2, arr)
    arr.append(x % 2)

def decToOct(x, arr):
    if x > 0:
        decToOct(x // 8, arr)
    arr.append(x % 8)


conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def decToHex(x, arr):
    if x > 0:
        decToHex(x // 16, arr)
    arr.append(conversion_table[x % 16])


## @brief Converts from a decimal value to a roman numeral value and from a roman numeral value to a decimal value
#  @param initialVal A string that represents the initial value
#  @param RNFrom A string value that represents the type of the initialVal
#  @param RNTo A string value that represents which type to convert to
#  @return the final value after conversion
def convertRN(initialVal, RNFrom, RNTo):
    if(RNFrom == "Decimal" and RNTo == "Roman Numerals"):
        finalVal = dectoRN(int(initialVal))
        return finalVal 
    elif(RNFrom == "Roman Numerals" and RNTo == "Decimal"):
        finalVal = romanToInt(initialVal)
        return finalVal 
    else:
        finalVal = 0
        return finalVal

def dectoRN(x):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    finalVal, i = "", 0
    while x > 0:
        finalVal += (x//values[i]) * numerals[i]
        x %= values[i]
        i += 1
    return finalVal

def romanToInt(x):
    romanNumerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    finalVal, p = 0, 'I'
    for c in x[::-1]:
        finalVal, p = finalVal - romanNumerals[c] if romanNumerals[c] < romanNumerals[p] else finalVal + romanNumerals[c], c
    return finalVal