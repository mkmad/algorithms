import populate_tree
from mycode.dsap.stackNQueue.queue import Queue as qq


class BFS(object):

    def __init__(self):
        self.queue = qq()

    def bfs(self, nodes=[]):
        if nodes:
            temp = []
            for i in nodes:
                print i.data,
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            self.bfs(temp)

    def bfs_iterative(self, node):
        """
        I missed all the preliminary base conditions,
        I enqueued node.left instead of cur.left.
        I checked for node.left instead cur.left
        WTF!!!!!


        The difference here is I can just maintain one queue
        and adding/removing from that, unlike having two
        arrays in recursive function
        """
        if node:
            self.queue.enqueue(node)
        while not self.queue.is_empty():
            cur = self.queue.dequeue()
            print cur.data,
            if cur.left:
                self.queue.enqueue(cur.left)
            if cur.right:
                self.queue.enqueue(cur.right)

    def print_bfs(self):
        print 'Recursive'
        self.bfs([populate_tree.populate()])
        print '\nIterative'
        self.bfs_iterative(populate_tree.populate())


if __name__ == '__main__':
    b = BFS()
    b.print_bfs()