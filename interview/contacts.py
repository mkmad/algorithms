class suffixTree(object):

    class node():
        def __init__(self, data):
            self.data = data
            self.chidren = []

    def __init__(self):
        self.root = self.node(None)

    def insert(self, data):
        self.insert_val(self.root, data, index=0)

    def insert_val(self, node, data, index=0):
        exists = False
        if index > len(data) - 1:
            return
        if node:
            for child in node.chidren:
                if child.data == data[index]:
                    exists = True
                    self.insert_val(child, data, index=index + 1)
                    break

            if not exists:
                node.chidren.append(self.node(data[index]))

    def find(self, node=None, data=None, index=0):
        if not node:
            self.find(self.root, data=data, index=index)
        else:

            for child in node.chidren:
                if child.data == data[index]:
                    if index == len(data) - 1:
                        print(len(child.chidren))
                        return True
                    return self.find(node=child, data=data, index=index + 1)


def contacts(queries):
    #
    # Write your code here.
    #

    st = suffixTree()

    for q in queries:
        if q[0] == "add":
            st.insert(q[1])
        elif q[0] == "find":
            if not st.find(data=q[1]):
                print(0)


if __name__ == "__main__":
    print contacts(["add hack",
                    "add hackerrank",
                    "find hac",
                    "find hak"])
