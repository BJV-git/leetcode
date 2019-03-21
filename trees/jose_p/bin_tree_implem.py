# logic: we form a tree so that it is easy to traverse, and get the values

class Bintree(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertleft(self, val):
        if not self.left:
            self.left = Bintree(val)
        else:
            temp = Bintree(val)
            temp.left = self.left
            self.left = temp

    def insertright(self, val):
        if not self.right:
            self.right = Bintree(val)
        else:
            temp = Bintree(val)
            temp.right = self.right
            self.right = temp

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getvalue(self):
        return self.val
