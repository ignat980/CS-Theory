from random import shuffle

def monotonic(numbers):
	return all([x <= y for x, y in zip(numbers, numbers[1:])])

def bogosort(numbers):
	i = 0
	while not monotonic(numbers):
		if i % 100 == 0:
			print(i, numbers)
		shuffle(numbers)
		i += 1

if __name__ == '__main__':
	numbers = [17, 5, 13, 213, 99, 123]
	bogosort(numbers)
	print(numbers)