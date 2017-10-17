#!/usr/bin/env python3

#filename = input("Enter file path:")

#f = open(filename)

#try:
#	f = open(filename)
#	printf(f.read())
#	f.close()
#except FileNotFoundError:
#	print("File not found")


filename = '/etc/protocols'
f = open(filename)

try:
	f.write('shiyanlou')
except:
	print("File write error")
finally:
	print("finally")
	f.close()


