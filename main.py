from pole import Pole
from typing import List

#elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start
tablica_elementow=[[1,1,1,2,1],[1,1,0,0,1],[1,1,1,1,1],[1,0,0,1,1],[1,1,-1,0,1]]

global_object_table=[]

def array_creation(table_of_elements:List[List[int]]):
    for row_counter,row in enumerate(table_of_elements):
        row_object_table=[]
        for columne_counter,element_value in enumerate(row):            
            row_object_table.append(Pole(columne_counter,row_counter,element_value))
        global_object_table.append(row_object_table)




array_creation(table_of_elements=tablica_elementow)
print(global_object_table[0][0])