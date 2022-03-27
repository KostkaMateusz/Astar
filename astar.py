from pole import Pole
import numpy as np
import matplotlib.pyplot as plt


# elements 1 is normal place; element 0 is przeszkoda; element -1 is meta; element 2 is start
tablica_elementow = [
    [1, 1, 1, 2, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, -1, 1, 0],
]

global_object_table = Pole.array_creation(tablica_elementow)

# a star engine


def a_star_engine(global_object_table: list[list[Pole]]):

    open_list = []
    closed_list = []

    open_list.append(global_object_table[0][3])
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
                    print("Znalazłem")
                    finded = True

                    break
                neigh.g = q.g + Pole.distance_calculator(neigh, q)
                neigh.h = Pole.distance_calculator(neigh, global_object_table[4][3])
                if neigh in open_list:
                    continue
                if neigh in closed_list:
                    continue
                print(f"X:{neigh.x_position} Y:{neigh.y_position}")
                open_list.append(neigh)

        closed_list.append(q)


a_star_engine(global_object_table)


array_of_values = []

for row in global_object_table:
    table_row_values = []
    for element in row:
        table_row_values.append(element.value_of_f)
    array_of_values.append(table_row_values)


values = np.array(array_of_values)

fig, ax = plt.subplots()
im = ax.imshow(values)

# # Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(5), labels=[0, 1, 2, 3, 4])
ax.set_yticks(np.arange(5), labels=[0, 1, 2, 3, 4])

# # # Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(global_object_table)):
    for j in range(len(global_object_table[1])):
        text = ax.text(j, i, values[i, j], ha="center", va="center", color="w")


ax.set_title("Astar")
fig.tight_layout()
plt.show()
