from pole import Pole
import numpy as np
import matplotlib.pyplot as plt


def create_plot(object_table: list[list[Pole]]):

    values = np.array([[element.value_of_f for element in row] for row in object_table])

    fig, ax = plt.subplots()
    im = ax.imshow(values)

    # # Show all ticks and label them with the respective list entries
    ax.set_xticks(
        np.arange(len(object_table[0])),
        labels=[element for element in range(len(object_table[0]))],
    )
    ax.set_yticks(
        np.arange(len(object_table)),
        labels=[element for element in range(len(object_table))],
    )

    # # # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.axvline(x=2, color="red")
    plt.axhline(y=4, color="red")
    rectangle = plt.Rectangle((0, 0), 1, 2, ec="red")
    plt.gca().add_patch(rectangle)
    # Loop over data dimensions and create text annotations.
    for i in range(len(object_table)):
        for j in range(len(object_table[1])):
            text = ax.text(j, i, values[i, j], ha="center", va="center", color="w")

    ax.set_title("Astar")
    fig.tight_layout()
    plt.show()
