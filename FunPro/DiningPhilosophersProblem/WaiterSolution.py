


## Synchronization create problem !!

import threading
from time import sleep
import os, random 

# 
numPhilosophers = numForks = 2

class Philosopher(threading.Thread):

	def __init__(self, index):

		threading.Thread.__init__(self)
		self.index = index
		self.leftFork = forks[self.index]
		
		self.rightFork = forks[(self.index + 1) % numForks]

	def run(self):

		while True:

			if waiter.serve(self):

				self.dinning()
				waiter.clean(self)

			self.thinking()
	

	def dinning(self):

		print "philosopher", self.index, " starts to eat."

		sleep(random.uniform(1, 3)/1000)

		print "Philosopher", self.index, " finishes eating and leaves to think"

	
	def thinking(self):

		sleep(random.uniform(1,3)/1000)

class Fork():

	def __init__(self, index):

		self.index =index
		self._lock = threading.Lock()

	def pickup(self):
		
		self._lock.acquire()

	def putdown(self):

		self._lock.release()

class Waiter:
	
	def __init__(self):
	
		self.forks = [Fork(idx) for idx in range(numForks)]

		self.forks_using = [False] * numForks

	def serve(self, philor):

		if not self.forks_using[philor.leftFork.index] and not self.forks_using[philor.rightFork.index]:

			self.forks_using[philor.leftFork.index] = True
			self.forks_using[philor.rightFork.index] = True
	
			self.forks[philor.leftFork.index].pickup()
			self.forks[philor.rightFork.index].pickup()

			return True
		else:
		
			return False

	def clean(self, philor):

		self.forks[philor.leftFork.index].putdown()
		self.forks[philor.rightFork.index].putdown()
		
		self.forks_using[philor.leftFork.index] = False
		
		self.forks_using[philor.rightFork.index] = False

	
			

if __name__=='__main__':

	waiter = Waiter()

	forks = [Fork(idx) for idx in range(numForks)]

	philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

	#open all the threading for philosopher

	for philosopher in philosophers:

		philosopher.start()

	try:

		while True : sleep(0.1)

	except Exception, e:
		
		raise e

	


























