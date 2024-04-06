from pydantic import BaseModel, validator

# API recognises in 2D array elements as 1 is normal place; element 0 is an obstacle; element -1 is meta; element 2 is start

class InputMap(BaseModel):
    input_map:list[list[int]]

    @validator("input_map")
    def valid_value(cls, input_table):
        for row in input_table:
            if(len(row)>43 or len(row)<2):
                raise ValueError("Lenght of the array must be smaller than 43 and grater than 2")
            for element in row:
                if element not in (-1,0,1,2):
                    raise ValueError("Value of a field must be -1 or 0 or 1 or 2")
        return input_table

  