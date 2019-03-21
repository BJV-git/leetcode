# or can also implement as method of the class itself

def preorder_self(self):
    print(self.key)

    if self.left:
        self.left.preorder()
    if self.right:
        self.right.preorder()

# pre_order

def preorder(tree):
    if tree:
        print(tree.getval())
        preorder(tree.getleft())
        preorder(tree.getright())


# in-order

def inorder(tree):

        if tree:
            inorder(tree.getleft())
            print(tree.getval())
            inorder(tree.getright())


def postorder(tree):

    if tree:
        postorder(tree.getleft())
        postorder(tree.getright())
        print(tree.getval())
