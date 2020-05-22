class LinkedTree:
    def __init__(self, root):
        self.key = root
        self.children = []

    def insert_node(self, new_node, verbose=False):
        if self.children == None or verbose:
            self.children.append(LinkedTree(new_node))
        else:
            t = LinkedTree(new_node)
            t.children = self.children
            self.children.append(t)

    def get_children(self, ind):
        return self.children[ind]

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key
