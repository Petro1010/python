#Implementation of Binary search:

def binary_search(L, value):
    left = 0
    right = len(L) - 1
    while left != right:
        mid = (right - left) // 2

        if value < L[mid]:
            right = mid - 1

        elif value > L[mid]:
            left = mid + 1

        else:
            return True

    return value == L[left]