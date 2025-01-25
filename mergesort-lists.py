# Implement a function to merge two sorted arrays into a single sorted array.

def merge_sort(arr1, arr2):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
        print(1)

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
        print(2)

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
        print(3)

    return merged_arr


a1 = [2, 5, 7]
a2 = [3, 4, 8]

print(merge_sort(a1, a2))