import copy


class Field:
    up = None
    right = None
    down = None
    left = None
    h = 0
    g = 0
    parent = None

    def __init__(self, x: int, y: int, value: int):
        self.x_position = x
        self.y_position = y
        self.value = value

    def __str__(self):
        return f"X:{self.x_position};Y:{self.y_position};Value:{self.value}"

    def print_parents(self):
        print(self)
        if self.parent != None:
            self.parent.print_parents()

    @property
    def list_of_neighbors(self):
        return [self.up, self.right, self.down, self.left]

    @property
    def value_of_f(self):
        return self.h + self.g

    @staticmethod
    def print_table(table):
        for row in table:
            table_row = ""
            for element in row:
                table_row += f"X:{element.x_position} Y:{element.y_position} F:{element.value_of_f} G:{element.g} H:{element.h} |"
            print(table_row)

    @staticmethod
    def generate_json(table):
        object_list = []
        for row in table:
            for element in row:
                object = {
                    "X": element.x_position,
                    "Y": element.y_position,
                    "V": int(element.value),
                    "F": element.value_of_f,
                    "G": element.g,
                    "H": element.h,
                }
                object_list.append(object)
        return object_list

    @staticmethod
    def print_all_items(table):
        for row in table:
            for element in row:
                print(element)
                print("UP:" + str(element.up))
                print("LEFT:" + str(element.left))
                print("DOWN:" + str(element.down))
                print("RIGHT:" + str(element.right))
                print("H:" + str(element.h))
                print("G:" + str(element.g))
                print("F:" + str(element.value_of_f))
                print("________________")

    @staticmethod
    def array_creation(table_of_elements: list[list[int]]) -> list[list]:
        table = list()
        for row_counter, row in enumerate(table_of_elements):
            row_table = list()
            for columne_counter, element_value in enumerate(row):
                row_table.append(Field(columne_counter, row_counter, element_value))
            table.append(row_table)
        # after creation of a array of object calculate references to neighbors
        Field.calculate_neighbors(table)
        return copy.deepcopy(table)

    @staticmethod
    def calculate_neighbors(table):
        for row in table:
            for element in row:
                neighbor_addreses_up_y = element.y_position - 1
                neighbor_addreses_right_x = element.x_position + 1
                neighbor_addreses_down_y = element.y_position + 1
                neighbor_addreses_left_x = element.x_position - 1

                if neighbor_addreses_up_y >= 0 and neighbor_addreses_up_y <= len(table) - 1:
                    table[element.y_position][element.x_position].up = table[neighbor_addreses_up_y][element.x_position]

                if neighbor_addreses_right_x >= 0 and neighbor_addreses_right_x <= len(row) - 1:
                    table[element.y_position][element.x_position].right = table[element.y_position][neighbor_addreses_right_x]

                if neighbor_addreses_down_y >= 0 and neighbor_addreses_down_y <= len(table) - 1:
                    table[element.y_position][element.x_position].down = table[neighbor_addreses_down_y][element.x_position]

                if neighbor_addreses_left_x >= 0 and neighbor_addreses_left_x <= len(row) - 1:
                    table[element.y_position][element.x_position].left = table[element.y_position][neighbor_addreses_left_x]

    @staticmethod
    def distance_calculator(place1, place2) -> int:
        distance_x = abs(place1.x_position - place2.x_position)
        distance_y = abs(place1.y_position - place2.y_position)
        return distance_x + distance_y

    @staticmethod
    def find_path(Node):
        path = []

        def way(Node: Field):
            if Node != None:
                path.append([Node.x_position, Node.y_position])
                way(Node.parent)

        way(Node)
        return path[::-1]
