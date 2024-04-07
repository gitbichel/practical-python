# bounce.py
#
# Exercise 1.5
height = [(3/5)**i * 100 for i in range(11)]

for i in range(1, 11):
	print(i, round(height[i], 4))

