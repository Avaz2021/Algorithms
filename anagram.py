# anagram.py
# Анаграмма - это когда все буквы в двух словах абсолютно 
#												одинаковые


def anagram(w1, w2):
	w1 = w1.lower()
	w2 = w2.lower()
	return sorted(w1) == sorted(w2)

print( anagram("капот", "тапок") )
print( anagram("лист", "дерево") )
