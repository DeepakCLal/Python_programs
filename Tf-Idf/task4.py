
#Import the class Preprocessor from the file preprocessor_30535816.py
from preprocessor import Preprocessor
#Import the class WordAnalyser from the file word_30535816.py
from word import WordAnalyser
#Import the class IDFAnalyser from the file idf_30535816.py
from idf import IDFAnalyser

def choice(term,documents):
	#Obtain the idf values of the term for different documents
	itermfreq = documents.get_IDF(term)
	#Obtain the frequency values of the term for different documents
	termfreq = documents.data[term]
	#Multiply the frequency and idf values of the term for different documents
	totfreq = itermfreq * termfreq
	#Extract the document with the highest result
	resultfreq = max(totfreq)
	#Return the document with the highest result
	return str(totfreq[totfreq == resultfreq].index)

#Initialise objects to call WordAnalyser, Preprocessor and IDFAnalyser within the main function.
#Extract the TF-IDF values for a term by calling the function choice within the main function.
def main():
	clean_ob1 = Preprocessor()
	clean_ob1.read_text('1952-0.txt')
	clean_ob1.clean()
	word_ob1 = WordAnalyser()
	word_ob1.analyse_words(clean_ob1.book_content)
	frequen1 = word_ob1.get_word_frequency()
	idfana1 = IDFAnalyser()
	idfana1.load_frequency(frequen1,'1952-0.txt')
	clean_ob2 = Preprocessor()
	clean_ob2.read_text('11-0.txt')
	clean_ob2.clean()
	word_ob2 = WordAnalyser()
	word_ob2.analyse_words(clean_ob2.book_content)
	frequen2 = word_ob2.get_word_frequency()
	idfana1.load_frequency(frequen2,'11-0.txt')
	clean_ob3 = Preprocessor()
	clean_ob3.read_text('1661-0.txt')
	clean_ob3.clean()
	word_ob3 = WordAnalyser()
	word_ob3.analyse_words(clean_ob3.book_content)
	frequen3 = word_ob3.get_word_frequency()
	idfana1.load_frequency(frequen3,'1661-0.txt')
	clean_ob4 = Preprocessor()
	clean_ob4.read_text('1342-0.txt')
	clean_ob4.clean()
	word_ob4 = WordAnalyser()
	word_ob4.analyse_words(clean_ob4.book_content)
	frequen4 = word_ob4.get_word_frequency()
	idfana1.load_frequency(frequen4,'1342-0.txt')
	clean_ob5 = Preprocessor()
	clean_ob5.read_text('pg16328.txt')
	clean_ob5.clean()
	word_ob5 = WordAnalyser()
	word_ob5.analyse_words(clean_ob5.book_content)
	frequen5 = word_ob5.get_word_frequency()
	idfana1.load_frequency(frequen5,'pg16328.txt')
	clean_ob6 = Preprocessor()
	clean_ob6.read_text('84-0.txt')
	clean_ob6.clean()
	word_ob6 = WordAnalyser()
	word_ob6.analyse_words(clean_ob6.book_content)
	frequen6 = word_ob6.get_word_frequency()
	idfana1.load_frequency(frequen6,'84-0.txt')
	print(choice('gutenbergs',idfana1))

if __name__ == '__main__':
	main()
