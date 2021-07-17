import string
class Preprocessor:
	def __init__(self):
		#Initialise the instance variable of the class which holds the content of the document
		self.book_content = ""
	def __str__(self):
		#Use __str__ method to print out the instance variable having the content of the document
		return str(self.book_content)
	def clean(self):
		#Initialise a temporary variable to store the values in self.book_content after making changes to it.
		temp = ""
		#Declare a variable which consists of characters from a-z and numbers from 0-9 and characters such as \n,\t etc.
		reference = string.ascii_lowercase+string.digits+string.whitespace
		#Remove anything except alphabet, numbers and spaces and replace '-' and '_' with ' ' and remove "'" and store the changes into a temporary variable
		for item in range(0,len(self.book_content)):
			if self.book_content[item].lower() in reference:
				#Convert all the characters into lower-case
				temp += self.book_content[item].lower()
			elif self.book_content[item] == '-' or self.book_content[item] == '_':
				temp += ' '
			elif self.book_content[item] == "'":
				temp += ''
			else:
				temp += ''
		#Place the contents in the temporary variable into self.book_content
		self.book_content = temp
		if len(self.book_content) == '':
			return 1
		else:
			return None
	def read_text(self, text_name):
		#Read the contents of the document and store it into the instance variable self.book_content
		with open(text_name,'r',encoding = 'utf-8') as text :
			self.book_content = text.read()

#Initialise object to call Preprocessor within the main function.

def main():
 clean_ob = Preprocessor()
 reading_text = input("enter a file name")
 clean_ob.read_text(reading_text)
 clean_ob.clean()
 print(clean_ob)
if __name__ == '__main__':
 	main()
