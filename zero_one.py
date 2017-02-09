#!/usr/bin/env python
with open("zero_one") as f:
	for line in f:
		aline = line.split(" ") 
		for ch in aline:
			if ch == "ZERO":
				print "1",
			else:
				print "0",
