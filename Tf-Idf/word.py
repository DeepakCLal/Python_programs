
#Import the class Preprocessor from the file preprocessor_30535816.py
from preprocessor import Preprocessor
class WordAnalyser:
	def __init__(self):
		#Initialise an instance variable which is a dictionary which will hold the word counts of the cleaned text.
		self.word_counts = dict()
	def __str__(self):
		#Use string method to print out the word counts of the document.
		return str(self.word_counts)
	def analyse_words(self, book_text):
		#Initialise a list to store each words of the document.
		word_list = list()
		#Initialise a list to store the contents of the document after each line
		sen_list = list()
		#Add the contents into word_list and sen_list.
		sen_list = book_text.split('\n')
		for characters in sen_list:
			word_list += characters.split(' ')
		#Extract the unique elements from word_list.
		word_set = set(word_list)
		#Calculate the word count of the words present in the document and store it into self.word_counts.
		for element in word_set:
			count = 0
			for each_word in word_list:
				if each_word == element:
					count += 1
			self.word_counts[element] = count
	def get_word_frequency(self):
		#Initialise a variable which is a dictionary which will hold the word frequency of the document.
		freq = dict()
		#Initialise a variable to calculate the total count and store the value into.
		total_count = 0
		#Calculate the word frequency and store it into freq.
		for items in self.word_counts:
			if items != '':
				total_count += self.word_counts[items]
		for elements in self.word_counts:
			if elements != '':
				freq[elements] = self.word_counts[elements]/total_count
		return freq

#Initialise objects to call WordAnalyser and Preprocessor within the main function.

def main():
	clean_ob = Preprocessor()
	reading_text = input("enter the text")
	clean_ob.read_text(reading_text)
	clean_ob.clean()
	word_ob = WordAnalyser()
	word_ob.analyse_words(clean_ob.book_content)
	word_ob.get_word_frequency()
	print(word_ob)
	print(word_ob.get_word_frequency())

if __name__ == '__main__':
	main()