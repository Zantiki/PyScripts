import math


def pi_archimedes():
    # Half the amount of polygon sides we wish to make up our approximation of the circumference
    # Chose 14 for tested accuracy
    our_iterable = range(14)
    # Variables describing our starting polygon as a square.
    pg_edge_length_squared = 2.0
    tot_pg_sides = 4

    # To get each iteration in this loop we can also call iter(our_iterable).next()
    for iteration in our_iterable:
        # Resize the polygon edge
        pg_edge_length_squared = 2 - 2 * math.sqrt(1 - pg_edge_length_squared / 4)
        # Adjust the total sides for the new polygon edges.
        tot_pg_sides *= 2

    # Returns the value of pi by the formula C/2r where the product of our variables
    # is an approximation of C.
    return tot_pg_sides * math.sqrt(pg_edge_length_squared) / 2


pi = pi_archimedes()
print("Our approximation:    {}".format(round(pi, 7)))
print("Common approximation: 3.1415926")
