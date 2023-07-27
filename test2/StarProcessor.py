class StarProcessor(object):

	originalPhrase = ''
	explanations = ['Explanation: Performing the removal from left to right:']
	finalPhrase = ''

	def __init__(self, phrase):
		self.originalPhrase = self.cleanPhrase(phrase)
		self.removeStars(self.originalPhrase)
		self.exposeExplanation()

	def cleanPhrase(self, phrase):
	    if phrase.find('=') != -1:
	        return phrase.split("= ", 1).pop()

	    return phrase

	def removeStars(self, phrase, n = 1):
		ordinalNumber = self.getOrdinalString(n)
		starPosition = phrase.find('*')

		if (starPosition != -1):
			phraseList = list(phrase)
			phraseList.pop(starPosition)
			letter = phraseList.pop(starPosition-1)

			self.finalPhrase = ''.join(phraseList)
			self.explanations.append(f"The closest character to the {ordinalNumber} star is '{letter}' in {phrase}, s becomes {self.finalPhrase}")
			self.removeStars(self.finalPhrase, n+1)

		if (not phrase):
			self.explanations.clear()
			self.explanations.append('Explanation: The entire string is removed, se we return an empty string.')

	def exposeExplanation(self):
		print('Output: ', self.finalPhrase)

		for explanation in self.explanations:
			print('- ', explanation)

	def getOrdinalString(self, n):
		suffixes = {
			1: 'st',
			2: 'nd',
			3: 'rd' 
		}
		i = n if (n < 20) else (n % 10)
		return str(n) + suffixes.get(i, 'th')