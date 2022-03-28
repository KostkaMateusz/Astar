from pole import Pole
from plot import create_plot


# elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start

start_x = 0
start_y = 3
end_x = 4
end_y = 2


tablica_elementow = [
    [1, 1, 1, 2, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, -1, 1, 0],
]

global_object_table = Pole.array_creation(tablica_elementow)


def a_star_engine(
    global_object_table: list[list[Pole]], start_x, start_y, end_x, end_y
):

    open_list = []
    closed_list = []

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
                    finded = True
                    break
                neigh.g = q.g + Pole.distance_calculator(neigh, q)
                neigh.h = Pole.distance_calculator(
                    neigh, global_object_table[end_x][end_y]
                )
                if neigh in open_list:
                    continue
                if neigh in closed_list:
                    continue
                # print(f"X:{neigh.x_position} Y:{neigh.y_position}")
                open_list.append(neigh)

        closed_list.append(q)


if __name__ == "__main__":

    a_star_engine(global_object_table, 0, 3, 4, 3)
    create_plot(global_object_table)
