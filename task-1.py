x = open("Book1.txt", "r") #open first file
y = open("Book2.txt", "r") #open second file
z = open("Book2.txt", "r") #open third file


def find_big(a):  			# this function will check the  biggest in all the books):
	longest_word = ''
	for word in a.read().split():
		if len(word)> len(longest_word):
			longest_word =  word
	print (longest_word)
	return len(longest_word)


if find_big(x) >= find_big(y) and find_big(x) >= find_big(z):
	print (find_big(x))
elif find_big(y) >= find_big(x) and find_big(y) >= find_big(z):
        print (find_big(y))
elif find_big(z) >= find_big(x) and find_big(z) >= find_big(y):
        print (find_big(z))


