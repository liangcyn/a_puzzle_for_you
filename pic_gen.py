import numpy
from PIL import Image



def convert_string_to_color(s):
	ls = []
	for c in s:
		ls.append(ord(c))

	return ls


result = convert_string_to_color("a b c hi tom! welcome to the first round of riddles. your code to go on is: brannerdining. send me the code to move onto the next round.")

data = numpy.zeros((1, 1000, 3), dtype=numpy.uint8)

for i in range(len(result)):
	data[0,i] = [result[i], 0, 0]

image = Image.fromarray(data)

image.save("lets_start_at_the_very_beginning.png")
