#!/usr/bin/env python3

def char_count(str):
	char_list = set(str)

	for char in char_list:
		print(char, str.count(char))

if __name__=='__main__':
	
	s = input("Enter a string:")

	char_count(s)

