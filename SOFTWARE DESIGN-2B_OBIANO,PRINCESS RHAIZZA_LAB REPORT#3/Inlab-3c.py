# Python program to count
# full nodes in a Binary Tree
# using iterative approach

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to count full nodes of binary tree
def getfullCount(root):
    # Base Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize count
    queue.append(root)

    count = 0  # initialize count for full nodes
    while (len(queue) > 0):
        node = queue.pop(0)

        # if it is full node then increment count
        if node.left is not None and node.right is not None:
            count = count + 1

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    return count


# Driver Program to test above function
root = Node(3)
root.left = Node(5)
root.right = Node(7)
root.left.right = Node(0)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

print(getfullCount(root))
