# This file generates a test set for the red0 problem
# I hit a TLE with my original solution and wrote this for testing purposes
# It can generate random inputs, or worst case * reps inputs


import random
f = open("red0test.txt", "w")

reps = 300000 # between 1 and 300000
strings = []
strings.append(str(reps) + "\n")

for _ in range(reps):
	# rand1 = random.randint(0, 10000) #2 * 10^18 is the limit for these
	# rand2 = random.randint(0, 2000000)
	
	# This is the worst case scenario
	rand1 = 1
	rand2 = 1152921504606846975

	strings.append(str(rand1) + " " + str(rand2) + "\n")

f.writelines(strings)