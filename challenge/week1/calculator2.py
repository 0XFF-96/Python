#!/usr/bin/env python3
import sys

# exception handing

	

# you should igrone the first parameter of sys
#def get_salary(argv):
#
#	
#	for item in argv:
#	
#		try:		
#			
#			num, salary = item.split(':')
#			salary = int (salary)
#		
#		except: ValueError:
#
##			print("parameter error")
#	
#
#def insurance(salary):

#	sal_after_insurance = salary - salary * ( 0.08 + 0.02 + 0.005 + 0.06) -3500

#	return sal_after_insurance 


			
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

	print(str(item).join(":"),format(int(tax_value),".2f"))



	
save_data = {}
i = 1	
while i <= (len(sys.argv)-1):
	try:	
		get_worker_salary = sys.argv[i]
		num,wage =get_worker_salary.split(':')		
		int_wage = int(wage)	
		basic_wage = int(wage) -int(wage) * (0.08 + 0.02 +
							 0.005 + 0.06) -3500
	except ValueError:

		print("parameter Error")
#calcuator the wage
		
	tax = calculator(basic_wage)	
	##save the result in key-value dict
	salary_after_tax =int_wage - tax -int_wage * (0.08 +0.02
						+ 0.005 + 0.06)
	
	save_data[num] = tax
# test code	
#	print(wage)
#	print(basic_wage)
#	print(tax)
#	print(int_wage * (0.08 + 0.02 + 0.005 + 0.06))
#	show_tax(num, tax)
#	print(salary_after_tax)
#	print('------')	

#	show_tax(num, salary_after_tax)
	print(num + ':'+ str(format(salary_after_tax,".2f")))	
	i +=1


# print the result 
#for value, item in save_data.items():
		
#	show_tax(item, value)



	
	
