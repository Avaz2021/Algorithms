# ss.py

# Последовательный поиск - поисковой алгоритм, который проверяет каждый элемент в структуре данных на предмет его соответствия тому, что ищет алгоритм

def ss(number_list, n):
	found = False
	for i in number_list:
		if i == n:
			found = True
			break
	return found

nums = list(range(0, 100)) # 0-99
s1 = ss(nums, 98)
print(s1)

s2 = ss(nums, 101)
print(s2)
