from .field import Field
import numpy as np
import matplotlib.pyplot as plt


def draw_path(path):
    x = [cor[0] for cor in path]
    y = [cor[1] for cor in path]
    plt.plot(x, y, color="green")


def create_plot(object_table: list[list[Field]], list_of_obstacles: list[list[int]], target: Field):

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

    # Loop over data dimensions and create obstacles.
    for obstacles in list_of_obstacles:
        rectangle = plt.Rectangle((-0.5 + obstacles[0], -0.5 + obstacles[1]), 1, 1, ec="red")
        plt.gca().add_patch(rectangle)

    path = Field.find_path(target)
    # start circle
    circle = plt.Circle(path[0], 0.2, ec="green")
    plt.gca().add_patch(circle)

    # end circle
    circle = plt.Circle(path[-1], 0.2, ec="yellow")
    plt.gca().add_patch(circle)

    # Loop over data dimensions and create text annotations.
    for i in range(len(object_table)):
        for j in range(len(object_table[1])):
            text = ax.text(j, i, round(values[i, j]), ha="center", va="center", color="w")

    # path from start to end
    draw_path(path)
    # set white colors
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_color("white")
    ax.spines["right"].set_color("white")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    plt.xlabel("X")
    plt.ylabel("Y")
    fig.tight_layout()
    plt.gcf()

    return plt
