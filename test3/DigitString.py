class DigitString(object):

	def __init__(self, digitString):
		self._beginCount(int(digitString))

	def _beginCount(self, n):
		numbers = '1'
		for i in range(1, n):
			numbers = self.count(numbers)
		
		final = self.count(numbers)

	def count(self, stringNumbers):
	    countResult = ""
	    numberCount = {}
	    outputString = ''
	     
	    for i in range(len(stringNumbers) + 1):
	        if i == len(stringNumbers) or stringNumbers[i] not in numberCount and i > 0:
	            countResult += str(numberCount[stringNumbers[i-1]]) + stringNumbers[i-1]
	            outputString += f"hay {str(numberCount[stringNumbers[i-1]])} {stringNumbers[i-1]}s,"
	            numberCount.clear()
	             
	        if i == len(stringNumbers):
	            numberCount[None] = 1
	        else:
	            if stringNumbers[i] in numberCount:
	                numberCount[stringNumbers[i]] += 1
	            else:
	                numberCount[stringNumbers[i]] = 1
	    
	    print(outputString)
	    return countResult






