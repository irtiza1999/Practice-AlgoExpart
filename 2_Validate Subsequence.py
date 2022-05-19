# Validate Subsequence
# Given two array. Have to find if the 2nd arr is a valid subsequence of the 1st one.
# Time O(n) Space O(1)

arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
targetArr = [1, 6, -1, 10]
out = []
pointer2 = 0
len2 = len(targetArr)

for i in range(len(arr1)):
    if pointer2 == len2:
        break
    if arr1[i] == targetArr[pointer2]:
        out.append(targetArr[pointer2])
        pointer2 += 1

print(pointer2 == len2)
