#!/usr/bin/env python3
import sys

if type(sys.argv[1]) != type(1):
	print("parameter Error")

var = int(sys.argv[1])


if var <= 1500:
	print(0,".2f")

elif var <= 3500:

	print( (var-3500)*0.1,".2f")

elif var <= 4500:

	print( (var-3500)*0.1,".2f")

elif var <=9000:

	print( (var-4500)*0.2 + 105)

elif var <=35000:

	print( (var-9000)*0.25 + 1005)

elif var <=55000:

	print( (var-35000)*0.3 +2755)

elif var <=80000:

	print( (var-55000)*0.35 + 5505)

else :

	print( (var-80000)*0.45 + 13505)

