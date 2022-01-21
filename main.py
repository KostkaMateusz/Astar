from pole import Pole
from typing import List

# elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start
tablica_elementow = [[1, 1, 1, 2, 1], [1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, -1, 0, 1]]


global_object_table = Pole.array_creation(tablica_elementow)


for row in global_object_table:
    for element in row:
        print(element)
        print("UP:"+str(element.up))
        print("LEFT:"+str(element.left))
        print("DOWN:"+str(element.down))
        print("RIGHT:"+str(element.right))
        print("________________")


