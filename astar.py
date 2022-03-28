from pole import Pole
from plot import create_plot
import numpy

start_x = 0
start_y = 3


end_x = 25
end_y = 25


map_size_x = 40
map_size_y = 30
list_of_obstacles = [[2, 1], [3, 1], [1, 3], [2, 3], [4, 4]]


def generate_map(start_x: int, start_y: int, end_x: int, end_y: int, map_size_x: int, map_size_y: int, list_of_obstacles: list[list[int]]) -> list[list[int]]:
    """elements 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start"""
    map = numpy.full((map_size_x, map_size_y), 1)
    map[start_x][start_y] = 2
    map[end_x][end_y] = -1
    for obstacles in list_of_obstacles:
        map[obstacles[1]][obstacles[0]] = 0
    return map


def a_star_engine(global_object_table: list[list[Pole]], start_x, start_y, end_x, end_y):

    open_list = []
    closed_list = []
    open_list.append(global_object_table[start_x][start_y])
    success = False

    while open_list and not success:

        minimum = 99999
        index_with_min = -1

        for index, element in enumerate(open_list):
            if element.value_of_f <= minimum:
                minimum = element.value_of_f
                index_with_min = index

        currentNode = open_list[index_with_min]
        successors = open_list.pop(index_with_min).list_of_neighbors
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
            g = currentNode.g + Pole.distance_calculator(currentNode, child)
            h = Pole.distance_calculator(child, global_object_table[end_y][end_x]) * 2

            if child in open_list:
                if child.g > g:
                    continue
            child.g = g
            child.h = h
            open_list.append(child)

    return success, currentNode


if __name__ == "__main__":

    map = generate_map(start_x, start_y, end_x, end_y, map_size_x, map_size_y, list_of_obstacles)
    global_object_table = Pole.array_creation(map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y)
    create_plot(global_object_table, list_of_obstacles, success, target)
