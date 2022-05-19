# Sorted Squared Array
# Time O(n) Space O(n)
arr = [-7, -5, -4, 3, 6, 8, 9]
arr2 = [0]*len(arr)
idx = len(arr)-1
p1 = 0
p2 = len(arr)-1

while p1 <= p2:
    if abs(arr[p1]) > abs(arr[p2]):
        arr2[idx] = abs(arr[p1]) ** 2
        p1 += 1
        idx -= 1
    else:
        arr2[idx] = abs(arr[p2]) ** 2
        p2 -= 1
        idx -= 1
print(arr2)
