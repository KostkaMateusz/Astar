import numpy
import random
from .pole import Pole
from .plot import create_plot


def generate_list_random_obstacles(number_of_obstacles, map_size_x: int, map_size_y: int):
    list_of_obstacles = []
    for i in range(number_of_obstacles):
        x = random.randint(1, map_size_x)
        y = random.randint(1, map_size_y)
        list_of_obstacles.append([y - 1, x - 1])
    return list_of_obstacles


# list_of_obstacles = [[2, 1], [3, 1], [1, 3], [2, 3], [4, 4]]


def generate_map(start_x: int, start_y: int, end_x: int, end_y: int, map_size_x: int, map_size_y: int, list_of_obstacles: list[list[int]]) -> list[list[int]]:
    """elements 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start"""
    map = numpy.full((map_size_x, map_size_y), 1)
    map[start_x][start_y] = 2
    map[end_x][end_y] = -1
    for obstacles in list_of_obstacles:
        map[obstacles[1]][obstacles[0]] = 0

    return map


def a_star_engine(global_object_table: list[list[Pole]], start_x, start_y, end_x, end_y, weight):

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
            g = currentNode.g + Pole.distance_calculator(currentNode, child)
            h = Pole.distance_calculator(child, global_object_table[end_y][end_x]) * weight

            if child in open_list:
                if child.g > g:
                    continue
            child.g = g
            child.h = h
            open_list.append(child)

    return success, currentNode


def generate_image(map_size_x, map_size_y, start_x, start_y, end_x, end_y, random, weight, number_of_obstacles):

    list_of_obstacles = generate_list_random_obstacles(number_of_obstacles, map_size_x, map_size_y)
    map = generate_map(start_x, start_y, end_x, end_y, map_size_x, map_size_y, list_of_obstacles)
    global_object_table = Pole.array_creation(map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)
    image = create_plot(global_object_table, list_of_obstacles, success, target)

    return image


if __name__ == "__main__":

    map_size_x = 11
    map_size_y = 11
    start_x = 3
    start_y = 2
    end_x = 10
    end_y = 10
    weight = 2
    number_of_obstacles = 5

    list_of_obstacles = generate_list_random_obstacles(number_of_obstacles, map_size_x, map_size_y)
    map = generate_map(start_x, start_y, end_x, end_y, map_size_x, map_size_y, list_of_obstacles)
    global_object_table = Pole.array_creation(map)
    success, target = a_star_engine(global_object_table, start_x, start_y, end_x, end_y, weight)
    create_plot(global_object_table, list_of_obstacles, success, target)
