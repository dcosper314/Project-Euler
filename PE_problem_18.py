# Imagine we have a binary tree with positive integers at each node
# Begining at the top of the tree, we can form a path down the tree and
# use the integers from each node passed to form a sum.
# Find the path with the largest sum in the given tree.

# Example of binary tree with three levels
#			45
#		32		67
#	14		24		97
#
# So begining at 45, we can choose a path through 32 or 67.
# If we choose, say, 32, we can then continue our path through 14 or 24.
# In this example it is clear that there are 4 possible paths.

# SOLUTION:
import csv

with open('pe_18_binary_tree.csv') as csvfile:
	f = csv.reader(csvfile,delimiter=' ')
	tree = []
	for row in  f:
		tree = tree + [row]
# This will pull the binary tree for problem 18


for i in range(0,len(tree)):
	for j in range(0,len(tree[i])):
		tree[i][j] = int(tree[i][j])
# The tree contains str; this statement changes entries to int type.


def max_path_sum(n):
	# This will give the optimal path sum.
	while len(n) > 1:
		newrow = []
		for x in range(len(n[-2])):
			newrow = newrow + [max(n[-2][x] + n[-1][x],
			n[-2][x] + n[-1][x+1])]
		n = n[0:len(n)-2] + [newrow]
	return n[0][0]

print(max_path_sum(tree))

# Answer: 1074

# Mathematical notes: The number of potential paths grows at 
# a rate of 2**x, where x is one less than the total number of rows.
# This number increases rather fast, so that for large numbers of 
# rows it will be unreasonable to sum along all paths. So we must find
# a more effecient method.

# This solution requires some explanation. What we will do is 
# work from the bottom of the tree. Consider the penultimate row.
# From every entry on this row, there are exactly two paths.
# We select the optimal path through this node, and add that value
# to get a new penultimate row.

# In the example preceeding the code, we had the tree
#			45
#		32		67
#	14		24		97

# Here the penultimate row is the row 32 67
# From 32, the best path to take will be through 24
# From 67, the best path will be through 97
# Thus we devise an updated tree by adding 24 to 32 and 97 to 67.

# Doing so gives us a new tree
#			45
#		56		164

# Next we do the same thing with the penultimate row of the new tree.
