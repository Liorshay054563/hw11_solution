# start
import random


## a + b
list_bool: list[bool] = [random.choice([True, False])  for i in range(3)]
print(all(list_bool))
#c
print(any(list_bool))
#d
if not any([False, False, False, False]):
    print('All False')
#e
if not all([False, False, False, False]):
    print('at least one False')
#f
list_int: list[int] = [random.randint(-2, 2)  for i in range(5)]
print(list_int)
#g
print(all(list_int))
#h
print(any(list_int))
#i
if not all(list_int):
    print("all 0")
#j
if not any(list_int):
    print("at least 1 0")

