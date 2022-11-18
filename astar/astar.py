import numpy
import random
from .field import Field
from .plot import create_plot


def a_star_engine(global_object_table: list[list[Field]], start_x, start_y, end_x, end_y, weight):

    open_list = []
    closed_list = []
    open_list.append(global_object_table[start_x][start_y])
    success = False
    while open_list and not success:

        currentNode = min(open_list, key=lambda element: element.value_of_f)
        index = open_list.index(currentNode)
        successors = open_list.pop(index).list_of_neighbors
        closed_list.append(currentNode)
        

        if currentNode.value == -1:
            success = True
            break
        
        for child in successors:            
            if child is None or child in closed_list:
                continue
            elif child.value == 0:
                closed_list.append(child)
                continue

            child.parent = currentNode
            g = currentNode.g + Field.distance_calculator(currentNode, child)
            h = Field.distance_calculator(child, global_object_table[end_y][end_x]) * weight

            if child in open_list:
                if child.g > g:
                    continue
            child.g = g
            child.h = h
            open_list.append(child)

    return success, currentNode


def find_values(array: list[list[int]],value:int):
    for i,x in enumerate(array):
        if value in x:
            return i,x.index(value)

def findObstacles(Map):
    list_of_obstacles=[]
    for i,row in enumerate(Map):
        if 0 in row:
            list_of_obstacles.append([row.index(0),i])
    return list_of_obstacles


def generate_image_from_json(input_map):

    start_x,start_y=find_values(input_map,2) 
    end_x,end_y=find_values(input_map,-1)   
    weight=1

    list_of_obstacles=findObstacles(input_map)

    global_object_table = Field.array_creation(input_map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)
    image = create_plot(global_object_table, list_of_obstacles, success, target)

    return image


def generate_object_list(input_map):

    start_x,start_y=find_values(input_map,2)
 
    end_x,end_y=find_values(input_map,-1)
   
    weight=1
    
    global_object_table = Field.array_creation(input_map)

    _, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)


    path_X = [val[0] for val in Field.find_path(target)]
    path_Y = [val[1] for val in Field.find_path(target)]

    path = [{"X":path_X[i], "Y":path_Y[i]} for i in range(0, len(path_X))]

    return path

    



