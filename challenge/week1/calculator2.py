#!/usr/bin/env python3
import sys

# exception handing

	
if not ((sys.argv[1])) :
	print("parameter Error")



	 

def calculator (basic_wage):
		

	if basic_wage <= 0:
			tax_value = 0

	elif basic_wage <= 1500:
			tax_value = basic_wage * 0.03 

	elif basic_wage <= 4500:
		tax_value = basic_wage * 0.1 -105

	elif basic_wage <=9000:
		tax_value = basic_wage * 0.2 -555
		
	elif basic_wage <=35000:
		tax_value = basic_wage * 0.25 -1005

	elif basic_wage <=55000:
		tax_value = basic_wage * 0.30 -2755

	elif basic_wage <=80000:
		tax_value = basic_wage * 0.35 -5505

	else :
		tax_value = basic_wage * 0.45 -135505

	return tax_value

def show_tax(item, tax_value):

	print(str(item) + ':' + str(tax_value))



	
	save_data = {}
	
for i in (len(sys.argv)-1):
		
	get_worker_salary = sys.argv[i+1]
	num,wage =get_worker_salary.split(':')		

	basic_wage = int(wage) -int(wage) * (0.08 + 0.02 +
						 0.005 + 0.6) -3500
		
	tax = calculator(basic_wage)
	
	##save the result in key-value dict

	save_data[num] = tax


	# print the result 
for value, item in save_data.items():
		
	show_tax(item, value)



	
	
