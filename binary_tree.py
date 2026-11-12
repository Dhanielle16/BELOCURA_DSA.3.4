from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_binary_tree():
    """
    Constructs the Binary Tree for BELOCURA:
    Level 0: B (Root)
    Level 1: E, L
    Level 2: O, C, U, R
    Level 3: A (Child of O)
    """
    root = TreeNode('B')
    root.left = TreeNode('E')
    root.right = TreeNode('L')
    root.left.left = TreeNode('O')
    root.left.right = TreeNode('C')
    root.right.left = TreeNode('U')
    root.right.right = TreeNode('R')
    root.left.left.left = TreeNode('A')
    return root


def tree_bfs(root):

    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result


def tree_dfs_preorder(root, result=None):

    if result is None:
        result = []
    if root:
        result.append(root.val)
        tree_dfs_preorder(root.left, result)
        tree_dfs_preorder(root.right, result)
    return result


if __name__ == "__main__":
    print("=====================================================")
    print("  ASSESSMENT 3.3: BINARY TREE TRAVERSALS (BELOCURA)")
    print("=====================================================")

    root = build_binary_tree()
    t_bfs = tree_bfs(root)
    t_dfs = tree_dfs_preorder(root)

    print(f"BFS result: {'-'.join(t_bfs)}")
    print(f"DFS result: {'-'.join(t_dfs)}")
    print("=====================================================")