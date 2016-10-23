""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from string import punctuation
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

book = 'pg103.txt'
words = open(book).read().lower().split()
def process_line(line, h): #ADDED for organization; To process lines
	line = line.replace('-', ' ')
	for word in line.split(): #prep words
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()

		h[word] = h.get(word,0)+1 

def get_word_list(file_name):
	""" Header, punctuation, and whitespace are stripped away.
	  The function returns a list. All words are converted to lower case."""
	h = dict() 	#opens a file and passes back a list of its words
	final = open('pg103.txt')
	for line in final:
        	if line.rstrip() == "*** START OF THIS PROJECT GUTENBERG EBOOK AROUND THE WORLD IN 80 DAYS ***":
			break
	for line in final:
		process_line(line, h)

	return h
	

def get_top_n_words(word_list, n):
	txt = []
	for word in words:
		if word not in txt:
			txt.append(word)

	# Make a list of (count, unique) tuples.
	counts = []
	for text in txt:
		count = 0
		for word in words:     # Iterate over words?
			if word == text:   # equal to the current text?
				count += 1
		counts.append((count, text))

	counts.sort()            # Sorting the list puts the lowest counts first.
	counts.reverse()         # Reverse it, putting the highest counts first.

	important_words=[]	
	for word in counts:		
		if word not in stop_words:
			important_words.append(word)
	important_words.sort()
	important_words.reverse()
	
	# Print the ten words with the highest counts.
	for i in range(min(n, len(important_words))):
		count, word = counts[i]
		print('%s %d' % (word, count))

def main():
	get_word_list(book)	
	get_top_n_words(words, 100)
	
main()

