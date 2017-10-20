from multiprocessing import Pipe , Process

conn1, conn2 = Pipe()


def f1():
	
	conn1.send('Hello shiyanlou')

def f2():
	
	data = conn2.recv()
	print(data)

def main():

	Process(target=f1).start()
	Process(target=f2).start()

if __name__ == '__main__':

	main()

	

