class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # Case 1: Key to delete is smaller than the current node value
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # Case 2: Key to delete is greater than the current node value
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # Case 3: Key to delete is equal to the current node value
        else:
            # Case 3.1: Node to delete has no children (leaf node)
            if not root.left and not root.right:
                root = None
            
            # Case 3.2: Node to delete has one child
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            
            # Case 3.3: Node to delete has two children
            else:
                # Find the successor (smallest value in the right subtree)
                successor = self.findMin(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
