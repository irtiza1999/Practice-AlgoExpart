# Minimum Waiting Time
# Time O(nlogn) Space O(1)

arr = [3, 2, 1, 2, 6]
arr = sorted(arr)
total = 0
x = len(arr) - 1
for i in range(len(arr)):
    total += arr[i]*x
    x -= 1
print(total)
