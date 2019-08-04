from random import randint

def func(chance: int) -> int:
	return randint(0, 100) <= chance


for i in range(10):
	result = [func(50) for i in range(1000000)]
	print(f'True: {result.count(True) / 10000}')
	print(f'False: {result.count(False) / 10000}')
	print('-' * 20)
	
