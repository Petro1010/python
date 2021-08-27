from priority_queues import *

def heap_sort(L):
	temp = []
	max_heap = Pri_Queue_heap(L)
	for i in range(len(L)):
		temp.insert(0, max_heap.remove_max())

	for j in range(len(L)):
		L[j] = temp[j]
