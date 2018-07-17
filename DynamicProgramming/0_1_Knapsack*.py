class Knapsack(object):
    """
        In 0/1 knapsack, we are given a bag of a particular weight and
        a list of items. Each item has a weight and a value

        Goal is to carry maximum number of items which gives the maximum
        total value. Also note, once an item is selected then we can't
        reselect the item again

        Solution:

        1. Initialize a 2D array where column ranges from 0 to max bag weight
           and row has the weights of all the items

        2. For the first row, if the column weight is greater or equal to the
           row weight, then pick the item in the row and update the value
           of matrix[row][weight] to the value of the item

           For all other rows, if the column weight is greater or equal to the
           row weight, then we have two choices:

                1. pick the item and add the value of the item to the value
                   of matrix[row - 1][column - wt of the item], i.e the remain
                   weight's value

                or

                2. Don't pick the item, in which case we chose the value of
                   matrix[row - 1][column], i.e the value that's previously
                   calculated for this column


        Some important insights when dealing with 2D array:

            1. Note how 2D arrays are created
            2. Note how 2D arrays are iterated (how i and j move)
            3. Note how we subscript the array, i.e matrix[row][column]
               in the below example its matrix[j][i]

        These were some of the mistakes I made ^^

        Problem specific insights:

            1. We need padding for columns (an extra column of 0's in
               the beginning) because we need i (the column variable) to
               go all the way from 0 till max weight else we have to
               subtract 1 from each weight of the item from the items
               array to ensure i doesn't overflow
            2. We don't need padding for j (the row variable) because we are
               only going to iterate through the length of the items array


    """

    def __init__(self):
        self.max_weight = 7

        # items is a list of tuples that holds
        # (weight, value)
        self.items = [(1, 1), (3, 4), (4, 5), (5, 7)]

        """
            Note: You shouldn't create 2D array like this
            
                self.matrix = [[0] * (self.max_weight + 1)] * len(self.items)
            
            Say for example if :
            
                a = [[0] * 5] * 4
                
                this means a is a list of 4 objects of the same references, 
                hence if you set a single value in any row/column then
                values in all rows and columns will be changed
                
                for eg:
            
            
                    In [8]: a
                    Out[8]: [   
                                [0, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 0], 
                                [0, 0, 0, 0, 0]
                            ]
        
                    In [9]: a[0][1] = 5
        
                    In [10]: a
                    Out[10]: [
                                [0, 5, 0, 0, 0], 
                                [0, 5, 0, 0, 0], 
                                [0, 5, 0, 0, 0], 
                                [0, 5, 0, 0, 0]
                            ]

            Therefor you need to create a 2d array like this:
             
                a = [[0] * 5] for _ in range(4)]
                
            The above statement will create 4 different values of the
            list ^^

        """

        self.matrix = [[0] * (self.max_weight + 1) for _ in range(len(self.items))]

    def solution(self):

        # TODO: i goes from left to right (column)
        # TODO: j goes from top to bottom (row)

        # TODO: Note how we iterate row first and then column
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix[0])):
                # For rows > 0
                if j > 0:
                    # If we can pick the item
                    if i >= self.items[j][0]:
                        # max value we get either by picking the item or not
                        # picking the item
                        self.matrix[j][i] = max(
                            self.items[j][1] + self.matrix[j - 1][i - self.items[j][0]],
                            self.matrix[j - 1][i]
                        )
                    # If we can't pick the item
                    else:
                        self.matrix[j][i] = self.matrix[j - 1][i]
                else:
                    # For the first row (the 0'th row)
                    if i >= self.items[j][0]:
                        self.matrix[j][i] = self.items[j][1]

        return self.matrix


if __name__ == '__main__':
    k = Knapsack()
    for val in k.solution():
        print val
