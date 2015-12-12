







def incrementDigitRecursive(word, digit):
	if word[digit] == 'z':
		word[digit] = 'a'
		incrementDigitRecursive(word, digit - 1)
	else:
		word[digit] = chr(ord(word[digit]) + 1)

	return word


def increment(word):
	n = len(word) - 1
	return incrementDigitRecursive(word, n)

def isStraight(word, digit):
	ret = True
	ret = ret and ord(word[digit + 1]) == (ord(word[digit + 0]) + 1)
	ret = ret and ord(word[digit + 2]) == (ord(word[digit + 1]) + 1)
	return ret

def hasStraight(word):
	ret = False
	for n in range(0, len(word) - 3):
		ret = ret or isStraight(word, n)
	return ret

def allValidChars(word):
	ret = True
	for c in word:
		ret = ret and (c != 'i')
		ret = ret and (c != 'l')
		ret = ret and (c != 'o')
	return ret

def isPair(word, digit):
	return (word[digit] == word[digit + 1])

def has2DisjointPairs(word):
	pairCount = 0
	n = 0
	while n < len(word) - 1:
		if isPair(word, n):
			pairCount += 1
			n += 1
		n += 1
		
	return (pairCount >= 2)




def findSolution(word):
	success = False
	while not success:
		success = True
		word = increment(word)
		success = success and hasStraight      (word)
		success = success and allValidChars    (word)
		success = success and has2DisjointPairs(word)
	return word



def main(word):
	answer = "".join(findSolution(list(word)))
	print "%s --> %s" % (word, answer)


main("hepxcrrq")
main("hepicrrq")
