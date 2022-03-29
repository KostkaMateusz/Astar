import imp
from fastapi import FastAPI
from models import AStarParams
from astar import generate_image


app = FastAPI()


# then generate one image
# then send plot


@app.post("/")
def root(aStarParams: AStarParams):

    dict_of_parameters = dict([ele for ele in aStarParams])
    print(dict_of_parameters)
    generate_image(**dict_of_parameters)

    return aStarParams
