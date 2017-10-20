from multiprocesssing import Pool

def f(i):

	print(i, end=' ')

def main():

	# intialize the 3 pooling 

	pool = Pool(processes=3)

	for i in range(30):

		# apply the method to process the task

		pool.apply(f, (i,))

if __name__=='__main__':
	
	main()


