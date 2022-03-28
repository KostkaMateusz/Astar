from pole import Pole
import numpy as np
import matplotlib.pyplot as plt


def create_plot(object_table: list[list[Pole]]):

    values = np.array([[element.value_of_f for element in row] for row in object_table])

    fig, ax = plt.subplots()
    im = ax.imshow(values)

    # # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(5), labels=[0, 1, 2, 3, 4])
    ax.set_yticks(np.arange(5), labels=[0, 1, 2, 3, 4])

    # # # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(object_table)):
        for j in range(len(object_table[1])):
            text = ax.text(j, i, values[i, j], ha="center", va="center", color="w")

    ax.set_title("Astar")
    fig.tight_layout()
    plt.show()
