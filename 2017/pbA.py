################################
# Oversized Pancake Flipper
# coded by 	: ajubin
# date		: 18 april 2017
################################

'''
	PROBLEM : 
	given a number of pancakes with 2 differents sides (drawn one "+" and empty one "-") and a pan that can only flip k consecutive pancakes,
	we have to find the minimum number of flips to perform with the pan to make all pancakes have their drawn faces visible.

	INPUT  : '+---+++--+++' 5
	
	SOLUTION : Recursive solution
	the pancakes are represented as a list of boolean, True:"+", using list comprehension
	starting from the left of the list, remove all consecutives pancakes that are well faced
	flip the k following pancakes (at least the first one of the new list not facing good) 
	Exit condition :
		- Every pancakes face good
		- The remaining number of pancakes is too low to be flipped with the given pan
'''

def solution(Blist, k, count):
	i = 0
	n = len(Blist)

	while(i < n and Blist[i]):
		i += 1
	new_Blist = Blist[i:]
	
	# Exit condition
	if not new_Blist:
		return count

	# Exit condition
	if k>n-i:
		return "IMPOSSIBLE"

	# flip the new k first pancakes and increase the flipcount
	for i in range(0,k):
		new_Blist[i] = not new_Blist[i]

	return solution(new_Blist, k, count+1) 



if __name__ == "__main__":
	import sys
	import fileinput
	
	sys.setrecursionlimit(10000) # to avoid maximum recursion depth error with the large test set
	lcount = 0
	
	for line in fileinput.input():
		args = line.split()
		if len(args) == 2:
			lcount += 1
			Blist = [b=="+" for b in args[0] ]
			pan = int(args[1])
			res = solution(Blist, pan, 0)
			print("Case #{}: {}".format(lcount, res))
