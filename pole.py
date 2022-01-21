from typing import List


class Pole:
    # this filds are for reference to neighbors
    up = None
    right = None
    down = None
    left = None
    global_object_table = []

    def __init__(self, x: int, y: int, value: int):
        self.x_position = x
        self.y_position = y
        self.value = value

    def __str__(self):
        return f"X:{self.x_position};Y:{self.y_position};Value:{self.value}"

    @classmethod
    def array_creation(cls, table_of_elements: List[List[int]]):
        for row_counter, row in enumerate(table_of_elements):
            row_object_table = []
            for columne_counter, element_value in enumerate(row):
                row_object_table.append(
                    Pole(row_counter, columne_counter, element_value))
            cls.global_object_table.append(row_object_table)
        return cls.global_object_table
