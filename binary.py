# binary.py

# Алгоритм перевода десятичного числа в двоичное

decimary = int(input("Десятичное число: "))
binary = ""

while decimary != 0:
	second = decimary % 2
	decimary = decimary // 2
	
	binary += str(second)

print(f"Двоичное число: {binary[::-1]}")
