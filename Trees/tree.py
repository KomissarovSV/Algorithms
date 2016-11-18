class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree(object):

    def __init__(self):
        self.root = None

    def put(self,key,value):
        if self.root is None:
            self.root = Node(key,value)
        else:
            self.add(self.root,key,value)

    def add(self,node,key,value):
        if node.key > key:
            if node.left is not None:
                self.add(node.left,key,value)
            else:
                node.left = Node(key,value)
        else:
            if node.right is not None:
                self.add(node.right,key,value)
            else:
                node.right = Node(key,value)

    def find(self,key):
        return self.findRec(self.root,key)

    def findRec(self,node,key):
        if node is None:
            return None
        if node.key is key:
            return node.value
        elif node.key > key:
            if node.left is not None:
                return self.findRec(node.left,key)
            else:
                return None
        else:
            if node.right is not None:
                return self.findRec(node.right,key)
            else:
                return None

    def getHeight(self):
        return self.heightRec(self.root)

    def heightRec(self,node):
        if node is None:
            return 0
        left = 0
        if node.left is not None:
            left = self.heightRec(node.left)
        right = 0
        if node.right is not None:
            right = self.heightRec(node.right)
        return max(left, right) + 1

    def isBalanced(self):
        return self.balanceRec(self.root)

    def balanceRec(self,node):
        leftHeight = 0
        if node.left is not None:
            leftHeight = self.balanceRec(node.left)
        rightheight = 0
        if node.right is not None:
            rightheight = self.balanceRec(node.right)
        if leftHeight - rightheight == 0 or leftHeight - rightheight == 1 or leftHeight - rightheight == -1:
            return True
        else:
            return False

    def remove(self,key):
        if self.root is not None:
            self.delete(self.root,key)

    def delete(self,node,key):
        if node.key is key:
            return


tree = Tree()

tree.put(5,"five")
tree.put(7,"seven")
tree.put(3,"three")
tree.put(14,"fourteen")
tree.put(11,"eleven")
tree.put(0,"zero")
tree.put(2,"two")
tree.put(13,"thirteen")


print(tree.find(7))
print(tree.find(12))

print(tree.getHeight())

print(tree.isBalanced())