def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def insertion_sort(L):
    for i in range(1, len(L)):
        start = i
        while start > 0:
            if (L[start - 1] > L[start]):
                swap(L, start - 1, start)
                start -= 1
            else:
                break