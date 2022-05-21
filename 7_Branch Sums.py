# Branch Sums
# Time O(n) Space O(n)
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


def brachSums(root):
    sums = []
    caclBranchSum(root, 0, sums)
    return sums


def caclBranchSum(node, runningSum, sums):
    if node is None:
        return
    newSum = runningSum + node.val
    if node.left is None and node.right is None:
        sums.append(newSum)
        return
    caclBranchSum(node.left, newSum, sums)
    caclBranchSum(node.right, newSum, sums)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print(brachSums(r))
