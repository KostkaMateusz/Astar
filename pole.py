
class Pole:
    def __init__(self,x:int,y:int,value:int):
        self.x_position=x
        self.y_position=y
        self.value=value

    def __str__(self):
        return f"X:{self.x_position};Y:{self.y_position};Value:{self.value}"
        