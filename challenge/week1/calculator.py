#!/usr/bin/env python3
import sys

if (len(sys.argv)-1) >= 2:

	print("parameter Error")
if not (int(sys.argv[1])) :
	print("parameter Error")

try:
	basic_wage = int(sys.argv[1]) - 3500

	if basic_wage <= 0:
		tax_value = 0
		print(format(tax_value,".2f"))

	elif basic_wage <= 1500:
		tax_value = basic_wage * 0.03
		print(format(tax_value,".2f"))
	elif basic_wage <= 4500:
		tax_value = basic_wage * 0.1 - 105
		print(format(tax_value,".2f"))
	elif basic_wage <=9000:
		tax_value = basic_wage * 0.2 -555
		print(format(tax_value,".2f"))
	elif basic_wage <=35000:
		tax_value = basic_wage * 0.25 -1005
		print(format(tax_value,".2f"))
	elif basic_wage <=55000:
		tax_value = basic_wage * 0.30 -2755
		print(format(tax_value,".2f"))
	elif basic_wage <=80000:
		tax_value = basic_wage * 0.35 -5505
		print(format(tax_value,".2f"))
	else :
		tax_value = basic_wage * 0.45 -135505
except :
	pass 
