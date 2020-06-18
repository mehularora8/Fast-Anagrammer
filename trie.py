"""
Implementation of TRIE Data Structure
TODO: Implement private variables and getter/setter methods
"""

class TRIEnode(object):
	"""
	Class for TRIE implementing linked nodes.
	"""

	def __init__(self, char: str):

		# Character housed by nose
		self.char = char
		# List to maintain children of this node
		self.children = []
		# Is this a leaf node
		self.leaf = False
		# How many words does this character appear in
		self.counter = 1

class TRIE(object):

	def __init__(self):
		"""
		Empty constructor, initializes root.  
		"""
		self.root = TRIEnode('*')

	def __init__(self, words: [str]):
		"""
		Constructs TRIE from list of words,
		initializes root and adds all words.  
		"""
		self.root = TRIEnode('*')
		for word in words: 
			self.addWord(word)

	def addWord(self, word: str):

		"""
		Function to add word.
		"""

		word = word.upper()

		currNode = self.root

		for ch in word:

			charInChildren = False

			for child in currNode.children:
				# Loop over all children of current node, starting at root
				if child.char == ch:
					# Child with next char found
					child.counter += 1
					currNode = child
					charInChildren = True
					break

			if not charInChildren: 
				# If child with char is not found
				# Append new trie node to children list
				newNode = TRIEnode(ch)
				currNode.children.append(newNode)
				currNode = newNode

		# End of word, mark leaf as true
		currNode.leaf = True


	def findPrefix(self, prefix: str) -> (bool, int):

		"""
		Function to find if prefix exists in
		the TRIE
		Returns tuple containing:
		- a bool indictaing if prefix was found
		- an int indicating how many words use that node
		"""

		prefix = prefix.upper()

		# Start at root node
		currNode = self.root

		"""
		Loop through characters in prefix
		break if character is not found in current
		node's child
		"""
		for ch in prefix: 

			charFound = False

			for child in currNode.children:

				if child.char == ch:
					currNode = child
					charFound = True
					break

			if not charFound:
				return (False, 0)

		return (True, currNode.counter)

	def findWord(self, word: str) -> bool:

		"""
		Function to find if prefix exists in
		the TRIE
		Returns tuple containing:
		- a bool indictaing if prefix was found
		- an int indicating how many words use that node
		"""

		word = word.upper()

		# Start at root node
		currNode = self.root

		"""
		Loop through characters in prefix
		break if character is not found in current
		node's child
		"""
		for ch in word: 

			charFound = False

			for child in currNode.children:

				if child.char == ch:
					currNode = child
					charFound = True
					break

			if not charFound:
				return False

		return currNode.leaf == True
