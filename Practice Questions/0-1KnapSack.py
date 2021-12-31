#items will hold values and their weights, n is the amount of items
#returns maximum possible value that can be put into the sack
def knapSackNaive(weight, items, n):

	if weight == 0 or n == 0:   #when no remaining capacity or no items to choose, the max value is 0
		return 0

	if items[n - 1][1] > weight:   #if weight of nth item is more than remaning capacity, it can not be included
		return knapSackNaive(weight, items, n - 1)

	else:
		#take the maximum of whether we inclide the item or do not include it
		return max(knapSackNaive(weight, items, n - 1), items[n - 1][0] + knapSackNaive(weight - items[n - 1][1], items, n - 1))


print(knapSackNaive(50, [(60, 10), (100, 20), (120, 30)], 3))


#This implementation will avoid the computation of the same sub problem
def knapSackDynamic(weight, items, n):

	value = [[0 for i in range(weight + 1)] for j in range(n + 1)]   #a matrix that shows that value with a certain amount of weight and items

	for k in range(n + 1):
		for h in range(weight + 1):

			if k == 0 or h == 0:  #if no items or no weight left, max value is 0
				value[k][h] = 0

			elif items[k - 1][1] > h:   #if the weight of the item is greater than the remaining weight, it will have the same value as the item before it and remaining weight is the same
				value[k][h] = value[k - 1][h]

			else:
				value[k][h] = max(value[k - 1][h], items[k - 1][0] + value[k - 1][h - items[k - 1][1]])   #max of not including item and including item

	return max([max(i) for i in value])


print(knapSackDynamic(50, [(60, 10), (100, 20), (120, 30)], 3))
