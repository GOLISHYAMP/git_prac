from urllib.request import urlopen

def __fetch_words__():
	story = urlopen('https://www.udemy.com/course/ros-tutorials/')
	story_words = []
	for line in story:
		line_words = line.decode('utf8').split()
		for word in line_words:
			story_words.append(word)

	for word in story_words:
		print(word)

if __name__ == '__main__':
	print("hiii re hai need nahi hai")
	__fetch_words__()