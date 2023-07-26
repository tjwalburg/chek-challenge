class ExpressionSolver(object):

	def __init__(self, pathFile):
		self.pathFile = pathFile
		self.expressionsList = []
		self.priority = {
			'+': 1,
			'-': 1,
			'*': 2,
			'/': 2
		}

		self.openBracketsList = {'(', '[', '{'}
		self.closeBracketsList = {')', ']', '}'}
		self.operatorsList = {'+', '-', '*', '/'}

		self.begin()


	def begin(self):
		self.readFile()
		self.beginSolver()

	def readFile(self):
		expressionsFile = open(self.pathFile, 'r')

		for line in expressionsFile.readlines():
			self.expressionsList.append(line)	

		expressionsFile.close()

	def beginSolver(self):
		for expression in self.expressionsList:
			expressionWithoutTrail = expression.rstrip('\n')
			try:
				result = self.createDataStructureForExpression(expressionWithoutTrail)
				print(f'The result for \"{expressionWithoutTrail}\" is', result)
			except Exception as e:
				print(f'The expression \"{expressionWithoutTrail}\" produces a SyntaxError')

	def evaluateExpression(self):
		operator = self.argumentsList.pop()
		b = int(self.numbersList.pop())
		a = int(self.numbersList.pop())

		if (operator == '+'):
			self.numbersList.append(a + b)
		elif operator ==  '-':
			self.numbersList.append(a - b)
		elif operator == '*':
			self.numbersList.append(a * b)
		else:
			self.numbersList.append(a/b)
	

	def createDataStructureForExpression(self, expression):
		self.argumentsList = []
		self.numbersList = []
		expressionToken = self.createListByExpression(expression)
		
		for token in expressionToken:
			if (token in self.openBracketsList):
				self.argumentsList.append(token)

			elif isinstance(token, int):
				self.numbersList.append(token)

			elif token in self.operatorsList:
				if (self.argumentsList and self.argumentsList[-1] in self.operatorsList and self.priority[self.argumentsList[-1]] >= self.priority[token]):
					self.evaluateExpression()
				self.argumentsList.append(token)

			elif token in self.closeBracketsList:
				self.evaluateExpression()
				if (self.argumentsList[-1] in self.openBracketsList):
					self.argumentsList.pop()


		while self.argumentsList:
			self.evaluateExpression()

		return self.numbersList.pop()

	def createListByExpression(self, expression):
		expressionList = []
		index = 0

		while index < len(expression):
			tokenToAdd = expression[index]
			if (expression[index].isdigit()):
				subIndex = index
				while subIndex < len(expression) and expression[subIndex].isdigit():
					subIndex += 1
				tokenToAdd = int(expression[index:subIndex])
				index = subIndex
			else:
				index += 1
			
			expressionList.append(tokenToAdd)

		return expressionList


		


