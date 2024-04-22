class Solution:
    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete_min(self, node):
        if node:
            if node.left is None:
                temp = node.right
                del node
                return temp
            node.left = self.delete_min(node.left)
            return node
        return None


    def deleteNode(self, root, key):
        if root:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left and not root.right:
                    del root
                    return None
                if not root.left:
                    temp = root.right
                    del root
                    return temp
                if not root.right:
                    temp = root.left
                    del root
                    return temp

                temp = self.find_min(root.right)
                root.val = temp.val
                root.right = self.delete_min(root.right)

            return root
        return None