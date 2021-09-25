# pallindrom.py
# Паллиндром - Число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.

def pallindrom(word):
	word = word.lower() # Уменьшение регистра
	word = word[::-1] == word
	return word

print(pallindrom("Анна"))
print(pallindrom("Аня"))
