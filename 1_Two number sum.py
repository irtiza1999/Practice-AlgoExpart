# Two number sum
# We have an array and a target integer. We need to find a pair of number which's sum == target.
# Time O(n) Space O(n)
# def twoNumSum():
#     mySet = []
#     myArr = [3, 5, -4, 8, 11, 1, -1, 6]
#     target = 10

#     for i in myArr:
#         y = target-i
#         if y in mySet:
#             print(y, i)
#         else:
#             mySet.append(i)


# Time O(n) Space O(1)
# Similar like binary search
def twoNumSum():
    myArr = [3, 5, -4, 8, 11, 1, -1, 6]
    myArr = sorted(myArr)
    l = 0
    r = len(myArr) - 1
    target = 10
    while l < r:
        mySum = myArr[l] + myArr[r]
        if mySum == target:
            return (myArr[l], myArr[r])
        elif mySum < target:
            l += 1
        elif mySum > target:
            r -= 1
    return []


print(twoNumSum())
