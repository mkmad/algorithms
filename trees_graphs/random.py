import bst_functions
import random

class findRandom():
    def __init__(self):
        pass

    def build_tree(self):
        #Build tree by importing bst_functions
        pass

    def choose_random(self, root, N):
        # Total number of Nodes
        # Probability of choosing root = 1/N
        # Probability of choosing left child = Left_SIZE * 1/N
        # Probability of choosing right child = RIGHT_SIZE * 1/N
        # Total probability = 1/N (1 + LEFT_SIZE + RIGHT_SIZE)
        probability_dict = \
            {
                root.left.size / N : root.left,
                root.right.size / N : root.right,
                1/N : root
            }
        probT = (1 + root.left.size + root.right.size) / N
        # Roll the dice now
        choice = random.randomint(0,probT)
        # This is to sort all the probabilities in
        # increasing order.

        ordered_p = sorted(probability_dict.keys())
        if choice < ordered_p[0]:
            final = probability_dict[ordered_p[0]]
        elif choice < ordered_p[1]:
            final = probability_dict[ordered_p[1]]
        else:
            final = probability_dict[ordered_p[-1]]

        if final == root:
            return root
        else:
            self.choose_random(final, N)