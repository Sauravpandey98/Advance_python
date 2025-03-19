from typing import List


class bst_node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if (
            self.data is None
        ):  # Side note= None should not be compared with operater like equal to or not equal to.It should always be compared using is or is not.
            self.data = data  # complexity= O(logn)
            return

        elif self.data >= data:
            if self.left:
                self.left.insert(data)
                return
            self.left = bst_node(data)
            return

        else:
            if self.right:
                self.right.insert(data)
                return
            self.right = bst_node(data)
            return

    def exist(self, data):
        # complex=O(logn)
        if data == self.data:
            return True

        if data < self.data:
            if self.left == None:
                return False
            return self.left.exist(data)

        if self.right == None:
            return False
        return self.right.exist(data)

    def min(self):

        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):

        if self.right is None:
            return self.data
        return self.right.max()

    def find_height(self):
        rheight = 0
        lheight = 0

        if self is None:  # Complexity = O(n)
            return -1

        if self.right is not None:
            rheight = self.right.find_height()
        if self.left is not None:
            lheight = self.left.find_height()

        return max(rheight, lheight) + 1

    # Implemented search operation along with deletion
    def delete_node_util(root, data, exist_flag):
        if root is None:
            print("BST is empty")
            return None

        if data < root.data and root.left is not None:
            root.left, exist_flag = root.left.delete_node_util(data, exist_flag)
        elif data > root.data and root.right is not None:
            root.right, exist_flag = root.right.delete_node_util(data, exist_flag)
        elif data == root.data:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.data = root.right.min()
                root, _ = root.right.delete_node_util(root.data, exist_flag)
        else:
            exist_flag = False
        return root, exist_flag

    def delete_node(root, data):
        exist_flag = True
        new_root, flag = bst_node.delete_node_util(root, data, exist_flag)
        if not flag:
            print("Data given is not present in the tree")
        return new_root

    def is_bstutil(self, prev):
        right_check = True
        left_check = True
        if self is not None:
            if self.left is not None:
                left_check = self.left.is_bstutil(prev)

            if prev.data is not None and self.data < prev.data:
                return False

            prev.data = self.data

            if self.right is not None:
                right_check = self.right.is_bstutil(prev)

            return left_check and right_check
        return True

    def is_bst(self):
        prev = bst_node()
        return self.is_bstutil(prev)

    ############################# TRAVERSAL ################################

    # 1. BFS(Level Order Traversal)
    def LO_trav(self):
        if self is None:
            return
        q = []
        q.append(self)
        while len(q):
            node = q.pop(0)
            print(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    # 2. DFS
    # i. Inorder
    def IO_trav(self):
        if self is None:
            return
        if self.left is not None:
            self.left.IO_trav()
        print(self.data)
        if self.right is not None:
            self.right.IO_trav()

    # ii. Preporder
    def PrO_trav(self):
        if self is None:
            return
        print(self.data)
        if self.left is not None:
            self.left.PrO_trav()
        if self.right is not None:
            self.right.PrO_trav()

    # iii. Postorder
    def PO_trav(self):
        if self is None:
            return
        if self.left is not None:
            self.left.PO_trav()
        if self.right is not None:
            self.right.PO_trav()
        print(self.data)


def create_tree_from_preorder_and_inorder(
    preorder: List[int], inorder: List[int]
) -> bst_node:
    val_indx_map = {val: indx for indx, val in enumerate(inorder)}

    pre_order_indx = 0

    def dfs(l, r):
        nonlocal pre_order_indx
        if l > r:
            return None

        node_val = preorder[pre_order_indx]
        root_node = bst_node(data=node_val)
        root_indx = val_indx_map[node_val]
        pre_order_indx += 1
        root_node.left = dfs(l, root_indx - 1)
        root_node.right = dfs(root_indx + 1, r)

        return root_node

    return dfs(0, len(inorder) - 1)


def create_tree_from_postorder_and_inorder(postorder: List[int], inorder: List[int]):
    val_indx_map = {val: indx for indx, val in enumerate(inorder)}

    post_ord_indx = -1

    def dfs(l, r):
        nonlocal post_ord_indx
        if l > r:
            return None

        node_val = postorder[post_ord_indx]
        root_node = bst_node(data=node_val)
        root_indx = val_indx_map[node_val]
        post_ord_indx -= 1

        root_node.right = dfs(root_indx + 1, r)
        root_node.left = dfs(l, root_indx - 1)

        return root_node

    return dfs(0, len(inorder) - 1)


def main():
    preorder = [1, 2, 3, 4, 5, 6, 7]
    inorder = [3, 2, 4, 1, 6, 5, 7]
    postorder = [3, 4, 2, 6, 7, 5, 1]

    root_node1 = create_tree_from_postorder_and_inorder(
        postorder=postorder, inorder=inorder
    )
    root_node2 = create_tree_from_preorder_and_inorder(
        preorder=preorder, inorder=inorder
    )

    print(root_node1.IO_trav())
    print(root_node2.IO_trav())

    # node_value = [20, 16, 14, 15, 25, 24, 26]
    # bst = bst_node()
    # for num in node_value:
    #     bst.insert(num)

    # print(
    #     "choices are :",
    #     "1. Insert",
    #     "2. Exist",
    #     "3. Max",
    #     "4. Min",
    #     "5.Find Height",
    #     "6.Level order Traversal",
    #     "7.Inorder",
    #     "8.Postorder",
    #     "9. Preorder",
    #     "10.Check_BST",
    #     "11.Delete Node",
    #     "12.Quit",
    #     sep="\n",
    # )
    # choice = ""
    # while choice != "12":
    #     choice = input("Enter your choice: ")
    #     if 1 >= int(choice) >= 12:
    #         print("Wrong choice")

    #     if choice == "1":
    #         data = input("enter data you need to insert: ")
    #         bst.insert(int(data))
    #     elif choice == "2":
    #         data = input("enter data you need to check")
    #         if bst.exist(int(data)):
    #             print("exist")
    #         else:
    #             print("does not exist")
    #     elif choice == "3":
    #         print(bst.max())
    #     elif choice == "4":
    #         print(bst.min())
    #     elif choice == "5":
    #         print(bst.find_height())
    #     elif choice == "6":
    #         bst.LO_trav()
    #     elif choice == "7":
    #         bst.IO_trav()
    #     elif choice == "8":
    #         bst.PO_trav()
    #     elif choice == "9":
    #         bst.PrO_trav()
    #     elif choice == "10":
    #         print(bst.is_bst())
    #     elif choice == "11":
    #         data = int(input("Enter the data you want to delete: "))
    #         new_bst = bst.delete_node(data)
    #         print("BST after deletion is:")
    #         new_bst.IO_trav()


if __name__ == "__main__":
    main()
