import random
import time


random.seed(time.time())


def func(chance: float) -> bool:
	return random.random() <= chance


for i in range(10):
	result = [func(0.5) for i in range(1000000)]
	print(f'True: {result.count(True) / 10000}')
	print(f'False: {result.count(False) / 10000}')
	print('-' * 20)
  
