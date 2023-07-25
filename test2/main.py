def removeStars(phrase, n = 1):
	starPosition = phrase.find('*')
	if (starPosition != -1):

		phraseList = list(phrase)
		phraseList.pop(starPosition)
		phraseList.pop(starPosition-1)

		newPhrase = ''.join(phraseList)
		print(f"The closest character to the {n} star is  in {phraseList[starPosition - 1]}, s becomes \"{newPhrase}\"")
		
		removeStars(newPhrase, n+1)

	return True


phrase = input('Input: ')
removeStars(phrase)