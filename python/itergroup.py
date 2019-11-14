from itertools import groupby
from functools import reduce
things = [("animal", "bear","F"), ("animal","human","F"),("animal", "duck","M"), ("plant", "cactus","M"), ("vehicle", "speed boat","M"), ("vehicle", "school bus","M")]
key= groupby(things, lambda x: x[2])
for i in key:
	print(i[0],len(list(i[1])))
