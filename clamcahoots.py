#!/usr/bin/python
import sys
import math

class clamCahoots:
	
	a = open(sys.argv[1], "r")
	clam_map = {}
	grid_size = int(sys.argv[2])
	prefix = sys.argv[1].split(".") 
	out_file = prefix[0] + "_lacunarity." + prefix[1]
	b = open(out_file, "w")
	
	b.write("Box Size\tLacunarity\tLog(Box Size)\tLog(Lacunarity)\tMean\tVariance\n")

	for i in xrange(grid_size):
	   for j in xrange(grid_size):
	      clam_map[(i,j)] = 0

	for line in a:
		clam_location = line.split()
		cor = 0 
		count = 0
		
		for rnge in xrange(len(clam_location)/2):
			
			xcor = clam_location[cor]
			ycor = clam_location[cor+1]
			clam_map[( int(xcor), int(ycor) )] = 1 
			cor += 2


	for r in xrange(grid_size):
		N = 0.
		mean = 0.
		variance = 0.
		locaunarity = 0.
		box_counts = []
		total_count = 0.
		for i in xrange(grid_size-r):
			for j in xrange(grid_size-r):
				count = 0.
				for x in xrange(1+r):
					for y in xrange(1+r):
						if clam_map[(i+x,j+y)] == 1:
							count += 1
				N += 1
				box_counts.append(count)
				total_count += count

	
		mean = total_count / N
	
		for i in xrange(len(box_counts)):
			box_variance = (((box_counts[i] - mean) ** 2 ) ** 0.5) ** 2 
			variance += box_variance

		variance = variance / N
	
		lacunarity = (variance / (mean **2 )) + 1
	
		b.write( str(r+1) + "\t" + str(lacunarity) + "\t" + str(math.log(r+1)) + "\t" + str(math.log(lacunarity)) + "\t" + str(mean) + "\t" + str(variance) + "\n")

			
				