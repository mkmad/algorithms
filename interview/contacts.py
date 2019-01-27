class suffixTree(object):

    """
    Provide a data Structure for finding all possible
    words that start with a given substring

    eg:

        If the words are "hack" and "hackerrank" and the
        search string is "hac" then you are supposed to
        return "hack" and "hackerrank"



    """

    class node():
        def __init__(self, data):
            self.data = data
            self.chidren = []
            self.number_children = 0

    def __init__(self):
        self.root = self.node(None)
        self.count = 0

    def insert(self, data):
        self.insert_val(self.root, data, index=0)

    def insert_val(self, node, data, index=0):
        exists = False
        if index > len(data) - 1:
            return

        if node:
            if node.chidren:
                for child in node.chidren:
                    if child.data == data[index]:
                        exists = True
                        self.insert_val(child, data, index=index + 1)
                        break

                if not exists:
                    child = self.node(data[index])
                    node.chidren.append(child)
                    self.insert_val(child, data, index=index + 1)

            else:
                child = self.node(data[index])
                node.chidren.append(child)
                self.insert_val(child, data, index=index + 1)

    def find(self, node=None, data=None, index=0):
        if not node:
            self.find(self.root, data=data, index=index)
        else:

            for child in node.chidren:
                if child.data == data[index]:
                    if index == len(data) - 1:
                        self.count_words(child)
                        print self.count
                        return True
                    return self.find(node=child, data=data, index=index + 1)

    def count_words(self, node):

        if node:
            if node.chidren:
                for child in node.chidren:
                    self.count_words(child)
            else:
                self.count += 1


def contacts(queries):
    #
    # Write your code here.
    #

    st = suffixTree()

    for val in queries:
        q = val.split()
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
