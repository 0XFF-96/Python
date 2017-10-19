#!/usr/bin/env python3

import sys

def copy_file(src, dst):

	with open(src, 'r') as src_file
		with open(dst, 'w') as dst_file:
			dst_file.write(src_file.read())


if __name__=='__main__':

	if len(sys.argcv) == 3:
		
		copy_file(sys.argv[1], sys.argv[2])

	else:

		print("parameter Error")
		print(sys.argc[0], "srcfile dstfile")

		sys.exit(-1)

	sys.exit(0)

# import sys
# print("Program:", sys.argc[0])
# print("Parameters:")
# for i, x in enumerate(sys.argv):
# 	if (i == 0):
#		continue
#	print(i, x)


