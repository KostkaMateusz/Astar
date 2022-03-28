from pole import Pole
from plot import create_plot
import numpy


start_x = 0
start_y = 3
end_x = 4
end_y = 2
map_size_x = 5
map_size_y = 5
list_of_obstacles = [[2, 1], [3, 1], [1, 3], [2, 3], [4, 4]]


def generate_map(start_x: int, start_y: int, end_x: int, end_y: int, map_size_x: int, map_size_y: int, list_of_obstacles: list) -> list[list[int]]:
    """elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start"""
    map = numpy.full((map_size_x, map_size_y), 1)
    map[start_x][start_y] = 2
    map[end_x][end_y] = -1
    for obstacles in list_of_obstacles:
        map[obstacles[1]][obstacles[0]] = 0
    return map


def a_star_engine(global_object_table: list[list[Pole]], start_x, start_y, end_x, end_y):

    open_list = []
    closed_list = []
    finish_x = None
    finish_y = None

    open_list.append(global_object_table[start_x][start_y])
    finded = False
    while len(open_list) != 0 and finded != True:
        minimum = min([element.value_of_f for element in open_list])
        index_with_min = -1
        for index, element in enumerate(open_list):
            if element.value_of_f == minimum:
                index_with_min = index
                break

        q = open_list.pop(index_with_min)
        for neigh in q.list_of_neighbors:
            if neigh is not None and neigh.value != 0:
                if neigh.value == -1:
                    # print("Znalazłem")
                    finish_x = neigh.x_position
                    finish_y = neigh.y_position
                    finded = True
                    break
                neigh.g = q.g + Pole.distance_calculator(neigh, q)
                neigh.h = Pole.distance_calculator(neigh, global_object_table[end_x][end_y])
                if neigh in open_list:
                    print(f"Opened:x_position:{neigh.x_position} y_position:{neigh.y_position}")
                    continue
                if neigh in closed_list:
                    print(f"Closed:x_position:{neigh.x_position} y_position:{neigh.y_position}")
                    continue
                # print(f"X:{neigh.x_position} Y:{neigh.y_position}")
                open_list.append(neigh)

        create_plot(global_object_table)
        closed_list.append(q)

    return finish_x, finish_y


if __name__ == "__main__":

    map = generate_map(start_x, start_y, end_x, end_y, map_size_x, map_size_y, list_of_obstacles)
    global_object_table = Pole.array_creation(map)
    x, y = a_star_engine(global_object_table, start_x, start_y, end_x, end_y)
    print(x, y)
    create_plot(global_object_table)
