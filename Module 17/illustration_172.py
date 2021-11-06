class node:
    def _init_(self, data=None):
        self.data=data
        self.left= None
        self.right=None

class BST:
    def init (self,data):
        self.root=node()
        self.root._init_(data)

    def InsertNode(self, val):
        ptr=self.root
        root1=self.root
        while(ptr!=None):
            if (val>ptr.data):
                root1=ptr
                ptr=ptr.right
            elif (val<ptr.data):
                root1=ptr
                ptr=ptr.left
            if (ptr==None):
                if (val<root1.data):
                    Node=node()
                    Node._init_(val)
                    ptr=node()
                    ptr.left=None
                    ptr.data=val
                    ptr.right=None
                    root1.left=ptr
            else:
                Node = node()
                Node._init_(val)
                ptr=node()
                ptr.right=None
                ptr.data=val
                ptr.right=None
                root1.right=ptr

    def traverse(root):
        ptr=root
        if (ptr.left!=None):
            BST.traverse(ptr.left)
            print(" ",str(ptr.data),end='')
        if (ptr.right!=None):
            BST.traverse(ptr.right)

new_bst=BST()
new_bst.init(10)
print('\nTree\t:')
BST.traverse(new_bst.root)
new_bst.InsertNode(20)
new_bst.InsertNode(5)
print('\nTree\t:')
BST.traverse(new_bst.root)
new_bst.InsertNode(2)
new_bst.InsertNode(1)
new_bst.InsertNode(15)
new_bst.InsertNode(17)
print('\nTree\t:')
BST.traverse(new_bst.root)
