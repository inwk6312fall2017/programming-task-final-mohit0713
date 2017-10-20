x = open("Book1.txt", "r") #open first file
y = open("Book2.txt", "r") #open second file
z = open("Book2.txt", "r") #open third file


def find_big(a):  			# this function will check the  biggest in all the books):
	longest_word = ''
	for word in a.read().split():
		print(word, len(word))


find_big(x)
