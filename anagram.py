from dictionary import csw19
from trie import *
import datetime

wordlist = TRIE(csw19)

def anagrammer(string, anagrams):
	# Make string lowercase in accordance with dictionary
	string = string.lower()
	predicate = ""
	anagramHelper(string, anagrams, predicate)
	

def anagramHelper(string, anagrams, predicate):

	found, count = wordlist.findPrefix(predicate)

	if found == False:
		return

	elif wordlist.findWord(predicate) == True:
		anagrams.append(predicate)

	for i in range(len(string)):
		# Add character to predicate
		predicate += string[i]
		# Remove added character from remaining string
		remainder = string[:i] + string[i+1:]
		anagramHelper(remainder, anagrams, predicate)
		# Remove character from predicate
		predicate = predicate[:-1]


# Function to check string formatting
def checkString(stringToCheck) -> bool:
	return stringToCheck.isalpha()


# Function to get valid input. Loops till a valid string is received. 
def getInput() -> str :

	string = input("Enter string: ")

	if string == "q":
		print("\nThank you for using fastanagrammer!\n")
		quit()

	while not checkString(string):
		string = input("Invalid string. Please enter a string with only alphabets: ")

		if string == "q":
			print("\nThank you for using fastanagrammer!\n")
			quit()

	return string

def main():
	print("\nWelcome to the fastest anagrammer! Enter the string of letters to anagram. Enter the letter q to quit.\n")

	string = getInput()

	while(string != "q"):
		anagrams = []

		startTime = datetime.datetime.now()
		anagrammer(string, anagrams)
		endTime = datetime.datetime.now()

		# Sort results to length
		anagrams = sorted(anagrams, key = lambda word: len(word))

		print(anagrams)
		print("\n{0} Results found in {1} seconds\n".format(len(anagrams), endTime - startTime))

		string = getInput()


if __name__ == '__main__':
	main()

