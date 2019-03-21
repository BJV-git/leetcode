# need to find the minimum absolute diffrnc
# so just from root lets find the successor or the predessor

def mindiff(root):
    def getMinimumDifference(self, root):

        def find_p(node):
            if not node or not node.left:
                return sys.maxsize
            node = node.left
            while node.right:
                node = node.right

            return node.val

        def find_s(node):
            if not node or not node.right:
                return sys.maxsize

            node = node.right
            while node.left:
                node = node.left
            return node.val

        def get_min(root):

            if not root: return sys.maxsize

            left = find_p(root)
            right = find_s(root)
            # print(left, right, root.val)

            if left == 0 and right == 0: return root.val
            if left == 0: return min(abs(root.val - right), min(get_min(root.left), get_min(root.right)))
            if right == 0: return min(abs(root.val - left), min(get_min(root.left), get_min(root.right)))

            return min(min(abs(root.val - right), abs(root.val - left)), min(get_min(root.left), get_min(root.right)))

        return get_min(root)