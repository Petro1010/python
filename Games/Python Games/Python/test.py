from functools import reduce
def noUpper(s):
	g = list(s)
	h = [i for i in g if not(91 > ord(i) > 64)]
	return "".join(h)

print(noUpper("HellS!!"))

#L = [i**(1/2) for i in range(5,20) if i%2 != 0]
#print(L)

#O = ["a","b","c"]
#B = ["d", "e", "f"]

#H = [O[i] + B[j] for i in range(len(O)) for j in range(len(B))]
#print(H)

square = lambda x : x**2
print(square(2))

a = reduce((lambda x, y: x / y), [10, 5], 200)
print(a)

print(list(map(noUpper, ["HelLLo", "KsDsX"])))

print("A".isupper())


S = (0, 1)
print(S[1])

marked = [[False for i in range(3)] for i in range(4)]
print(marked)

print((2,3) == (3 - 1, 5 - 2))
print(int("5"))

z = []
x = [1,2,3]
z.append(x)
x = [6,7,5]
z.append(x)
print(z)


print(len("hello"))