from pole import Pole
from typing import List

#elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start
tablica_elementow=[[1,1,1,2,1],[1,1,0,0,1],[1,1,1,1,1],[1,0,0,1,1],[1,1,-1,0,1]]

global_object_table=[]

def array_creation(table_of_elements:List[List[int]]):
    for row_counter,row in enumerate(table_of_elements):
        row_object_table=[]
        for columne_counter,element_value in enumerate(row):            
            row_object_table.append(Pole(row_counter,columne_counter,element_value))
        global_object_table.append(row_object_table)

def calculate_neighbor(object_table:List[List[Pole]]):
    #simple mathematic reference
    #change hardcoded values
    #later add recursive finding
    for row in object_table:
        for element in row:
            neighbor_addreses_up_y=element.y_position+1
            neighbor_addreses_right_x=element.x_position+1
            neighbor_addreses_down_y=element.y_position-1
            neighbor_addreses_left_x=element.x_position-1
            
            if neighbor_addreses_up_y>=0 and neighbor_addreses_up_y<=4:
                global_object_table[element.x_position][element.y_position].up=global_object_table[element.y_position][neighbor_addreses_up_y]
            
            if neighbor_addreses_right_x>=0 and neighbor_addreses_right_x<=4:
                global_object_table[element.x_position][element.y_position].right=global_object_table[neighbor_addreses_right_x][element.y_position]
            
            if neighbor_addreses_down_y>=0 and neighbor_addreses_down_y<=4:
                global_object_table[element.x_position][element.y_position].down=global_object_table[element.y_position][neighbor_addreses_down_y]
            
            if neighbor_addreses_left_x>=0 and neighbor_addreses_left_x<=4:
                global_object_table[element.x_position][element.y_position].left=global_object_table[neighbor_addreses_left_x][element.y_position]
                
            


array_creation(table_of_elements=tablica_elementow)
calculate_neighbor(global_object_table)


print(global_object_table[4][3])
print(global_object_table[4][3].right)