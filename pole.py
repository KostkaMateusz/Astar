from typing import List


class Pole:
    # this filds are for reference to neighbors
    up = None
    right = None
    down = None
    left = None
    global_object_table = []
    h=0
    g=0
    
  
    def __init__(self, x: int, y: int, value: int):
        self.x_position = x
        self.y_position = y
        self.value = value

    def __str__(self):
        return f"X:{self.x_position};Y:{self.y_position};Value:{self.value}"
    

    @property
    def list_of_neighbors(self):
        return [self.up,self.right,self.down,self.left]
    
    @property
    def value_of_f(self):
        return self.h+self.g
    
    @classmethod
    def print_table(cls):
        for row in cls.global_object_table:
            table_row=""
            for element in row:
                table_row+=f"X:{element.x_position} Y:{element.y_position} F:{element.value_of_f} G:{element.g} H:{element.h} |"
            print(table_row)
    
    @classmethod
    def print_all_items(cls):        
        for row in cls.global_object_table:
            for element in row:
                print(element)
                print("UP:"+str(element.up))
                print("LEFT:"+str(element.left))
                print("DOWN:"+str(element.down))
                print("RIGHT:"+str(element.right))
                print("H:"+str(element.h))
                print("G:"+str(element.g))
                print("F:"+str(element.value_of_f))
                print("________________")

    @classmethod
    def array_creation(cls, table_of_elements: List[List[int]]) -> List[List]:
        for row_counter, row in enumerate(table_of_elements):
            row_object_table = []
            for columne_counter, element_value in enumerate(row):
                row_object_table.append(Pole(columne_counter,row_counter, element_value))
            cls.global_object_table.append(row_object_table)
        # after creation of a array of object calculate references to neighbors
        Pole.calculate_neighbors()   
        return cls.global_object_table

    @classmethod
    def calculate_neighbors(cls):
        # simple mathematic reference        
        # later add recursive finding
        for row in cls.global_object_table:
            for element in row:
                neighbor_addreses_up_y = element.y_position-1
                neighbor_addreses_right_x = element.x_position+1
                neighbor_addreses_down_y = element.y_position+1
                neighbor_addreses_left_x = element.x_position-1

                if neighbor_addreses_up_y >= 0 and neighbor_addreses_up_y <= len(cls.global_object_table)-1:
                    cls.global_object_table[element.y_position][element.x_position].up = cls.global_object_table[neighbor_addreses_up_y][
                        element.x_position]

                if neighbor_addreses_right_x >= 0 and neighbor_addreses_right_x <= len(row)-1:
                    cls.global_object_table[element.y_position][element.x_position].right = cls.global_object_table[element.y_position][
                        neighbor_addreses_right_x]

                if neighbor_addreses_down_y >= 0 and neighbor_addreses_down_y <= len(cls.global_object_table)-1:
                    cls.global_object_table[element.y_position][element.x_position].down = cls.global_object_table[neighbor_addreses_down_y][
                        element.x_position]

                if neighbor_addreses_left_x >= 0 and neighbor_addreses_left_x <= len(row)-1:
                    cls.global_object_table[element.y_position][element.x_position].left = cls.global_object_table[element.y_position][
                        neighbor_addreses_left_x]
