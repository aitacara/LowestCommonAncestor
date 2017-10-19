class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.l = TreeNode(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)

    def printTree(root):
      thislevel = [rootnode]
      a = '                                 '
      while thislevel:
        nextlevel = list()
        a = a[:len(a)/2]
        for n in thislevel:
          print a+str(n.value),
          if n.left: nextlevel.append(n.left)
          if n.right: nextlevel.append(n.right)
          print
          thislevel = nextlevel