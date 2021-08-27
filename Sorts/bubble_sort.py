def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

#Bubble sort implementation

def bubble_sort(L):
    for i in range(len(L)):
        #print(L)
        for j in range(len(L) - i - 1):
            if (L[j] > L[j + 1]):
                swap(L, j, j+1)