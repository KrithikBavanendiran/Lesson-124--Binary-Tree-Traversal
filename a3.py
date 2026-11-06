from binarytree import build

class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
    
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.val, end=' ')

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.right=Node(6)

    tree_list=[1,2,3,4,5,6]
    visual_tree=build(tree_list)
    print("\nBinary tree visualisation: ")
    print(visual_tree)
    print("Postorder traversal of the binary tree: ")
    print(root.postorder_traversal())
