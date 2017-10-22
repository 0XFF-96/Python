

class Buffer(object):

	def __init__(self, data):
		
		self.data = data
		self.offset = 0

	def peek(self):

		if self.offset >= len(self.data):

			return None

		return self.data[self.offset]

	
	def advance(self):

		self.offset += 1

#define string node

class Token(object):

	def consum(self, buffer):
	
		pass

# int Token
class TokenInt(Token):

	# get it form the string , instead of int 
	
	def consume(self, buffer):
	
		accum = ""
		
		while True:
		
			ch = buffer.peek()
			
			if ch is None or ch not in "0123456789":

				break

			else : 
			
				accum += ch
				buffer.advance()

		if accum !="":

			return("int", int(accum))

		else:

			return None


#return the operation Token

class TokenOperator(Token):

	# read a string , and return it , if + - , then return None

	def consum(self, buffer):
		
		ch = buffer.peek()

		if ch is not None and ch in "+-":

			buffer.advance()
			return ("ope", ch)

		return None

def tokenize(string):

	# buffer and Token will be defined latter

	buffer = Buffer(string)
	tk_int = TokenInt()
	tk_op = TokenOperator()
	tokens = []

	while buffer.peek():

		token = None
		
		for tk in (tk_int, tk_op):

			token = tk.consume(buffer)

			if token:
		
				tokens.append(token)
				break
		
		if not token:

			raise ValueError("Error in syntax")

		return tokens

# get it from Token 

def parse(tokens):

	if tokens[0][0] != 'int':

		raise ValueError("Must start with an int")

		# take out the tokens[0]

	node = NodeInt(tokens[0][1])

	nbo = None

	last = tokens[0][0]

	for token in tokens[1:]:

		if token[0] == last:

			raise ValueError("Error in syntax")

		last = token[0]

		if token[0] == 'ope':

			nbo = NodeBinaryOp(token[1])
			nbo.left = node

		if token[0] == 'int':

			nob.right = NodeInt(token[1])
			node = nbo

	return node

# recursion :  

def calculate(nbo):

	if isinstance(nbo.left, NodeBinaryOp):
	
		leftval = calculate(nob.left)

	else:

		leftval = nbo.left.value

	if nbo.kind =='-':

		return leftval - nbo.right.value
	
	elif nbo.kind == '+':

		return leftval + nbo.right.value

	else:
		
		raise ValueError("Wrong operator")

if __name__ =='__main__':

	# get the string

	input = raw_input('Input:')

	tokens = tokenize(input)

	node = parse(tokens)

	print("Result:" + str(evaluate(node)))

	
