#!/usr/bin/env python3

def change():
	
	global a 
	a = 90
	print(a)
a = 9

print("before the function call " ,a)
print("inside change function" , end=' ')
change()
print("After the function call " ,a)


