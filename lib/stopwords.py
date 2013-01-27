def stopwords():
	words = open('../lib/stopwords.txt', 'r').read().strip().split('\n')
	wordDict = {}
	for word in words:
		wordDict[word] = word
	return wordDict



