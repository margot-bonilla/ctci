# Definition of a binary tree node
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
        self.n = 0

    def insert(self, x: int) -> None:
        pass

    def delete(self, x: int) -> None:
        pass

    def find(self, x: int) -> bool:
        pass

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.data)
        self.inorder()

    def getRandomNode(self) -> TreeNode:
        pass

# The BinaryTree object will be created and called as follows
# binaryTree = BinaryTree();
# binaryTree.insert(x);
# binaryTree.delete(x);
# found = binaryTree.find(x);
# randomNode = binaryTree.getRandomNode();


