class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def preorder(root):
    if root is None:
        return []

    return ([root.data] +
            preorder(root.left) +
            preorder(root.right))



def inorder(root):
    if root is None:
        return []

    return (inorder(root.left) +
            [root.data] +
            inorder(root.right))



def postorder(root):
    if root is None:
        return []

    return (postorder(root.left) +
            postorder(root.right) +
            [root.data])



def create_tree(values):
    if not values:
        return None

    nodes = [Node(value) for value in values]

    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]

        if right < len(nodes):
            nodes[i].right = nodes[right]

    return nodes[0]



def main():
    letters = list("DHANIELLEBELOCURA")

    root = create_tree(letters)

    print("DFS METHODS IN BINARY TREE")
    print("Name: Dhanielle Belocura")

    print("\nPreOrder Traversal:")
    print(" - ".join(preorder(root)))

    print("\nInOrder Traversal:")
    print(" - ".join(inorder(root)))

    print("\nPostOrder Traversal:")
    print(" - ".join(postorder(root)))


if __name__ == "__main__":
    main()
