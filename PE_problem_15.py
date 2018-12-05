#Suppose that you have an nxn grid. How many ways can you get from the
#upperleft most position to the bottom rightmost position?
#THE ONLY MOVES YOU CAN MAKE ARE RIGHT AND DOWN.

#SOLUTION:
#This is a counting problem. Consider your grid of squares. Since
#we are always beginning and ending at the same spots, the number 
#of moves in each path are exactly the same. Moreover, if we have 
#an nxn grid of squares, we must move right and down exactly n times
#each. Thus what we are really counting is the number of ways we can
#permute a list of n R's and n D's.

#For example, a 1 x 1 grid is a square, and the available paths are
# D or R. For a 2 x 2 grid, the available paths are RRDD, RDRD, RDDR,
# DDRR, DRDR, DRRD

import math

#we are charged with finding the solution for n = 20
n = 20

#Let us first work as if we are permuting 20 x 2 objects without replacement
paths_raw = math.factorial(2*n)
print(paths_raw)

#However, each R and D are indistinguishable, so we need to divide out
#by the number of ways we can permute the Ds and Rs (separately)

repeats_R = math.factorial(n)
repeats_D = math.factorial(n)
paths_raw = paths_raw/repeats_D
paths = paths_raw/repeats_R
print(paths)

#Solution: 137846528820
