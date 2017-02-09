#!/usr/bin/env python
import binascii
with open("zero_one.txt") as f:
	data=f.read().replace(" ", "")
	n = int(data, 2)
	print binascii.unhexlify('%x' % n)
