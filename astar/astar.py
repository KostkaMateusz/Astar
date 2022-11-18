import numpy
import random
from .field import Field
from .plot import create_plot


def generate_list_random_obstacles(number_of_obstacles, map_size_x: int, map_size_y: int):
    list_of_obstacles = []
    for _ in range(number_of_obstacles):
        x = random.randint(1, map_size_x)
        y = random.randint(1, map_size_y)
        list_of_obstacles.append([y - 1, x - 1])
    return list_of_obstacles


def generate_map(start_x: int, start_y: int, end_x: int, end_y: int, map_size_x: int, map_size_y: int, list_of_obstacles: list[list[int]]) -> list[list[int]]:
    """elements 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start"""
    map = numpy.full((map_size_x, map_size_y), 1)
    map[start_x][start_y] = 2
    map[end_x][end_y] = -1
    for obstacles in list_of_obstacles:
        map[obstacles[1]][obstacles[0]] = 0

    return map


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



def generate_image(map_size_x, map_size_y, start_x, start_y, end_x, end_y, weight, number_of_obstacles):

    list_of_obstacles = generate_list_random_obstacles(number_of_obstacles, map_size_x, map_size_y)
    map = generate_map(start_x, start_y, end_x, end_y, map_size_x, map_size_y, list_of_obstacles)
    global_object_table = Field.array_creation(map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)
    image = create_plot(global_object_table, list_of_obstacles, success, target)

    return image


#ToDO find obstacles in json

def findObstacles(Map):
    list_of_obstacles=[]
    for i,row in enumerate(Map):
        if 0 in row:
            list_of_obstacles.append([row.index(0),i])
    return list_of_obstacles


def generate_image_from_json(input_map):

    start_x,start_y=find_values(input_map,2) 
    end_x,end_y=find_values(input_map,-1)   
    weight=1.005

    list_of_obstacles=findObstacles(input_map)

    global_object_table = Field.array_creation(input_map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)
    image = create_plot(global_object_table, list_of_obstacles, success, target)

    return image



def generate_object_list(input_map):

    start_x,start_y=find_values(input_map,2)
 
    end_x,end_y=find_values(input_map,-1)
   
    weight=1.05
    
    global_object_table = Field.array_creation(input_map)

    _, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)


    path_X = [val[0] for val in Field.find_path(target)]
    path_Y = [val[1] for val in Field.find_path(target)]

    path = [{"X":path_X[i], "Y":path_Y[i]} for i in range(0, len(path_X))]

    return path

    



