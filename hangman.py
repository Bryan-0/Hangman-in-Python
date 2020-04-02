class Hangman():

	def __init__(self, word):
		self.word = word
		self.attempts = 10

	def get_attempts(self):
		return self.attempts

	def get_word(self):
		return self.word

	def encrypt_word(self):
		self.wList = []
		self.eList = []
		output = ""

		for letter in self.word:
			self.wList.append(letter)
			self.eList.append("_")

		for letter in self.eList:
			output += " {} ".format(letter)

		print("     			{}                    ".format(output))

	def check_letter(self, letter):
		output = ""

		if letter in self.wList:

			for index in range(len(self.wList)):

				if letter == self.wList[index]:

					if self.wList.count(letter) >= 2:
						repeated = []

						for i in range(len(self.wList)): 
							if self.wList[i] == letter:
								repeated.append(i)

						for ind in repeated:		
							self.eList.insert(ind, letter)
							self.eList.pop(ind + 1)
						
					self.eList.insert(self.wList.index(letter), letter)
					self.eList.pop(self.eList.index(letter) + 1)

			for letter in self.eList:
				output += " {} ".format(letter)
			print("     			{}                    ".format(output))
		else:
			self.attempts -= 1
			for letter in self.eList:
				output += " {} ".format(letter)
			print("     			{}                    ".format(output))

	def check_win(self):
		if "_" not in self.eList:
			return True
		else:
			return False


print("")
print("Welcome to Hangman!")
print("")
print("Write a word so others can try to guess which word is!")
print("You only have 10 attempts so think wisely!")
print("")
print("Created by Brayan Ayala")
print("")

word = input("Write the word you want others to guess: ")


game = Hangman(word)
game.encrypt_word()

while game.get_attempts() != 0:
	print("Attempts left: {}".format(game.get_attempts()))
	letter = input("Write a letter to guess the word: ")
	game.check_letter(letter)

	if game.check_win():
		print("YOU WON!")
		break

if game.get_attempts() == 0:
	print("YOU LOSE! :(")
