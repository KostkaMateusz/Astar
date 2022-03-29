from fastapi import FastAPI
from models import AStarParams
from astar import generate_image
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# add cross


@app.post("/")
def root(aStarParams: AStarParams):

    dict_of_parameters = dict([ele for ele in aStarParams])
    print(dict_of_parameters)
    img = generate_image(**dict_of_parameters)
    image = io.BytesIO()

    img.savefig(image, format="png")
    image.seek(0)

    return StreamingResponse(image, media_type="image/png")
