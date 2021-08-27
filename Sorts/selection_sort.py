def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def selection_sort(L):
    for i in range(len(L) - 1):
        minindex = i
        for j in range(i, len(L)):
            if L[j] < L[minindex]:
                minindex = j

        swap(L, i, minindex)