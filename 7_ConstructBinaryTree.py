class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def __init__(self):
        self.preorders = []
        self.inorders = []

    def solve(self, prevals, invals):
        if not prevals or not invals:
            return None

        root_val = prevals[0]
        root = Node(root_val)

        inorder_root_idx = invals.index(root_val)

        left_length = inorder_root_idx
        right_length = len(invals) - left_length - 1

        if left_length:
            root.left = self.solve(prevals[1:left_length + 1], invals[:inorder_root_idx])

        if right_length:
            root.right = self.solve(prevals[left_length + 1:], invals[inorder_root_idx + 1:])

        return root

    def inorder(self, subtree):
        if subtree:
            self.inorder(subtree.left)
            self.inorders.append(subtree.val)
            self.inorder(subtree.right)

    def preorder(self, subtree):
        if subtree:
            self.preorders.append(subtree.val)
            self.preorder(subtree.left)
            self.preorder(subtree.right)


def test():
    s = Solution()
    prevals = [1, 2, 4, 7, 3, 5, 6, 8]
    invals = [4, 7, 2, 1, 5, 3, 8, 6]
    root = s.solve(prevals, invals)
    s.inorder(root)
    assert s.inorders == invals

    s.preorder(root)
    assert s.preorders == prevals


if __name__ == '__main__':
    test()
