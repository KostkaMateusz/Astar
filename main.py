from pole import Pole
from typing import List

# elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start
tablica_elementow = [[1, 1, 1, 2, 1], [1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, -1, 1, 0]]

global_object_table = Pole.array_creation(tablica_elementow)

# Pole.print_all_items()
#a star engine

def distance_calculator(place1:Pole,place2:Pole)->int:
    distance_x=abs(place1.x_position-place2.x_position) 
    distance_y=abs(place1.y_position-place2.y_position)
    return distance_x+distance_y



def a_star_engine(global_object_table:List[List[Pole]]):

    open_list=[]
    closed_list=[]

    open_list.append(global_object_table[0][3])
    finded=False
    while(len(open_list)!=0 and finded!=True):
        minimum=min([element.value_of_f for element in open_list])
        index_with_min=-1
        for index,element in enumerate(open_list):
            if element.value_of_f==minimum:
                index_with_min=index
                break

        q=open_list.pop(index_with_min)
        for neigh in q.list_of_neighbors:
            if neigh is not None and neigh.value!=0:
                if neigh.value==-1:
                    print("Znalazłem")
                    finded=True
                    break
                neigh.g=q.g+distance_calculator(neigh,q)
                neigh.h=distance_calculator(neigh,global_object_table[4][3])
                if neigh in open_list:
                    continue
                if neigh in closed_list:
                    continue
                print(f"X:{neigh.x_position} Y:{neigh.y_position}")
                open_list.append(neigh) 

        closed_list.append(q)



a_star_engine(global_object_table)
print(global_object_table[0][3])
# Pole.print_all_items()
Pole.print_table()