# Non-Constructible Change
# Given an array of coins. Have to find a value which is not possible to make using the coins in the array. (Can use a coin only one time)
# Time O(n) Space O(1)

arr = [5, 7, 1, 1, 2, 3, 22]
arr = sorted(arr)
sum = 0
for i in range(len(arr)):
    if sum + 1 >= arr[i]:  # if prev sum + 1 < current coin then not possible
        sum += arr[i]
    else:
        break
print(sum+1)
