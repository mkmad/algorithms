class SuffixTree(object):
    """
    Create all possible suffixes and add them to tri

    eg:

    minimize ->
    inimize
    nimize
    imize
    mize
    ize
    ze
    e

    for each of these indices, check if there is a
    match on the first letter to any of the node's
    children. If there is a match, then move on to
    that child and check the next letter for match
    and so on

    If there is no match (in any level of the tree)
    then create a child node and add it to the node's
    children

    Later, compress the suffix tree on nodes that
    have only one child

    Note: root will have no data/label and it will
          not take part in compression
    """

    class Node:
        def __init__(self):
            self.children = []
            self.label = ''

    def __init__(self):
        self.word = list('minimize')
        # adding sentinel char
        self.word.append('$')
        self.root = None

    def build_suffixes(self):
        """
        Create all possible suffixes and call build suffixes:

        minimize
        inimize
        nimize
        imize
        mize
        ize
        ze
        e

        """
        for i in range(len(self.word)):
            self.suffix(self.word[i:], self.root)

    def suffix(self, word, root=None, index=0):
        """
        For a given array, check if the first element is
        the first char of any child, if it is then move
        on to the next char and the child's child recursively.
        Its basically saying there is already a suffix in the sub
        tree that starts with that character


        If the first element is not the beginning of any child
        then create a child node with the char as the label


         Note: Since we are moving to the child's levels recursively
               you need to make sure as to which root you are passing
               to the recursive call. I messed it up couple of times


        """
        if index < len(word):

            # If root doesn't exist
            if not root:
                node = self.Node()
                child_node = self.Node()
                child_node.label = word[index]
                node.children.append(child_node)
                self.root = node
                # move on to the child you just created with
                # the next index
                # TODO: The next root is child_node
                self.suffix(word, root=child_node, index=index + 1)

            else:
                if root.children:
                    # keep track if there is a match for the suffix
                    # is true or false. I use this since L111 might
                    # come back and I don't want to accidentally
                    # execute L116 after executing L111
                    match = False

                    # Check if there is a suffix that starts with
                    # word[index] in any of the child's first char
                    for val in root.children:
                        if word[index] == val.label[0]:
                            match = True
                            if index < len(word) - 1:
                                # move on to the matched child with
                                # the next index
                                # TODO: The next root is val
                                self.suffix(word, root=val, index=index + 1)

                    if not match:
                        # create a child since a match for the suffix
                        # was not found
                        node = self.Node()
                        node.label = word[index]
                        root.children.append(node)
                        # move on to the child you just created with
                        # the next index
                        # TODO: The next root is node
                        self.suffix(word, root=node, index=index + 1)
                else:
                    # Since the root has no children, create a child
                    node = self.Node()
                    node.label = word[index]
                    root.children.append(node)
                    # move on to the child you just created with
                    # the next index
                    # TODO: The next root is node
                    self.suffix(word, root=node, index=index + 1)

    def compress(self, root):
        # compress a node if it has only one child, also set the
        # label so we can see which nodes are compressed
        if root:
            if len(root.children) == 1:
                root.label += root.children[0].label
                root.children = root.children[0].children
                # TODO: note:-
                # Note, call recursively with root or else
                # you'll end up with just compressing the
                # root and the immediate child and not the
                # grandchildren
                self.compress(root)

            for val in root.children:
                self.compress(val)

    def compress_tree(self):
        # Need to call compress from root's children
        # because root has no data and will not take part in
        # compression
        if self.root:
            for val in self.root.children:
                self.compress(val)

    def return_root(self):
        return self.root


if __name__ == '__main__':
    st = SuffixTree()
    st.build_suffixes()
    st.compress_tree()
    root = st.return_root()
    print root