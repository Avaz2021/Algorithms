# characters.py

# Алгоритм нахождения одинаковых букв в слове

def characters(string):
	string = string.lower()
	count_dict = {}
	for c in string:
		if c in count_dict:
			count_dict[c] += 1

		else:
			count_dict[c] = 1

	print(count_dict)

characters("Аваз")
