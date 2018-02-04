class DetectCycle(object):

    class Node(object):

        def __int__(self):
            self.data = None
            self.next = None

    def __int__(self):
        self.head = None

    def populate_linked_lisk_with_cycle(self):
        """
        Building this linked list:

        1 -> 2 -> 3 -> 4 -> 5 -> 6  -> 7
                       ^               |
                       |               v
                      11 <- 10 <- 9 <- 8
        """
        self.head = self.Node()
        self.head.data = 1

        loop_node = None
        cnt = 2
        cur = self.head

        while cnt < 12:
            n = self.Node()
            n.data = cnt
            cur.next = n

            if cnt == 4:
                loop_node = n

            cnt += 1
            cur = n

        cur.next = loop_node

        print cur.data
        print cur.next is loop_node
        print loop_node.data

    def find_collision(self):
        """
        Have two pointers, slow and fast. Move slow
        one step at a time and fast two steps at a time
        When they collide the move slow back to head (
        don't change the fast) and move both one step
        at a time. This time when they collide, then that
        is the starting point of the loop

        Note: Its import to initialize both slow and fast to
        head first. I did slow = head and fast = head.next.next
        and that didn't work out

        """
        slow = self.head
        fast = self.head

        while slow is not fast or slow is self.head:
            slow = slow.next
            fast = fast.next.next

        print 'Collision point'
        print slow.data

        slow = self.head

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        print 'Start of the loop'
        print slow.data

    def detect_cycle(self):
        self.populate_linked_lisk_with_cycle()
        self.find_collision()


if __name__ == '__main__':
    d = DetectCycle()
    d.detect_cycle()
