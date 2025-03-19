class tree_node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


class AVL_tree(tree_node):
    def __init__(root, data=None):
        super().__init__(data)

    def insert(root, data):
        if root.data is None:
            root.data = data
            return root

        if data < root.data:
            if root.left is None:
                root.left = AVL_tree(data)
            else:
                root.left = root.left.insert(data)

        if data > root.data:
            if root.right is None:
                root.right = AVL_tree(data)
            else:
                root.right = root.right.insert(data)
        root.update_height()

        BF = root.get_BF()

        if BF in range(-1, 2):
            return root

        root = root.balance(data)
        return root

    def delete(root, data):
        if root is None:
            return root

        if data < root.data and root.left is not None:
            root.left = root.left.delete(data)
        elif data > root.data and root.right is not None:
            root.right = root.right.delete(data)
        elif data == root.data:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.data = root.right.min()
                root = root.right.delete(root.data)

        root.update_height()
        BF = root.get_BF()

        if BF in range(-1, 2):
            return root

        root = root.balance(data)
        return root

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def update_height(root, rotation=None):
        if rotation is None:
            root.height = (
                max(getattr(root.right, "height", -1), getattr(root.left, "height", -1))
                + 1
            )
            return

        else:
            if rotation == "RR":
                root.right.update_height()
                root.update_height()
            else:
                root.left.update_height()
                root.update_height()

    def get_BF(root):
        BF = getattr(root.right, "height", -1) - getattr(root.left, "height", -1)
        return BF

    def balance(root, data):

        if root.get_BF() < -1:

            if data < root.left.data:
                root = right_rotate(root)
                root.update_height(rotation="RR")
            else:
                root.left = left_rotate(root.left)
                root.left.update_height(rotation="LR")
                root = right_rotate(root)
                root.update_height(rotation="RR")

        else:
            if data > root.right.data:
                root = left_rotate(root)
                root.update_height(rotation="LR")
            else:
                root.right = right_rotate(root.right)
                root.right.update_height(rotation="RR")
                root = left_rotate(root)
                root.update_height(rotation="LR")

        return root

    def check_balanced(root):
        if root.get_BF() not in range(-1, 2):
            return False

        if root.left is not None:
            return root.left.check_balanced()
        if root.right is not None:
            return root.right.check_balanced()
        return True


def right_rotate(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root


def left_rotate(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root


def main():
    avl_node = AVL_tree()
    nums = [11, 12, 13, 14]
    for num in nums:
        avl_node = avl_node.insert(num)
    avl_node = avl_node.delete(13)
    print(avl_node.check_balanced())


if __name__ == "__main__":
    main()
