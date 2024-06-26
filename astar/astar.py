from .field import Field


def a_star_engine(global_object_table: list[list[Field]], start_x :int, start_y:int, end_x:int, end_y:int, weight:float):

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
                if child.g >= g:
                    continue
            child.g = g
            child.h = h
            open_list.append(child)

    return currentNode


def find_values(array: list[list[int]],value:int):
    for i,x in enumerate(array):
        if value in x:
            return i,x.index(value)

def findObstacles(Map:list[list[int]]):
    list_of_obstacles=[]
    for i,row in enumerate(Map):
        if 0 in row:
            list_of_obstacles.append([row.index(0),i])
    return list_of_obstacles


def generate_object_list(input_map:list[list[int]]):

    start_x,start_y=find_values(input_map,2)
 
    end_x,end_y=find_values(input_map,-1)
   
    weight=1
    
    global_object_table = Field.array_creation(input_map)

    target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)

    path_X = [val[0] for val in Field.find_path(target)]
    path_Y = [val[1] for val in Field.find_path(target)]

    path = [{"X":path_X[i], "Y":path_Y[i]} for i in range(0, len(path_X))]

    values=[[element.value_of_f for element in row] for row in global_object_table]

    return (path,values)
