#Co-Authors: Devin Fan & Sophia Chen

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

color_names = []
all_diffs = []
with open(colorfile) as fp:
	for line in fp:
		colors = line.split()
		color_names.append(colors[0])
		vals = colors[2]
		vals = vals.split(',')
		red = int(vals[0])
		green = int(vals[1])
		blue = int(vals[2])
		total_diff = abs(red - R) + abs(green - G) + abs(blue - B)
		all_diffs.append(total_diff)
	min_diff = 765
	for color, diff in zip(color_names, all_diffs):
		if diff < min_diff:
			min_diff = diff
			min_color = color
	print(f'The closest color is {min_color} with a value of {min_diff}.')
