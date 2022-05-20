# Find Closest Value in BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Recursive
# Time O(log n) Space O(lon n)


# def findClosest(root, target, mini=10**10):
#     if root is None:
#         return mini
#     if abs(target - mini) > abs(target-root.val):
#         mini = root.val
#     if target < root.val:
#         return findClosest(root.left, target, mini)
#     elif target > root.val:
#         return findClosest(root.right, target, mini)
#     else:
#         return mini

# Iterative
# Time O(log n) Space O(1)
def findClosest(root, target, mini=10**10):
    curNode = root
    while curNode is not None:
        if root is None:
            return mini
        if abs(target - mini) > abs(target-curNode.val):
            mini = curNode.val
        if target < curNode.val:
            curNode = curNode.left
        elif target > root.val:
            curNode = curNode.right
        else:
            break
    return mini


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print(findClosest(r, 12))
