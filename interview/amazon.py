import math


class Interview(object):

    def __init__(self):
        pass




    def nearestVegetarianRestaurant(self, totalRestaurants, allLocations, numRestaurants):
        # WRITE YOUR CODE HERE

        allLocations_sorted = sorted(allLocations, key=lambda x: math.sqrt(x[0] ^ 2 + x[1] ^ 2))

        print allLocations_sorted
        return allLocations_sorted[:numRestaurants]


if __name__ == '__main__':
    i = Interview()
    print i.nearestVegetarianRestaurant(3, [[1, -3], [1, 2], [3, 4]], 1)
