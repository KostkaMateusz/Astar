from pydantic import BaseModel, ValidationError, validator

# API recognises in 2D array elements as 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start

class InputMap(BaseModel):
    input_map:list[list[int]]

    @validator("input_map")
    def valid_value(cls, input_table):
        for row in input_table:
            if(len(row)>40 and len(row)>2):
                raise ValueError("Lenght of the array must be smaller than 40 and grater than 2")
            for element in row:
                if element not in (-1,0,1,2):
                    raise ValueError("Value of a field must be -1 or 0 or 1 or 2")
        return input_table

    



def must_be_positive(v):
    if v <= 0:
        raise ValueError("Must be positive")
    return v


def must_be_smaller(v):
    if v > 30 or v < 5:
        raise ValueError("Map Size must be grater than 5 and smaller than 20")
    return v


def must_be_smaller_than_other(v):
    if v[0] > v[1]:
        raise ValueError(f"{v[0]} must be smaller than {v[1]}")
    return v


class AStarParams(BaseModel):
    map_size_x: int
    map_size_y: int
    start_x: int
    start_y: int
    end_x: int
    end_y: int
    weight: int

    number_of_obstacles: int

    # list_of_obstacles: list[list[int]] | None

    _map_size_x = validator("map_size_x", allow_reuse=True)(must_be_smaller)
    _map_size_y = validator("map_size_y", allow_reuse=True)(must_be_smaller)

    _positive_start_x = validator("start_x", allow_reuse=True)(must_be_positive)
    _positive_start_y = validator("start_y", allow_reuse=True)(must_be_positive)

    @validator("start_x")
    def x_must_be_in_map_range(cls, v, values: dict):
        if v > values.get("map_size_x", 1):
            raise ValueError("Map start_x must be smaller than map size x and bigger than 5")
        return v

    @validator("start_y")
    def y_must_be_in_map_range(cls, v, values):
        if v > values.get("map_size_y", 1):
            raise ValueError("Map start_y must be smaller than map size x")
        return v

    @validator("end_x")
    def end_x_must_be_in_map_range(cls, v, values):
        if v > values.get("map_size_x", 1):
            raise ValueError("Map end_x must be smaller than map size x")
        return v

    @validator("end_y")
    def end_y_must_be_in_map_range(cls, v, values):
        if v > values.get("map_size_y", 1):
            raise ValueError("Map end_y must be smaller than map size x")
        return v

    _positive_end_x = validator("end_x", allow_reuse=True)(must_be_positive)
    _positive_end_y = validator("end_y", allow_reuse=True)(must_be_positive)

    _positive_weight = validator("weight", allow_reuse=True)(must_be_positive)
    _positive_number_of_obstacles = validator("number_of_obstacles", allow_reuse=True)(must_be_positive)

    @validator("number_of_obstacles")
    def range_of_number_of_obstacles(cls, v, values):
        if v > values.get("map_size_y", 1) ** 2:
            raise ValueError("Number of obstalces must be lower than number of fields")
        return v
